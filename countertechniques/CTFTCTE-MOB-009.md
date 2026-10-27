# CTFTCTE-MOB-009 — Recover application logic from engine bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-009`](../techniques/CTFTTE-MOB-009.md) — Engine bytecode packaged with a mobile application

---

## Offensive Recovery (CTF practitioner / solver)

Recover the application's observable behaviour from the engine bytecode the package ships.

1. **Confirm the container.** List the package. A generated platform shell plus a large asset plus
   an engine runtime library, and nothing of substance in the platform decompilation, is the
   signature — stop reading the shell.
2. **Locate the asset by convention.** Packaged assets directory on Android, application bundle on
   iOS. Framework naming conventions narrow it to one or two files; brute-forcing names is wasted
   effort.
3. **Identify engine and bytecode version** from the header. The version pins the decompiler: a
   decompiler built for another version emits plausible-looking nonsense, which is worse than an
   error, so check the version against the tool's supported range first.
4. **Decompile, then read the restored module graph.** Prefer the artifacts the compiler retained —
   module boundaries and original function names — over raw disassembly; they turn a flat listing
   into a call graph.
5. **Rebuild the behaviour, not just the strings.** Base URL(s), endpoint paths, HTTP verbs, headers,
   serialized payload shapes, and any value the app persists locally. Then decide what the challenge
   actually asks for: a value stored by the app is not automatically the answer, and a second
   endpoint often belongs to the next part of a multi-part challenge.
6. **Confirm each hypothesis with a single request.** The bundle tells you *which* calls exist; it
   rarely tells you what the server returns.

| Observation | Reading |
|---|---|
| platform decompilation is only framework classes | logic is elsewhere: look for the engine asset |
| asset starts with a known bytecode magic | engine confirmed; read the version field next |
| decompiler output is syntactically odd but parses | wrong bytecode version, not a hostile target |
| strings reveal endpoints but no structure | decompile; string extraction is a shortcut, not a result |
| the app writes a value to local storage and never reads it back | that value is the challenge artefact, not an internal detail |

## Forensic / Blue-Team Perspective (DFIR analyst)

Shipping engine bytecode is a build-pipeline decision with a review consequence: the bundle is
*code* and belongs in code review, not in the "data/asset" bucket. For analysis, record the asset
hash and the bytecode version alongside the app version — a version bump silently invalidates every
earlier decompiler configuration, and a re-packaged bundle is otherwise indistinguishable. The
absence of obfuscation is itself informative: a bundle that decompiles cleanly to named functions was
built without the framework's production hardening, which is a supply-chain observation worth
reporting.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The recovery defeats compiled-artifact delivery; the bytecode version is the operational gate. |

## Tools

- [hermes-dec](../tools/CTFTTOU-417.md) ([CTFTTOU-417](../tools/CTFTTOU-417.md)) — header parsing, disassembly, decompilation
- container tooling — extraction and platform-shell decoding
- string extraction — engine confirmation and fallback
- a generic HTTP client — to act on the endpoints the bundle revealed

## References

- <https://github.com/P1sec/hermes-dec>
- <https://github.com/facebook/hermes/blob/main/doc/BytecodeFileFormat.md>
- casebook: `2025/HF2025/All_the_things_she_sent/All_the_things_she_sent.md`
