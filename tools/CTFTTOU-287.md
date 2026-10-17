# CTFTTOU-287 — js-beautify

> **Tool ID:** `CTFTTOU-287`  
> **Related techniques/counters:** CTFTTE-FOR-034, CTFTCTE-FOR-034

## Description

Reformats minified, packed or one-line JavaScript into readable, indented source so the
control flow and string literals of an obfuscated client-side payload become legible.
Pairs with an unpacker ([de4js](CTFTTOU-263.md)) for `eval`/`p,a,c,k,e,d` layers and with
[CyberChef](CTFTTOU-048.md) for the base/hex/URL decodes that typically wrap the final
exfiltration or redirect target. Available as the `js-beautify` CLI and as the
beautifier.io web front end.

## URL

<https://github.com/beautifier/js-beautify>

## Related Techniques

CTFTTE-FOR-034, CTFTCTE-FOR-034
