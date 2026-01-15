# Quick Reference Guide - Python Built-ins Inspector

## Installation

```bash
# Clone or download builtins_inspector.py
# No dependencies required - uses only Python standard library
python --version  # Requires Python 3.6+
```

## Command Cheat Sheet

| Command | Description | Output Length |
|---------|-------------|---------------|
| `--summary` | Show category counts | Short (10 lines) |
| `--inspect <name>` | Deep dive into one built-in | Medium (20-40 lines) |
| `--category "<category>"` | List all in category | Medium (10-50 lines) |
| `--all` | Full inspection of everything | Very Long (5000+ lines) |
| `--help` | Show help message | Short |

## Quick Examples

```bash
# 1. Get overview
python builtins_inspector.py --summary

# 2. Understand dict
python builtins_inspector.py --inspect dict

# 3. Understand len
python builtins_inspector.py --inspect len

# 4. See all functions
python builtins_inspector.py --category "Built-in Function"

# 5. See all exceptions
python builtins_inspector.py --category "Exception Class"

# 6. Full dump (careful!)
python builtins_inspector.py --all > full_inspection.txt
```

## Category Names (Case Sensitive)

- `"Built-in Function"`
- `"Built-in Class"`
- `"Exception Class"`
- `"Constant"`
- `"Other"`

## Common Use Cases

### Learn How X Works
```bash
python builtins_inspector.py --inspect X
```
Replace X with: `dict`, `list`, `str`, `int`, `len`, `print`, `iter`, `next`, etc.

### Find Related Built-ins
```bash
# All functions
python builtins_inspector.py --category "Built-in Function"

# All exceptions
python builtins_inspector.py --category "Exception Class"
```

### Understand Magic Methods
```bash
# Functions that trigger magic methods
python builtins_inspector.py --inspect len    # Triggers __len__
python builtins_inspector.py --inspect str    # Triggers __str__
python builtins_inspector.py --inspect iter   # Triggers __iter__

# Classes that implement protocols
python builtins_inspector.py --inspect dict   # See __getitem__, __setitem__, etc.
python builtins_inspector.py --inspect list   # See __add__, __mul__, etc.
```

## Output Format Guide

### For Functions:
```
Function: <name>
Type: builtin_function_or_method
Module: builtins
Implementation: C (CPython interpreter)
[Triggers Magic Method: __xxx__ (if applicable)]
Documentation: <first line of docstring>
```

### For Classes:
```
Class: <name>
Type: type
Module: builtins
Inheritance Chain (MRO): <class hierarchy>
Public Methods: <list>
Special Methods: <list of __dunder__ methods>
Documentation: <first line of docstring>
```

### For Constants:
```
Constant: <name>
Value: <repr>
Type: <type name>
Documentation: <explanation>
```

## Pro Tips

### 1. Pipe to Less for Long Output
```bash
python builtins_inspector.py --all | less
```

### 2. Search Within Output
```bash
python builtins_inspector.py --all | grep -i "iterator"
```

### 3. Save to File
```bash
python builtins_inspector.py --inspect dict > dict_analysis.txt
```

### 4. Compare Multiple Built-ins
```bash
python builtins_inspector.py --inspect list > list.txt
python builtins_inspector.py --inspect tuple > tuple.txt
diff list.txt tuple.txt
```

### 5. Count Methods
```bash
python builtins_inspector.py --inspect dict | grep -c "Special Methods"
```

## Understanding the Output

### Inheritance Chain (MRO)
```
├─ dict
├─ object
└─ (end)
```
- Top-down: most specific to most general
- Method lookup follows this order
- All classes end with `object`

### Method Categories

**Public Methods**: User-facing API
```python
my_dict.get('key')      # ✓ Public method
my_dict.update({...})   # ✓ Public method
```

**Special Methods**: Protocol implementation
```python
len(my_dict)            # Calls my_dict.__len__()
my_dict['key']          # Calls my_dict.__getitem__('key')
'key' in my_dict        # Calls my_dict.__contains__('key')
```

### Type Information

| Type | Meaning | Example |
|------|---------|---------|
| `type` | A class (creates objects) | `dict`, `list`, `int` |
| `builtin_function_or_method` | A function | `print`, `len`, `isinstance` |
| `bool` | Boolean constant | `True`, `False` |
| `NoneType` | Null value | `None` |
| `ellipsis` | Ellipsis constant | `Ellipsis` or `...` |

## Troubleshooting

### "Unknown category"
```bash
# Wrong (spaces matter)
python builtins_inspector.py --category "built-in function"  # ✗

# Correct
python builtins_inspector.py --category "Built-in Function"  # ✓
```

### "Could not inspect"
```bash
# Name doesn't exist
python builtins_inspector.py --inspect Dict  # ✗ (case sensitive)
python builtins_inspector.py --inspect dict  # ✓
```

### Output Too Long
```bash
# Use less for scrolling
python builtins_inspector.py --all | less

# Or save to file
python builtins_inspector.py --all > output.txt
```

## Python API (Programmatic Use)

```python
from builtins_inspector import BuiltinsInspector, OutputFormatter

# Create inspector
inspector = BuiltinsInspector()
inspector.inspect_all()

# Get summary
summary = inspector.get_summary()
print(summary)

# Inspect specific item
result = inspector.inspect_single('dict')
print(result)

# Get all in category
functions = inspector.classified['Built-in Function']
print(functions)

# Format output
formatter = OutputFormatter()
info = result['info']
formatted = formatter.format_class(info)
print(formatted)
```

## Key Concepts Explained

### 1. What Are Built-ins?
Objects available without importing. In the `builtins` module.

### 2. Why 157 Built-ins?
- 51 functions: `print()`, `len()`, etc.
- 27 classes: `dict`, `list`, etc.
- 69 exceptions: `ValueError`, `TypeError`, etc.
- 6 constants: `True`, `False`, `None`, etc.
- 4 other: miscellaneous

### 3. Why Inspect Built-ins?
- Understand Python's core
- Learn magic methods
- Debug custom classes
- Write Pythonic code

### 4. What's a Magic Method?
Methods like `__len__`, `__str__`, `__add__` that Python calls automatically.

Example:
```python
my_list = [1, 2, 3]
len(my_list)        # Python calls my_list.__len__()
str(my_list)        # Python calls my_list.__str__()
my_list + [4]       # Python calls my_list.__add__([4])
```

### 5. Function vs Class?
- **Function**: Call directly → `print("hi")`
- **Class**: Create instance → `d = dict()`, then use `d`

## Most Useful Inspections

```bash
# Core data structures
--inspect dict
--inspect list
--inspect str
--inspect tuple
--inspect set

# Essential functions
--inspect len
--inspect print
--inspect range
--inspect enumerate
--inspect zip

# Type checking
--inspect isinstance
--inspect issubclass
--inspect type

# Common exceptions
--inspect ValueError
--inspect TypeError
--inspect KeyError
--inspect AttributeError
```

## Learning Path

1. **Start**: `--summary` (get overview)
2. **Explore**: `--inspect dict` (learn one class)
3. **Compare**: `--inspect list` (see similarities)
4. **Deep Dive**: `--category "Built-in Class"` (see all classes)
5. **Master**: `--all` (complete reference)

## Quick Facts

- 📊 157 total built-ins in Python 3
- 🏎️ All implemented in C for speed
- 🔧 Most common: `len()`, `print()`, `range()`, `list()`, `dict()`
- 🎯 Most magic methods: `dict` and `list` classes
- ⚠️ Most exceptions: 69 different exception classes
- 🔒 Constants: Only 6 (`True`, `False`, `None`, `Ellipsis`, `NotImplemented`, `__debug__`)

## Further Reading

After using this tool, explore:
- Python Data Model (official docs)
- PEP 3119 (Abstract Base Classes)
- `inspect` module documentation
- CPython source code (C implementation)

---

**Remember**: This tool explains *how* Python works internally, not just *what* exists.
