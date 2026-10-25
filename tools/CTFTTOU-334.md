# CTFTTOU-334 — Rizin and Cutter

> **Tool ID:** `CTFTTOU-334`  
> **Related techniques/counters:** CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-002, CTFTCTE-REV-002, CTFTTE-REV-003, CTFTCTE-REV-003, CTFTTE-REV-004, CTFTCTE-REV-004, CTFTTE-REV-005, CTFTCTE-REV-005, CTFTTE-REV-008, CTFTCTE-REV-008, CTFTTE-REV-009, CTFTCTE-REV-009, CTFTTE-REV-010, CTFTCTE-REV-010

## Description

Rizin is a fork of radare2, providing a complete framework for binary analysis, disassembly, and reverse engineering. Cutter is the official GUI for Rizin (and radare2), offering a user-friendly Qt-based interface. Together, they provide powerful static and dynamic analysis capabilities for CTF binary challenges.

Rizin features:
- Multi-architecture support (x86, ARM, MIPS, RISC-V, and more)
- Disassembler and decompiler
- Scriptable with Python, JavaScript, and Rizin's own language
- Binary patching and modification
- Analysis of binaries, firmware, and memory dumps
- Integration with external tools

Cutter features:
- Modern Qt-based GUI
- Visual graph representation of functions and cross-references
- Collaborative reverse engineering
- Python scripting support
- Customizable interface

## URL

- **Rizin**: <https://rizin.re/>
- **Cutter**: <https://github.com/rizinorg/cutter>
- **GitHub (Rizin)**: <https://github.com/rizinorg/rizin>
- **GitHub (Cutter)**: <https://github.com/rizinorg/cutter>

## Installation

**Debian/Ubuntu/Kali:**
```bash
# Install Rizin
sudo apt update && sudo apt install -y rizin

# Install Cutter (GUI)
sudo apt install -y cutter

# Verify installation
rizin --version
cutter --version
```

**From source:**
```bash
# Build Rizin
git clone https://github.com/rizinorg/rizin.git
cd rizin
meson setup build
cd build
meson compile
sudo meson install

# Build Cutter
git clone https://github.com/rizinorg/cutter.git
cd cutter
# Follow build instructions in README.md
```

**Docker:**
```bash
# Use pre-built Docker images
docker pull rizinorg/rizin
docker pull rizinorg/cutter
```

## Usage

**Rizin (CLI):**
```bash
# Basic analysis
rizin -AAA binary.elf

# Analyze and list functions
rizin -AA binary.elf | grep -E "[0-9]+ [a-f0-9]+.*sym\.|

# Disassemble main function
rizin -AA -q -c 's main; pdf' binary.elf

# Search for strings
rizin -AA -q -c 'is' binary.elf

# Search for flag references
rizin -AA -q -c '/is flag/i' binary.elf

# Patch binary (change bytes at offset)
rizin -w -c 'wx 90 90 @ 0x123456' binary.elf
```

**Cutter (GUI):**
```bash
# Open binary
cutter binary.elf

# Use GUI to:
# - View strings
# - Analyze functions
# - View call graphs
# - Decompile functions
# - Set breakpoints (with debugging plugin)
# - Export to Python script
```

**Common Rizin Commands:**
```
# Analyze binary
-aa        # Full analysis
-aaa       # Full analysis with extra checks
-aaa       # Full analysis recursively

# Navigation
-s sym.main         # Seek to main symbol
-s 0x123456        # Seek to address

# Disassembly
-pD                # Disassemble current function (pseudo-C)
-pdd               # Disassemble with more details
-pdf               # Disassemble current function

# Functions
-afl               # List all functions
-fl               # List function names

# Strings
-is                # Search for strings
-iss               # Search for strings with more info

# Cross-references
-axt main          # Show cross-references to main
-axt @ 0x123456   # Show cross-references to address

# Search
-/ text            # Search for text
-/x 90 90 90      # Search for bytes

# Memory
-dx 16 @ esp      # Hexdump 16 bytes at stack pointer
-px 16 @ 0x123456 # Hexdump 16 bytes at address

# Registers
-dr              # Show registers

# Patching
-wx 90 90 @ 0x123456  # Write bytes (NOPs)
-wa hex @ address  # Write hex data

# Quit
-q                # Quit
```

## Python Scripting

Rizin and Cutter support Python scripting for automation:

```python
# rizin-python example
import rizin

# Open binary
r = rizin.Rizin("binary.elf")

# Analyze
r.analyze()

# Get functions
for func in r.functions:
    print(f"Function: {func.name} at {hex(func.addr)}")

# Search for flag
for string in r.strings:
    if "flag" in string.lower():
        print(f"Found: {string} at {hex(string.addr)}")

# Write script to file
with open("script.rz", "w") as f:
    f.write('aa\n')
    f.write('afl\n')
    f.write('q\n')

# Run script
rizin -q -i script.rz binary.elf
```

## Integration

**With Ghidra:**
- Export Rizin analysis to Ghidra-compatible formats
- Use complementary analysis capabilities

**With GDB:**
```bash
# Debug with GDB integration
rizin -d -r gdb:///path/to/binary binary.elf
```

**With Frida:**
- Use Rizin to find interesting addresses, then hook with Frida
- Combine static and dynamic analysis

## CTF-Specific Workflows

### 1. Extract Strings for Flag
```bash
rizin -AA -q -c '/is flag/i' binary.elf
rizin -AA -q -c 'is ~flag' binary.elf
```

### 2. Find Main Function
```bash
rizin -AA -q -c 's main; pdf' binary.elf
```

### 3. Analyze Check Function
```bash
rizin -AA -q -c 's check; pdf' binary.elf
rizin -AA -q -c 'axt @ sym.check' binary.elf
```

### 4. Patch Binary
```bash
# Find the comparison
rizin -AA -q -c '/x cmp' binary.elf

# Patch to always jump (NOPs)
rizin -w -q -c 'wx 90 90 @ 0x123456' binary.elf
```

### 5. Extract Hidden Data
```bash
# Dump data at specific address
rizin -AA -q -c 'px 32 @ 0x123456' binary.elf
```

## Comparison with Similar Tools

| Feature | Rizin | Ghidra | IDA | Binary Ninja |
|---------|-------|--------|-----|-------------|
| Multi-architecture | ✅ | ✅ | ✅ | ✅ |
| Decompiler | ✅ | ✅ | ✅ | ✅ |
| Scripting | ✅ (Python, JS) | ✅ (Python, Java) | ✅ (Python, IDC) | ✅ (Python) |
| GUI | ❌ (Cutter available) | ✅ | ✅ | ✅ |
| Open Source | ✅ | ✅ | ❌ | ❌ |
| Headless | ✅ | ✅ | ❌ | ❌ |
| Collaboration | ❌ | ✅ | ❌ | ✅ |

## Tips for CTFs

1. **Start with full analysis**: `rizin -AAA binary` for comprehensive auto-analysis
2. **Use Cutter for visualization**: Graph view helps understand control flow
3. **Search for flag patterns**: `/is flag` or `/is FLG` often finds the flag
4. **Check XREFs**: `axt @ function` shows who calls a function
5. **Look at strings**: `is` lists all strings - often contains the flag or hints
6. **Patch carefully**: Use `-w` flag to enable write mode before patching
7. **Script repetitive tasks**: Use Python to automate analysis across multiple files

## Related Techniques

CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-002, CTFTCTE-REV-002, CTFTTE-REV-003, CTFTCTE-REV-003, CTFTTE-REV-004, CTFTCTE-REV-004, CTFTTE-REV-005, CTFTCTE-REV-005, CTFTTE-REV-008, CTFTCTE-REV-008, CTFTTE-REV-009, CTFTCTE-REV-009, CTFTTE-REV-010, CTFTCTE-REV-010

## References

- [Rizin Official Site](https://rizin.re/)
- [Rizin GitHub](https://github.com/rizinorg/rizin)
- [Cutter GitHub](https://github.com/rizinorg/cutter)
- [Rizin Book](https://rizin.re/docs/book/)
- [Rizin Tutorials](https://rizin.re/tutorials/)
- [Cutter Documentation](https://cutter.re/docs/)
- [radare2 book (still mostly applicable)](https://radare.gitbooks.io/radare2book/)
