# Python Built-ins Inspector Tool

> **Deep inspection and educational analysis of Python's `builtins` module**

A professional-grade tool that goes beyond simple listing to provide interpreter-level understanding of Python's foundational objects.

---

## What This Tool Does

This tool **deeply inspects** Python's builtins module and explains:

**What each built-in is**: Function, Class, Exception, or Constant  
**How it works internally**: C implementation, magic methods, protocols  
**How to use it**: Public API, special methods, inheritance  
**Why it matters**: Educational context and practical implications  

### Not Just Another `dir()` Wrapper

Most tools just list names. This tool:
- **Classifies** using Python's type system
- **Explains** magic method connections
- **Educates** about language design
- **Organizes** for human understanding

Think of it as **Python's built-in documentation written for language designers**.

---

## Quick Start

```bash
# No installation required - pure Python standard library
python builtins_inspector.py --summary

# Inspect specific built-ins
python builtins_inspector.py --inspect dict
python builtins_inspector.py --inspect len

# List categories
python builtins_inspector.py --category "Built-in Function"

# Full inspection (warning: very long!)
python builtins_inspector.py --all
```

---

## Requirements

- Python 3.6 or higher
- No external dependencies
- Works on all platforms (Linux, macOS, Windows)

---

## Core Features

### 1. Intelligent Classification

Automatically categorizes every built-in into:

| Category | Count | Examples |
|----------|-------|----------|
| **Built-in Function** | 51 | `print`, `len`, `isinstance` |
| **Built-in Class** | 27 | `dict`, `list`, `str`, `int` |
| **Exception Class** | 69 | `ValueError`, `TypeError`, `KeyError` |
| **Constant** | 6 | `True`, `False`, `None`, `Ellipsis` |
| **Other** | 4 | Miscellaneous objects |

### 2. Deep Inspection

For **functions**, shows:
- Type and module information
- C implementation details
- Which magic methods they trigger
- Clean documentation

For **classes**, shows:
- Method Resolution Order (MRO)
- Public methods vs special methods
- Inheritance hierarchy
- Protocol implementation

For **constants**, shows:
- Value and type
- Singleton behavior
- Usage context

### 3. Educational Output

Example for `len()`:
```
Function: len
-------------
Type: builtin_function_or_method
Module: builtins
Implementation: C (CPython interpreter)
Triggers Magic Method: __len__
  └─ When you call len(obj), Python looks for obj.__len__()

Documentation:
  Return the number of items in a container.
```

This **explains the connection** between `len()` and `__len__()` that most documentation misses.

---

## Documentation Files

| File | Purpose |
|------|---------|
| **QUICK_REFERENCE.md** | Command cheat sheet and common use cases |
| **DOCUMENTATION.md** | Technical internals and architecture |
| **EXAMPLES.md** | Detailed example outputs with explanations |
| **README.md** | This file - overview and getting started |

---

## Use Cases

### 1. Learning Python Internals
```bash
# Understand how iteration works
python builtins_inspector.py --inspect iter
python builtins_inspector.py --inspect next
```

### 2. Debugging Custom Classes
```python
# Your class doesn't work with len()?
# Check what's needed:
python builtins_inspector.py --inspect len
# Output: "Triggers Magic Method: __len__"
# Solution: Implement __len__ in your class!
```

### 3. Understanding Operators
```bash
# How does + work for lists?
python builtins_inspector.py --inspect list
# Look for __add__ in special methods
```

### 4. Exception Hierarchy
```bash
# See all available exceptions
python builtins_inspector.py --category "Exception Class"

# Understand specific ones
python builtins_inspector.py --inspect ValueError
```

---

## Key Insights from This Tool

### 1. Functions Trigger Magic Methods

```python
len(my_list)    # → my_list.__len__()
str(my_obj)     # → my_obj.__str__()
iter(my_seq)    # → my_seq.__iter__()
```

The tool **explicitly shows** these connections, which is crucial for understanding Python.

### 2. Classes Are Blueprints

```python
dict()          # Creates a new dictionary instance
d = dict()      # d is the instance
d.get('key')    # Methods called on instances, not the class
```

The tool **clarifies** that methods belong to classes but are invoked on instances.

### 3. Everything Is an Object

```python
type(print)     # <class 'builtin_function_or_method'>
type(dict)      # <class 'type'>
type(True)      # <class 'bool'>
```

The tool **reveals** the type of every built-in, showing Python's consistency.

### 4. Inheritance Matters

```python
# ValueError inherits from Exception
try:
    int("not a number")
except Exception as e:  # Catches ValueError!
    print(e)
```

The tool **shows MRO** so you understand exception hierarchies.

---

## Command Reference

### Summary Statistics
```bash
python builtins_inspector.py --summary
```
Shows counts per category (10 lines of output).

### Single Object Inspection
```bash
python builtins_inspector.py --inspect <n>
```
Deep dive into one built-in (20-40 lines of output).

### Category Listing
```bash
python builtins_inspector.py --category "<category>"
```
Lists all built-ins in a category (10-50 lines).

Categories:
- `"Built-in Function"`
- `"Built-in Class"`
- `"Exception Class"`
- `"Constant"`
- `"Other"`

### Full Inspection
```bash
python builtins_inspector.py --all
```
Complete analysis of all 157 built-ins (5000+ lines). Pipe to `less` or save to file:
```bash
python builtins_inspector.py --all | less
python builtins_inspector.py --all > full_report.txt
```

---

## Educational Philosophy

This tool follows these principles:

1. **Show, Don't Tell**: Demonstrate how things work with concrete examples
2. **Context Matters**: Explain *why* things are designed this way
3. **Hierarchical Learning**: Start simple, add detail progressively
4. **Practical Focus**: Connect theory to actual code usage
5. **Avoid Jargon**: Use clear language accessible to intermediate programmers

---

## Architecture

### Clean Separation of Concerns

```
BuiltinsInspector   → Core inspection logic
OutputFormatter     → Presentation layer
main()              → CLI interface
```

### Modular Design

```python
collect_names()      # Get all names from builtins
resolve_object()     # Name → actual object
classify_object()    # Object → category
inspect_*()          # Deep analysis per category
format_*()           # Human-readable output
```

### Type-Safe and Well-Documented

- Type hints on all functions
- Docstrings on all classes and methods
- Error handling with try-except
- No external dependencies

---

## Statistics

Python 3.x builtins module contains:

- **157 total objects**
- **51 functions** (32%)
- **27 classes** (17%)
- **69 exceptions** (44%)
- **6 constants** (4%)
- **4 other** (3%)

Most complex classes (by special methods):
1. `dict` - 35 special methods
2. `list` - 34 special methods
3. `str` - 33 special methods

---

## Sample Output

### For a Function (`len`):
```
Function: len
-------------
Type: builtin_function_or_method
Implementation: C (CPython interpreter)
Triggers Magic Method: __len__
  └─ When you call len(obj), Python looks for obj.__len__()
```

### For a Class (`dict`):
```
Class: dict
-----------
Callable: True (creates instances)
Inheritance Chain (MRO):
  ├─ dict
  └─ object
Public Methods (11): clear, copy, get, items, keys, ...
Special Methods (35): __contains__, __getitem__, __setitem__, ...
```

---

## Programmatic Usage

```python
from builtins_inspector import BuiltinsInspector

# Create and run inspector
inspector = BuiltinsInspector()
inspector.inspect_all()

# Get summary
summary = inspector.get_summary()
# {'Total Built-ins': 157, 'Built-in Functions': 51, ...}

# Inspect specific item
result = inspector.inspect_single('dict')
# {'category': 'Built-in Class', 'info': {...}}

# Access classified objects
all_functions = inspector.classified['Built-in Function']
# ['abs', 'all', 'any', 'ascii', 'bin', ...]
```

---

## What You'll Learn

By using this tool, you'll understand:

How Python's syntax maps to method calls  
Why certain methods have `__dunder__` names  
How to make custom classes work with built-in functions  
The difference between functions and classes  
How Python's exception hierarchy works  
What makes Python "Pythonic" at the language level  

---

## Getting Started Path

**Beginner Path:**
1. Run `--summary` to see the landscape
2. Run `--inspect print` to see a simple function
3. Run `--inspect list` to see a simple class
4. Experiment with other built-ins

**Intermediate Path:**
1. Run `--category "Built-in Function"` to see all functions
2. Run `--inspect len` to understand magic methods
3. Run `--inspect dict` to see complex class structure
4. Compare similar objects (e.g., `list` vs `tuple`)

**Advanced Path:**
1. Run `--all` and study the output
2. Compare exceptions: `ValueError` vs `TypeError`
3. Understand MRO: `bool` → `int` → `object`
4. Study protocol implementation in classes

---

## Code Quality

- ✅ Type hints throughout
- ✅ Comprehensive docstrings
- ✅ Error handling
- ✅ No external dependencies
- ✅ PEP 8 compliant
- ✅ Modular and extensible
- ✅ Educational comments

---

## Design Goals

This tool was designed to:

1. **Teach**, not just list
2. **Explain**, not just describe  
3. **Connect**, showing relationships between concepts
4. **Clarify**, making complex ideas accessible
5. **Inspire**, encouraging deeper exploration

---

## Further Reading

After using this tool, explore:

- **Python Data Model** - Official documentation
- **PEP 3119** - Abstract Base Classes
- **CPython Source** - See the C implementation
- **`inspect` module** - Python's introspection tools

---

## Pro Tips

```bash
# Save output for reference
python builtins_inspector.py --inspect dict > dict_ref.txt

# Compare built-ins
diff <(python builtins_inspector.py --inspect list) \
     <(python builtins_inspector.py --inspect tuple)

# Find all iteration-related items
python builtins_inspector.py --all | grep -i "iter"

# Count methods in a class
python builtins_inspector.py --inspect dict | grep -c "Special Methods"
```

---

## Acknowledgments

This tool was built with love for Python and the developers who want to understand it at a deeper level.

---

## License

This is an educational tool. Use it freely for learning and teaching.

---

## Contributing

Ideas for improvement:
- Add JSON/HTML export formats
- Interactive REPL mode
- Comparison between Python versions
- Visual class hierarchy diagrams
- Performance benchmarks

---

**Made for Python developers who want to think like language designers**

Run `--help` to get started, or jump right in with `--inspect dict`!
