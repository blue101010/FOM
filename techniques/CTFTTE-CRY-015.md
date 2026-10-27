# CTFTTE-CRY-015 — RSA exponent bound by a small linear relation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Crypto  
> **Paired counter-technique:** [`CTFTCTE-CRY-015`](../countertechniques/CTFTCTE-CRY-015.md) — Recover the factors from a bounded exponent relation

---

## How the challenge author hides

Nothing looks weak: `N = p·q` is a healthy balanced semiprime, `e` is full-size, no prime,
no bit of `d` and no helper value is leaked. What is small is not the private exponent but a
**linear relation the public exponent satisfies**:

$$e\,x + y \equiv 0 \pmod{\varphi(N)}, \qquad x \approx N^{1/4}, \quad |y| \approx N^{1/8}$$

Every textbook test fails. `d` is full size, so Wiener (`d < N^{1/4}/3`) and Boneh-Durfee
(`d < N^{0.292}`) return nothing, Fermat/Pollard never apply, and `RsaCtfTool` reports
"no attack succeeded" because none of its modules test a bounded `(x, y)` relation. The trap is
that the weakness lives in the *shape of the exponent pair*, invisible to a scanner looking at
`d` alone.

The canonical generator is the Yen-Kim-Lim-Moon exponentiation scheme, published as a
countermeasure to CRT fault attacks. With `φ = φ(N)` and a quarter-size bound `B = 2^{nbits/4}`:

```
er, r ← [1, B]                      # two small secrets
dr    = er⁻¹ mod φ
d     = dr + r                      # full-size "perturbed" private exponent
e     = d⁻¹ mod φ                   # full-size public exponent
```

`d` is `dr` plus a 256-bit noise, so it never enters a small-`d` window. Multiplying
`e·(dr + r) ≡ 1` by `er` collapses the construction into the relation above:

$$e\,\underbrace{(1 + e_r r)}_{x \approx N^{1/4}} \;\underbrace{- e_r}_{y \approx N^{1/8}} \equiv 0 \pmod{\varphi(N)}$$

Two publication variants:

- **Parameters published.** `er` and `r` are printed next to `N`, `e`, `c`. The relation is then
  immediately evaluable: `kφ(N) = e(1 + er·r) − er` is a multiple of the totient, and
  `d ≡ e⁻¹ (mod kφ(N))` decrypts — a multiple of `φ` is as good as `φ` itself.
- **Parameters withheld.** Only `N`, `e`, `c` are given. The bounded relation is the sole
  residue of the construction, and it is exactly the input of the generalized Wiener attack
  (Nitaj, PKC 2004), whose Theorem 2 asks for `x ≤ ⅓N^{1/4}` and `|y| ≤ ½cN^{−3/4}ex` with
  `c ≤ 1` — satisfied here because `er, r = O(N^{1/8})`.

The same smell appears whenever an author "adds noise" to a modular inverse instead of drawing
`d` fresh, or reuses one small multiplier across several keys: any leak of `x` (or of a multiple
of `φ`, see `CTFTCTE-CRY-001`) plus a small `y` reopens this relation.

## Indicators

- `e` is large (close to `N`, more than 1024 bits) yet neither Wiener nor Boneh-Durfee returns.
- The generator advertises a "fault-resistant", "CRT-hardened" or "noise-protected" exponent.
- `N` is unique and balanced: no shared modulus, no close primes, so the failure of the standard
  sweep is itself the signal.
- Several `(N, e)` pairs share a small multiplicative structure — `x` repeats or is close.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1573 | Encrypted Channel | Weakly generated RSA exponent pairs; ATT&CK models the channel, not the key-recovery cryptanalysis. |

## Tools

- [generalized_wiener_recover.py](../tools/CTFTTOU-414.md) ([CTFTTOU-414](../tools/CTFTTOU-414.md)) — continued fractions + Coppersmith fallback + decryption
- [SageMath](../tools/CTFTTOU-190.md) ([CTFTTOU-190](../tools/CTFTTOU-190.md)) — `small_roots` for the fallback branch
- [sympy](../tools/CTFTTOU-198.md) ([CTFTTOU-198](../tools/CTFTTOU-198.md)) — continued fractions, isqrt
- [RsaCtfTool](../tools/CTFTTOU-191.md) ([CTFTTOU-191](../tools/CTFTTOU-191.md)) — sweep that fails here; use it to prove the absence of the standard classes, not to solve

## References

- <https://iacr.org/archive/pkc2004/29470001/29470001.pdf> (Nitaj, *A Generalized Wiener Attack on RSA*, PKC 2004 — Theorem 2)
- <https://link.springer.com/chapter/10.1007/3-540-45861-1_30> (Yen, Kim, Lim, Moon, *RSA Speedup With Chinese Remainder Theorem Immune Against Hardware Fault Cryptanalysis*, 2003)
- <https://d-nb.info/972386416/34> (*New RSA Vulnerabilities Using Lattice Reduction Methods*)
- <https://hackmd.io/@msalaani/hackfest7-crypto>
