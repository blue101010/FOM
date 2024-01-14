# FOM
**Forensic Obfuscation Model (FOM) by BlueOneZero (blue101010) Corporation.**

![Alt text](fom.png)

```
#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+
#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+#FF+
#FF+#FF+#FF+#FF+#FF+
```

# Usage
A specialized model, akin to the MITRE ATT&CK framework, focuses on forensics and steganography. This concept diverges from MITRE ATT&CK, as it does not extensively incorporate kill chain phases in the steps for forensically concealing content within files. The model introduces a framework of TTPs (Tactics, Techniques, and Procedures) along with mitigations, procedures, and Counter-Techniques (CTEs).

The tool and model primarily focus on retrieving data from files that were 'obfuscated' using forensic tools, steganography, or other techniques. Contrary to the MITRE ATT&CK framework, the counter-techniques (CTs) in this model may be more detailed.



# Tactic
A tactic (FOMTA) is used to hide something mainly through forensics, steganography, "security by obscurity" and less with cryptography.

Example : FOMTA001: Binary hexadecimal format modifications.


# Technique and sub-technique
A technique (FOMTE) is implementing a tactic (FOMTA) of obfuscation.

Example : FOMTE001: Modify binary image header hexadecicimal signature or "magic number". Ref https://www.garykessler.net/library/file_sigs.html

# Counter technique and counter sub-technique
A countertechnique (FOMCTE) is implementing a mitigation, restoration to "default" of a technique (TE).
!! These counter techniques are the main focus of this model !!


# Enterprise FOM

This repository contains the Forensic Obfuscation Model (FOM) for enterprise.

## Contents

- [enterprise-fom.json](<url to enterprise-fom.json>): The main JSON file containing the FOM techniques and countertechniques.
- [index.json](<url to index.json>): The collection index JSON file listing the contents of this repository in a machine-readable format.