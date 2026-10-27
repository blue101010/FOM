# CTFTSKL-007 — ctf-crypto-bounded-exponent-relation

> **Skill ID:** `CTFTSKL-007`  
> **Kind:** Fine-grained skill (one FOM pair)  
> **Related techniques/counters:** CTFTTE-CRY-015, CTFTCTE-CRY-015

## Description

Solves RSA challenges whose public exponent is bound by a small linear relation instead of being
weak in itself: `e·x + y ≡ 0 mod φ(N)` with `x ≈ N^{1/4}`, `y ≈ N^{1/8}`. Covers the
Yen-Kim-Lim-Moon `d = dr + r` construction (a published CRT-fault countermeasure), both
publication variants — helper values `er`, `r` printed (multiple of `φ`, four lines of
arithmetic) and helper values withheld (generalized Wiener / Nitaj PKC 2004) — plus the
semiconvergent sweep, the `p̃ + X` Coppersmith hand-off when the fraction sweep fails, and the
`x > N^{1/4}/3` edge where the theorem itself stops applying.

The tell is negative: `e` and `d` are both full size, `N` is balanced with nothing leaked, and
the whole standard sweep (Wiener, Boneh-Durfee, Fermat, Pollard, RsaCtfTool) returns nothing.

## Skill file

- [ctf-skills-main/ctf-crypto-bounded-exponent-relation/SKILL.md](../../ctf-skills-main/ctf-crypto-bounded-exponent-relation/SKILL.md) — canonical

## When to load

```yaml
artifact_type: key-material | ciphertext
evidence:
  - e is full size (comparable to N), yet Wiener and Boneh-Durfee both return nothing
  - d is full size: no small-private-exponent window is plausible
  - N is balanced: no shared modulus, no close primes, no partial leak
  - generator mentions a CRT-fault countermeasure, a "perturbed"/"noised" private exponent, or prints er, r
  - e*(1 + er*r) - er is divisible by phi(N) when er and r are published
```

## FOM pairs

- [CTFTTE-CRY-015](../techniques/CTFTTE-CRY-015.md) / [CTFTCTE-CRY-015](../countertechniques/CTFTCTE-CRY-015.md) — RSA exponent bound by a small linear relation / recover the factors from a bounded exponent relation

## Tools

- [generalized_wiener_recover.py](../tools/CTFTTOU-414.md) — attack CLI, relation proof, SageMath hand-off
- [SageMath](../tools/CTFTTOU-190.md) — `small_roots(X = N^{1/4})` for the Coppersmith fallback
- [sympy](../tools/CTFTTOU-198.md) — continued fractions if you drive the sweep yourself
- [RsaCtfTool](../tools/CTFTTOU-191.md) — run once to confirm the standard classes are absent

## Related skills

- [ctf-crypto-weak-rsa](../../ctf-skills-main/ctf-crypto-weak-rsa/SKILL.md) — the coarse weak-parameter bucket (CRY-001); use it when `d` really is small
- [ctf-crypto-predictable-prng](../../ctf-skills-main/ctf-crypto-predictable-prng/SKILL.md) — when the exponent comes from a recoverable generator

## Notes

Validated by `scripts/yklm_selftest.py` (stdlib only): relation 100% (15/15, 25/25, 10/10 at
256/512 bits), branch A decrypt 100%, branch B direct ~92% with semiconvergents, residual cases
beyond the `N^{1/4}/3` edge. Source event: Hackfest 7 Finals 2023 — "ALO" (branch A, 2 solves)
and "ALO REVENGE" (branch B, 0 solves). One event, so `CTFTTE-CRY-015` stays `taxonomy_only`
until a second independent event is curated.

## Related Techniques

CTFTTE-CRY-015, CTFTCTE-CRY-015
