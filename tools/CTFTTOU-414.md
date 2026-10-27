# CTFTTOU-414 — generalized_wiener_recover.py

> **Tool ID:** `CTFTTOU-414`
> **Related techniques/counters:** CTFTTE-CRY-015, CTFTCTE-CRY-015

## Description

Workspace-authored RSA recovery for a public exponent bound by a small linear relation
(`e·x + y ≡ 0 mod φ`, `x ≈ N^{1/4}`): the residue of the Yen-Kim-Lim-Moon `d = dr + r`
construction. Stdlib only, no third-party package.

- **`--file` / `--n --e --c`** — parse a challenge output (labels `N`, `e`, `c`, `er`, `r`,
  hex or decimal, or bare integers) and run the cheapest branch first.
- **Branch A** (`er`, `r` published): `kφ = e(1 + er·r) − er`, then factor `N` from that
  multiple of the totient (fast small-multiple path, then the 2-adic square-root path), then
  `d = e⁻¹ mod φ`.
- **Branch B** (`N`, `e`, `c` only): generalized Wiener (Nitaj, PKC 2004) — convergents of
  `e/N`, then their semiconvergents, square test on `(p − q)²`, and `p̃ = (s + √(s²−4N))/2`
  kept as the Coppersmith input.
- **`--emit-sage`** — writes a standalone `small_roots(X = N^{1/4})` script with the shift family
  for the fallback branch; `--check-relation` proves that a candidate `(x, y)` really yields a
  multiple of `φ` by factoring `N` from it.
- Decryption is always validated by re-encryption, and optionally against `--flag-prefix`.

Related harness: [`yklm_selftest.py`](../../ctf-skills-main/ctf-crypto-bounded-exponent-relation/scripts/yklm_selftest.py)
replays the whole construction at reduced scale (256/512 bits) and asserts the relation, the
multiple-of-φ shortcut, the sweep and the lattice hand-off.

## URL

Local (workspace): [ctf-skills-main/ctf-crypto-bounded-exponent-relation/scripts/generalized_wiener_recover.py](../../ctf-skills-main/ctf-crypto-bounded-exponent-relation/scripts/generalized_wiener_recover.py)

## Usage

```bash
# branch B from a challenge dump
python3 generalized_wiener_recover.py --file chall.txt --flag-prefix 'HACKFEST{'

# branch A when er and r are printed with N, e, c
python3 generalized_wiener_recover.py --file chall.txt --flag-prefix 'HACKFEST{'

# lattice hand-off when no fraction closes
python3 generalized_wiener_recover.py --file chall.txt --emit-sage coppersmith.sage

# prove the relation e*x + y = k*phi(N) for a known (x, y)
python3 generalized_wiener_recover.py --check-relation --n N --e E --x X --y Y

# replay the construction (relation + branch A + branch B + lattice eligibility)
python3 yklm_selftest.py --trials 15 --bits 256
```

## Notes

- Measured on replayed instances: convergents plus semiconvergents close ~92% directly
  (23/25 and 39/40 in the larger sweep); the semiconvergent stage alone lifts 36/40 to 39/40.
- Residual failures are the instances where `x > N^{1/4}/3`, i.e. Nitaj's own hypothesis is
  violated — that edge needs a bivariate lattice on the relation, not `p̃ + X`.
- `RsaCtfTool` does not cover this class: its `wiener` and `boneh_durfee` modules assume a small
  `d`, which the YKLM construction never produces.

## Skills

- [ctf-crypto-bounded-exponent-relation](../skills/CTFTSKL-007.md) — bounded exponent relation (CRY-015)

## Related Techniques

CTFTTE-CRY-015, CTFTCTE-CRY-015
