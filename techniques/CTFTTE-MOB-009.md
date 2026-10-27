# CTFTTE-MOB-009 — Engine bytecode packaged with a mobile application

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-009`](../countertechniques/CTFTCTE-MOB-009.md) — Recover application logic from engine bytecode

---

## How the challenge author hides

The target ships as a mobile application package in which **no file holds the logic in the form the
platform tooling reads**. The decompiled Java/Kotlin layer is a generated shell, the native libraries
are the framework's own runtimes, and the application code lives in an asset compiled for the
**embedded script engine**. Nothing is obfuscated: the code is written in a language the platform
decompiler does not target, inside a container that makes it look like ordinary mobile code.

The concealment is a *delivery* decision, not a crypto or packing trick, so the failure mode is
tooling-shaped: the standard decompiler opens the package, shows a few dozen generated classes, and
concludes there is nothing to analyse.

What turns it into a technique — and distinguishes it from the sibling bytecode pairs — is the
triage the solver has to perform before any code is readable:

1. **locate the asset by container convention** (the packaged assets directory on Android, the
   application bundle inside the iOS payload), not by name guessing;
2. **identify the engine and its bytecode version** from the asset header, because engine
   decompilers are version-locked and a mismatched version silently produces garbage;
3. **recover structure** — the function graph and the source-position/name annotations the compiler
   retained — then read the observable behaviour out of it.

The same shape reproduces with any engine a cross-platform framework embeds: only the magic, the
version table and the decompiler change. That is why the class is stated in terms of the *engine*,
not of one framework.

Boundary: logic hidden in a **native library** is the same move with a different substrate and belongs
to [`CTFTTE-MOB-002`](CTFTTE-MOB-002.md); an author-designed instruction set is
[`CTFTTE-REV-004`](CTFTTE-REV-004.md); an artifact compiled for the *same* language as the source is
[`CTFTTE-REV-007`](CTFTTE-REV-007.md); JVM artifacts are [`CTFTTE-REV-006`](CTFTTE-REV-006.md). And
once the logic is readable, the endpoints it reveals are ordinary network/web artefacts — the
technique ends where that domain begins.

## Indicators

- the package contains a multi-megabyte asset named by framework convention, sitting next to a
  matching engine runtime library;
- platform decompilation yields only a bootstrap shell — the "no logic here" verdict is the signal,
  not a dead end;
- the asset starts with a bytecode magic and carries a version field;
- an app manifest asset names a cross-platform framework, which implies a script-engine bundle in
  production builds;
- a fraction of the engine's built-in strings (UI library names, error messages) leak into naive
  string extraction, which confirms the engine before any decompilation.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Compiled-artifact delivery hides the logic; ATT&CK does not model the engine/version triage that the recovery depends on. |

## Tools

- [hermes-dec](../tools/CTFTTOU-417.md) ([CTFTTOU-417](../tools/CTFTTOU-417.md)) — bytecode file parser, disassembler and decompiler for one engine family
- container tooling — list and extract the package, decode the platform shell
- string extraction on the asset — preliminary engine confirmation, and the fallback when no
  decompiler is installed for that version
- the engine's bytecode-format documentation, for the version table

## References

- <https://github.com/facebook/hermes/blob/main/doc/BytecodeFileFormat.md>
- <https://github.com/P1sec/hermes-dec>
- casebook: `2025/HF2025/All_the_things_she_sent/All_the_things_she_sent.md` (offline replay; the
  requests were reconstructed from the bundle, the flag was not validated)
