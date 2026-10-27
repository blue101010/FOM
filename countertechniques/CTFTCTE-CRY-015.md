# CTFTCTE-CRY-015 — Recover the factors from a bounded exponent relation

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-015`](../techniques/CTFTTE-CRY-015.md) — RSA exponent bound by a small linear relation

---

## Offensive Recovery (CTF practitioner / solver)

Given `N`, `e` (and `c`), recover `φ(N)` — or the factors — from `e·x + y ≡ 0 (mod φ)` with
small `x`, `y`. Two branches, cheapest first.

**Branch A — the small parameters are published (`er`, `r` given).**
Evaluate the relation directly; it is a multiple of the totient, and a multiple of `φ` is enough:

```
k_phi = e * (1 + er * r) - er        # == k * φ(N)
d     = inverse(e, k_phi)            # valid mod k*φ, hence mod φ
m     = pow(c, d, N)
```

Validate with `pow(m, e, N) == c`, never with the flag format alone.

**Branch B — only `N`, `e`, `c` are published (generalized Wiener).**
`x` sits at the edge of the convergent denominators of `e/N`, so continued fractions enumerate it:

1. Compute the convergents of `e/N` — and, when they do not close, their semiconvergents
   `(h_{i-1} + j·h_{i-2}) / (k_{i-1} + j·k_{i-2})`, because `x` sits between two convergents as
   soon as it nears the `N^{1/4}` edge of the window.
2. For each candidate `k/x`, `s = N + 1 − ⌊e·x / k⌋` estimates `p + q`; `t = s² − 4N` estimates
   `(p − q)²`.
3. If `t` is a perfect square (search a ±2 window around `s` to absorb the flooring error), then
   `p = (s + t^{1/2})/2` and `N mod p == 0` closes the branch.
4. Otherwise `p̃ = (s + ⌊t^{1/2}⌋)/2` is within `N^{1/4}` of the true prime: Coppersmith
   `f(X) = p̃ + X` with `X = N^{1/4}`, plus the small shifts `(2j+1)·N^{1/4}` that recentre the
   unknown, and keep any root that divides `N`.
5. `d = e⁻¹ mod φ`, decrypt, re-encrypt to confirm.

Expected cost: milliseconds for branch A, under a second for branch B on replay instances.
Measured by replaying the construction at 256 and 512 bits (`scripts/yklm_selftest.py`):
convergents plus semiconvergents close **~92%** of instances directly (23/25 and 39/40 in the
larger sweep). The residual failures are exactly the instances where `x > N^{1/4}/3`, i.e. where
the theorem's own hypothesis fails — past that edge neither the fraction sweep nor the
`p̃ + X` route is guaranteed, and the next move is a bivariate lattice on the relation itself.
Do not read the fallback as dead code.

**What fails and must not be retried.** Wiener (`d` is full size), Boneh-Durfee (`d > N^{0.292}`),
Fermat (primes are independent and balanced), Pollard `p−1`, and every automated sweep that only
looks at `d`. Recognising that the weakness is in `(x, y)`, not in `d`, is the whole solve.

## Forensic / Blue-Team Perspective (DFIR analyst)

The scheme is sold as a CRT fault-attack countermeasure, so its presence in a codebase means
someone traded a side-channel risk for a *structural* key-recovery risk. Audit rule: a private
exponent must be drawn from a uniform distribution over the valid range, never assembled as
`inverse(small) + small`. A published `er`/`r` pair for "verifiability" is a disclosure of `kφ(N)`.
In DFIR terms, key material that factors from public parameters alone leaves no cryptographic
protection at all, so a TLS/SSH endpoint running such a generator has to be treated as
plaintext-equivalent during incident scoping.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573 | Encrypted Channel | Recovery factors a weakly generated exponent pair; ATT&CK has no cryptanalytic equivalent. |

## Tools

- [generalized_wiener_recover.py](../tools/CTFTTOU-414.md) ([CTFTTOU-414](../tools/CTFTTOU-414.md)) — convergent sweep, square test, Coppersmith hand-off, decryption
- [SageMath](../tools/CTFTTOU-190.md) ([CTFTTOU-190](../tools/CTFTTOU-190.md)) — `small_roots` for step 4
- [sympy](../tools/CTFTTOU-198.md) ([CTFTTOU-198](../tools/CTFTTOU-198.md)) — `continued_fraction_convergents`, `isqrt`

## References

- <https://iacr.org/archive/pkc2004/29470001/29470001.pdf> (Nitaj, PKC 2004 — Theorem 2, the bound that makes branch B work)
- <https://link.springer.com/chapter/10.1007/3-540-45861-1_30> (YKLM scheme definition and its fault-attack rationale)
- <https://hackmd.io/@msalaani/hackfest7-crypto> (Hackfest 7 Finals 2023 — branch A solve in four lines, branch B solve with the lattice fallback)
