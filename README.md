# FOM

**Forensic Obfuscation Model (FOM) by BlueOneZero (blue101010) Corporation.**

A specialized model, akin to the MITRE ATT&CK framework, that focuses on forensics and steganography. This concept diverges from MITRE ATT&CK, as MITRE ATt&CK does not extensively incorporate forensic procedures with technical details. The model introduces a framework of TTPs (Tactics, Techniques, and Procedures) along with mitigations, procedures, and **Counter-Techniques (CTEs)**.

**A counter technique (FOMCTE) is implementing a mitigation, restoration to "default" of a technique (TE).**
!! **The counter techniques are the main focus of this model [countertechniques.md](https://github.com/blue101010/FOM/blob/main/countertechniques/countertechniques.md)**!!

![Alt text](fom.png)

```
#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+
#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+
#FF+#FF+#FF+#FF+#FF+
```

The tool and model primarily focus on retrieving data from files that were 'obfuscated' using forensic tools, steganography, or other techniques. At contrary to the MITRE ATT&CK framework, the counter-techniques (CTs) in this model may be more detailed.

## Tactic

A [Tactic](https://github.com/blue101010/FOM/tactics) (FOMTA) is used to hide something mainly through forensics, steganography, "security by obscurity" and less with cryptography.
Example : [FOMAT001](https://github.com/blue101010/FOM/tactics/FOMTA001.md): Binary hexadecimal format modifications.

## Technique and sub-technique

A technique (FOMTE) is implementing a A [Tactic](https://github.com/blue101010/FOM/tactics) (**FOMTA**) of obfuscation.

## Enterprise FOM

This repository contains the Forensic Obfuscation Model (**FOM**).

## Counter-techniques - techniques and tactics

- [Counter-techniques](https://github.com/blue101010/FOM/blob/main/countertechniques/countertechniques.md) : The list of counter-techniques

## Contents Details

- [enterprise-fom.json](https://github.com/blue101010/FOM/blob/main/enterprise-fom.json): The main JSON file containing the FOM techniques and countertechniques.
- [index.json](https://github.com/blue101010/FOM/blob/main/index.json): The collection index JSON file listing the contents of this repository in a machine-readable format.

