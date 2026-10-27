# CTFTTOU-437 — o365spray and MSOLSpray

> **Tool ID:** `CTFTTOU-437`  
> **Related techniques/counters:** CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## Description

Identity-platform reconnaissance and credential validation tools. Their role in a challenge is the step
*before* everything else: deciding which of a list of candidate accounts exist in the tenant, whether the
tenant federates to another identity provider, and whether a supplied password is the one that works.

- **o365spray** — domain and user enumeration plus a throttled password-spray mode, and enumeration of the
  tenant's authentication configuration (managed versus federated, which determines where a login is
  actually validated).
- **MSOLSpray** — the smaller, older counterpart for the same validation step; useful when only the spray
  primitive is needed.

Both are deliberate about rate limiting for a reason: this is the one Azure surface where a careless loop
locks the account the challenge depends on. Use `--enum`/validate-one modes, never a blind loop against a
live tenant.

## URL

- <https://github.com/0xZDH/o365spray>
- <https://github.com/dafthack/MSOLSpray>

## Installation

```bash
git clone --depth 1 https://github.com/0xZDH/o365spray.git ~/TOOLS/o365spray
python3 -m venv ~/.venvs/ctfazure && source ~/.venvs/ctfazure/bin/activate
pip install -r ~/TOOLS/o365spray/requirements.txt
python ~/TOOLS/o365spray/o365spray.py --help
```

## Usage

```bash
source ~/.venvs/ctfazure/bin/activate
python ~/TOOLS/o365spray/o365spray.py --validate --domain tenant.tld
python ~/TOOLS/o365spray/o365spray.py --enum --domain tenant.tld --userlist candidates.txt
python ~/TOOLS/o365spray/o365spray.py --spray --domain tenant.tld --userlist users.txt --password 'Candidate1'
```

Pitfalls: a "valid" answer can mean the tenant answered differently for existing and non-existing accounts,
not that the password is right — read which check produced the verdict. Federation detected here redirects
the credential question to another provider, which is a different pair. Smart-lockout policies make a
second attempt expensive: prefer the enumeration phase, which does not consume attempts.

## Related Techniques

CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-CLD-009, CTFTCTE-CLD-009

## References

- [o365spray repository](https://github.com/0xZDH/o365spray)
- [MSOLSpray repository](https://github.com/dafthack/MSOLSpray)
- [Microsoft Entra smart lockout](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-password-smart-lockout)
