#!/usr/bin/env python3
"""
CTFT v3 reference engine — proves the proposed schema is executable, not just descriptive.

Loads the v3 collections (techniques, playbooks, indicators, tools), takes a challenge
*fingerprint*, and runs the agent loop from SCHEMA_V3.md section 5:

    observe -> retrieve(rank candidates) -> select -> plan(playbook steps) -> report

No CTF tools are actually invoked; step execution is simulated so the control flow,
ranking maths and tool bindings can be inspected end to end.

Usage:
    python v3/solve.py                      # runs all example fingerprints
    python v3/solve.py --validate           # also JSON-Schema-validate every object (needs jsonschema)
    python v3/solve.py --index 0            # run a single example
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def load_model():
    techniques = load("techniques.for.json")["items"]
    playbooks = {p["id"]: p for p in load("playbooks.for.json")["items"]}
    indicators = {i["id"]: i for i in load("indicators.json")["items"]}
    tools = {t["id"]: t for t in load("tools.json")["items"]}
    return techniques, playbooks, indicators, tools


def triggers_match(trig, present):
    """Boolean expression over indicator ids (all_of / any_of / none_of)."""
    all_of = all(i in present for i in trig.get("all_of", []))
    any_of = (not trig.get("any_of")) or any(i in present for i in trig.get("any_of", []))
    none_of = all(i not in present for i in trig.get("none_of", []))
    return all_of and any_of and none_of


def rank(fingerprint, techniques, playbooks, indicators):
    """
    score = sum(indicator.weight * evidence_match) * technique.prevalence   -> normalized 0..1
    Candidate is eligible only if its playbook's triggers fire.
    Deliberately crosses no tactic boundary here (single-tactic demo set), but the
    scoring key is tactic-agnostic.
    """
    present = {e["indicator"] for e in fingerprint.get("evidence", []) if e.get("value")}
    candidates = []
    for tech in techniques:
        pb = playbooks.get(tech["paired_counter"])
        if not pb or not triggers_match(pb["triggers"], present):
            continue
        raw, why = 0.0, []
        for ind_id in tech.get("indicators", []):
            if ind_id in present:
                w = indicators.get(ind_id, {}).get("weight", 0.0)
                raw += w
                why.append(f"{ind_id}({w})")
        # artifact-type prior: small boost if the technique targets this artifact
        if fingerprint["artifact_type"] in tech.get("artifact_types", []):
            raw += 0.15
            why.append(f"artifact={fingerprint['artifact_type']}(+0.15)")
        score = raw * tech.get("prevalence", 0.5)
        candidates.append({
            "technique": tech["id"],
            "playbook": pb["id"],
            "name": pb["name"],
            "raw": round(raw, 3),
            "prevalence": tech.get("prevalence", 0.5),
            "score": round(score, 3),
            "priority": pb.get("priority", 5),
            "why": why,
        })
    if candidates:
        top = max(c["score"] for c in candidates) or 1.0
        for c in candidates:
            c["score"] = round(c["score"] / top, 3)  # normalize
    # rank by score, break ties by authored priority
    return sorted(candidates, key=lambda c: (c["score"], c["priority"]), reverse=True)


def plan(playbook, tools):
    """Turn a playbook into an ordered, tool-bound step plan (simulated execution)."""
    lines = []
    for step in playbook["steps"]:
        tool = tools.get(step.get("tool") or "", {})
        cmd = tool.get("invocation", {}).get("cmd", "(manual)")
        produces = ", ".join(step.get("produces", [])) or "-"
        gate = step.get("success_when") or step.get("validates") or ""
        lines.append({
            "step": step["id"],
            "action": step["action"],
            "tool": tool.get("name", step.get("tool")),
            "cmd": cmd,
            "produces": produces,
            "gate": gate,
            "branch": {k: step[k] for k in ("on_true", "on_false") if k in step},
        })
    return lines


def run_case(fp, model, idx):
    techniques, playbooks, indicators, tools = model
    print("=" * 78)
    print(f"[{idx}] FINGERPRINT: {fp.get('label','(unlabeled)')}")
    print(f"    artifact={fp['artifact_type']}  runtime={fp.get('runtime')}  "
          f"protections={fp.get('protections')}")
    present = [e["indicator"] for e in fp.get("evidence", []) if e.get("value")]
    print(f"    observed indicators: {present}")

    ranked = rank(fp, techniques, playbooks, indicators)
    print("\n  RETRIEVE -> ranked candidates:")
    if not ranked:
        print("    (no playbook triggers fired — need more evidence)")
        return
    for c in ranked:
        print(f"    {c['score']:>5}  {c['technique']} -> {c['playbook']}  "
              f"\"{c['name']}\"  [prio {c['priority']}]  because {c['why']}")

    chosen = ranked[0]
    pb = playbooks[chosen["playbook"]]
    print(f"\n  SELECT  -> {pb['id']} (score {chosen['score']}, confidence_prior "
          f"{pb.get('confidence_prior')}, cost {pb.get('cost')}, automation {pb.get('automation')})")
    print("  PLAN    -> executable steps:")
    for s in plan(pb, tools):
        print(f"    - {s['step']:<11} {s['action']}")
        print(f"                  tool: {s['tool']:<16} cmd: {s['cmd']}")
        print(f"                  produces: {s['produces']:<28} gate: {s['gate']}")
        if s["branch"]:
            print(f"                  branch: {s['branch']}")
    print(f"  SUCCESS -> {pb.get('success_criteria')}")
    print(f"  FALLBACK-> {pb.get('fallbacks') or '(none)'}")


def validate(model):
    try:
        import jsonschema  # noqa
    except ImportError:
        print("jsonschema not installed; skipping validation "
              "(`pip install jsonschema` to enable).")
        return
    from jsonschema import validate as jv
    techniques, playbooks, indicators, tools = model
    checks = [
        ("technique.schema.json", techniques),
        ("playbook.schema.json", list(playbooks.values())),
        ("indicator.schema.json", list(indicators.values())),
        ("tool.schema.json", list(tools.values())),
    ]
    ok = 0
    for schema_name, items in checks:
        schema = load(os.path.join("schemas", schema_name))
        for it in items:
            jv(instance=it, schema=schema)
            ok += 1
    # referential integrity
    for t in techniques:
        for ind in t["indicators"]:
            assert ind in indicators, f"{t['id']} references missing {ind}"
    for pb in playbooks.values():
        for tl in pb.get("tools", []):
            assert tl in tools, f"{pb['id']} references missing {tl}"
        step_ids = {s["id"] for s in pb["steps"]}
        for s in pb["steps"]:
            for k in ("on_true", "on_false"):
                tgt = s.get(k)
                if tgt and not tgt.startswith("s3-fallback"):
                    assert tgt in step_ids or tgt.startswith("s"), \
                        f"{pb['id']}/{s['id']} {k} -> unknown {tgt}"
    print(f"VALIDATION OK: {ok} objects schema-valid; indicator/tool references resolve.\n")


def evaluate(path, model):
    """precision@k over a labelled fingerprint set (TODO 4.1).

    A case counts only if it carries `expected`. The measurement is meaningful only on a
    hold-out set: a case whose write-up was read while curating the technique measures
    memorisation, so in-sample files are labelled as such in the output.
    """
    techniques, playbooks, indicators, _ = model
    with open(path if os.path.isabs(path) else os.path.join(HERE, os.path.basename(path)),
              encoding="utf-8") as handle:
        data = json.load(handle)
    cases = [c for c in data.get("items", []) if c.get("expected")]
    in_sample = "holdout" not in os.path.basename(path)

    print("=" * 78)
    print(f"EVALUATE {os.path.basename(path)} — {len(cases)} labelled case(s)"
          f"{' [IN-SAMPLE: not a baseline]' if in_sample else ' [hold-out]'}")
    if not cases:
        print("  no labelled cases; precision@k is undefined.")
        print("  Add cases citing write-ups that were NOT used during curation.")
        print("=" * 78)
        return 0

    ks = (1, 3, 5)
    hits = {k: 0 for k in ks}
    per_domain = {}
    for case in cases:
        ranked = [c["technique"] for c in rank(case, techniques, playbooks, indicators)]
        expected = set(case["expected"])
        domain = sorted(expected)[0].split("-")[1]
        bucket = per_domain.setdefault(domain, {"n": 0, **{k: 0 for k in ks}})
        bucket["n"] += 1
        for k in ks:
            if expected & set(ranked[:k]):
                hits[k] += 1
                bucket[k] += 1

    total = len(cases)
    print("  overall: " + "  ".join(f"precision@{k}={hits[k] / total:.3f}" for k in ks))
    for domain in sorted(per_domain):
        bucket = per_domain[domain]
        scores = "  ".join(f"p@{k}={bucket[k] / bucket['n']:.3f}" for k in ks)
        print(f"  {domain} (n={bucket['n']}): {scores}")
    print("=" * 78)
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--index", type=int, default=None)
    ap.add_argument("--evaluate", nargs="?", const="holdout.json", default=None,
                    metavar="FILE",
                    help="score precision@1/3/5 over a labelled fingerprint set "
                         "(default: v3/holdout.json)")
    args = ap.parse_args()

    model = load_model()
    if args.validate:
        validate(model)
    if args.evaluate is not None:
        return evaluate(args.evaluate, model)

    fps = load("fingerprints.examples.json")["items"]
    if args.index is not None:
        run_case(fps[args.index], model, args.index)
    else:
        for i, fp in enumerate(fps):
            run_case(fp, model, i)
    print("=" * 78)


if __name__ == "__main__":
    sys.exit(main())
