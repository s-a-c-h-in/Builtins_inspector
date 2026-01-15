# Python Built-ins Inspector Tool - Example Outputs

## Installation and Usage

```bash
# Make the script executable (optional)
chmod +x builtins_inspector.py

# Basic usage
python builtins_inspector.py --summary
python builtins_inspector.py --inspect <name>
python builtins_inspector.py --category "Built-in Function"
python builtins_inspector.py --all  # Warning: Very long output!
```

## Example 1: Summary Statistics

```bash
$ python builtins_inspector.py --summary
```

**Output:**
```
SUMMARY
=======
Total Built-ins: 157
Built-in Functions: 51
Built-in Classes: 27
Exception Classes: 69
Constants: 6
Other: 4
```

**Explanation:**
- Python's builtins module contains 157 objects total
- Most are exception classes (69) used for error handling
- 51 are functions like `print()`, `len()`, `isinstance()`
- 27 are classes like `dict`, `list`, `str`, `int`
- 6 constants: `True`, `False`, `None`, `Ellipsis`, `NotImplemented`, `__debug__`
- 4 miscellaneous objects

---

## Example 2: Inspecting `dict` (Built-in Class)

```bash
$ python builtins_inspector.py --inspect dict
```

**Output:**
```
Class: dict
-----------
Type: type
Module: builtins
Callable: True (creates instances)

Inheritance Chain (MRO):
  ├─ dict
  └─ object

Public Methods (11):
  clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update
  ... and 1 more
  Note: These are called on instances, e.g., my_obj.method()

Special Methods (35):
  Important: __contains__, __getitem__, __init__, __iter__, __len__, __repr__, __setitem__, __str__
  All: __class__, __class_getitem__, __contains__, __delattr__, __delitem__, __dir__, 
       __doc__, __eq__, __format__, __ge__, __getattribute__, __getitem__, __getstate__, 
       __gt__, __hash__
  ... and 20 more

Documentation:
  dict() -> new empty dictionary 
  dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs
```

**What This Tells Us:**

1. **Type Information**
   - `dict` is a `type` (it's a class that creates objects)
   - Lives in the `builtins` module (always available)
   - Callable because you can do `dict()` to create instances

2. **Inheritance Chain (MRO)**
   - `dict` inherits only from `object` (the root of all classes)
   - Simple inheritance = fast lookups

3. **Public Methods**
   - These are the API you use: `my_dict.get()`, `my_dict.keys()`
   - Called on instances: `d = dict()` then `d.clear()`
   - 11 methods provide dictionary functionality

4. **Special Methods (Magic Methods)**
   - `__contains__`: Makes `'key' in my_dict` work
   - `__getitem__`: Makes `my_dict['key']` work
   - `__setitem__`: Makes `my_dict['key'] = value` work
   - `__len__`: Makes `len(my_dict)` work
   - `__iter__`: Makes `for key in my_dict:` work
   - These implement Python's protocols

5. **Key Insight**
   - `dict` is implemented in C for speed
   - The class defines how dictionaries behave
   - When you do `d['key']`, Python calls `d.__getitem__('key')`
   - This is how Python's syntax maps to method calls

---

## Example 3: Inspecting `print` (Built-in Function)

```bash
$ python builtins_inspector.py --inspect print
```

**Output:**
```
Function: print
---------------
Type: builtin_function_or_method
Module: builtins
Callable: True
Implementation: C (CPython interpreter)

Documentation:
  Prints the values to a stream, or to sys.stdout by default.
```

**What This Tells Us:**

1. **Type Information**
   - Not a class, it's a function
   - Type is `builtin_function_or_method` (CPython-specific)
   - Callable: yes, you invoke it as `print()`

2. **Implementation**
   - Written in C, not Python
   - Part of the CPython interpreter
   - No Python source code to view
   - Fast execution

3. **Key Insight**
   - `print` is a function, not a method
   - No magic method association (unlike `len`)
   - Directly callable: `print("hello")`

---

## Example 4: Inspecting `len` (Function with Magic Method)

```bash
$ python builtins_inspector.py --inspect len
```

**Output:**
```
Function: len
-------------
Type: builtin_function_or_method
Module: builtins
Callable: True
Implementation: C (CPython interpreter)
Triggers Magic Method: __len__
  └─ When you call len(obj), Python looks for obj.__len__()

Documentation:
  Return the number of items in a container.
```

**What This Tells Us:**

1. **Magic Method Connection**
   - `len()` doesn't do the work itself
   - It triggers the `__len__()` method on the object
   - When you call `len(my_list)`, Python calls `my_list.__len__()`

2. **How Python Works**
   ```python
   my_list = [1, 2, 3]
   len(my_list)  # ← Calls my_list.__len__()
   # Returns: 3
   ```

3. **Custom Classes**
   ```python
   class MyContainer:
       def __len__(self):
           return 42
   
   obj = MyContainer()
   len(obj)  # Returns: 42
   ```
   - By implementing `__len__`, your class works with `len()`
   - This is Python's protocol system

4. **Key Insight**
   - Built-in functions often trigger magic methods
   - This is how Python achieves polymorphism
   - Same syntax works for lists, dicts, strings, custom objects

---

## Example 5: Inspecting Constants

```bash
$ python builtins_inspector.py --inspect None
```

**Output:**
```
Constant: None
--------------
Value: None
Type: NoneType
Module: builtins

Documentation:
  Singleton constant.
```

**What This Tells Us:**

1. **Singleton Pattern**
   - Only ONE `None` object exists in Python
   - `None is None` is always `True`
   - Use `is None`, not `== None`

2. **Type Information**
   - `None` has its own type: `NoneType`
   - You cannot create more instances of `NoneType`
   - Represents absence of value

3. **Other Constants**
   - `True` and `False` (type: `bool`)
   - `Ellipsis` (type: `ellipsis`, used in slicing: `arr[..., 0]`)
   - `NotImplemented` (type: `NotImplementedType`, used in operator overloading)
   - `__debug__` (type: `bool`, used for assertions)

---

## Example 6: Category Listing

```bash
$ python builtins_inspector.py --category "Built-in Function"
```

**Output (truncated):**
```
Built-in Function (51)
======================
  abs, aiter, all, anext, any
  ascii, bin, breakpoint, callable, chr
  compile, delattr, dir, divmod, enumerate
  eval, exec, format, getattr, globals
  hasattr, hash, hex, id, input
  isinstance, issubclass, iter, len, locals
  max, min, next, oct, open
  ord, pow, print, repr, reversed
  round, setattr, sorted, sum, vars
  __build_class__, __import__
```

**Insights:**

1. **Function Categories**
   - **Type checking**: `isinstance()`, `issubclass()`, `callable()`
   - **Iteration**: `iter()`, `next()`, `enumerate()`, `reversed()`
   - **Math**: `abs()`, `min()`, `max()`, `sum()`, `round()`, `divmod()`, `pow()`
   - **Introspection**: `dir()`, `vars()`, `globals()`, `locals()`, `id()`
   - **Conversion**: `int()`, `str()`, `bool()`, `hex()`, `oct()`, `bin()`, `chr()`, `ord()`
   - **I/O**: `print()`, `input()`, `open()`
   - **Meta**: `eval()`, `exec()`, `compile()`, `__import__()`

2. **Special Functions**
   - `__build_class__`: Used by Python to build classes (internal)
   - `__import__`: Used by `import` statement (internal)
   - `breakpoint()`: Drops into debugger (Python 3.7+)

---

## Example 7: Exception Class Hierarchy

```bash
$ python builtins_inspector.py --inspect ValueError
```

**Output:**
```
Class: ValueError
-----------------
Type: type
Module: builtins
Callable: True (creates instances)

Inheritance Chain (MRO):
  ├─ ValueError
  ├─ Exception
  ├─ BaseException
  └─ object

Public Methods (2):
  add_note, with_traceback
  Note: These are called on instances, e.g., my_obj.method()

Special Methods (17):
  Important: __init__, __repr__, __str__
  All: __class__, __delattr__, __dir__, __doc__, __eq__, __format__, 
       __ge__, __getattribute__, __gt__, __hash__, __init__, __init_subclass__
  ... and 5 more

Documentation:
  Inappropriate argument value (of correct type).
```

**What This Tells Us:**

1. **Exception Hierarchy**
   - `ValueError` → `Exception` → `BaseException` → `object`
   - All exceptions inherit from `BaseException`
   - Most inherit from `Exception` (except `SystemExit`, `KeyboardInterrupt`)

2. **Usage**
   ```python
   try:
       int("not a number")
   except ValueError as e:
       print(f"Caught: {e}")
   ```

3. **Why Inheritance Matters**
   ```python
   try:
       risky_operation()
   except Exception as e:  # Catches ValueError, TypeError, etc.
       handle_error(e)
   ```

---

## Practical Applications

### 1. Learning Python Internals
```bash
# Understand how iteration works
python builtins_inspector.py --inspect iter
python builtins_inspector.py --inspect next

# See the magic methods for iteration
python builtins_inspector.py --inspect list  # Look for __iter__
```

### 2. Debugging Custom Classes
```python
# If your class doesn't work with len(), check:
python builtins_inspector.py --inspect len
# Output tells you to implement __len__()

class MyClass:
    def __len__(self):
        return 10  # Now len(MyClass()) works!
```

### 3. Understanding Operators
```bash
# How does + work?
# For numbers: __add__
# For sequences: __add__
python builtins_inspector.py --inspect list  # See __add__ in special methods
```

### 4. Exploring Exception Handling
```bash
# See all available exceptions
python builtins_inspector.py --category "Exception Class"

# Understand specific ones
python builtins_inspector.py --inspect TypeError
python builtins_inspector.py --inspect KeyError
```

---

## Advanced Usage Tips

### Combining with grep
```bash
# Find all functions that trigger magic methods
python builtins_inspector.py --all | grep "Triggers Magic Method"

# Find all classes with __len__
python builtins_inspector.py --all | grep -A 5 "__len__"
```

### Scripting
```python
from builtins_inspector import BuiltinsInspector

inspector = BuiltinsInspector()
inspector.inspect_all()

# Get all class names
classes = inspector.classified['Built-in Class']
print(f"Found {len(classes)} classes")

# Inspect each one programmatically
for cls_name in classes:
    result = inspector.inspect_single(cls_name)
    # Process result...
```

### Comparison Across Python Versions
```bash
# Run on Python 3.8
python3.8 builtins_inspector.py --summary > py38_builtins.txt

# Run on Python 3.11
python3.11 builtins_inspector.py --summary > py311_builtins.txt

# Compare
diff py38_builtins.txt py311_builtins.txt
```

---

## Key Takeaways

1. **Python's Core Is Small**
   - Only 157 built-in objects
   - Everything else is in the standard library or external packages

2. **Functions vs Classes**
   - Functions: Direct callable (e.g., `print()`)
   - Classes: Create instances (e.g., `list()` creates a list)

3. **Magic Methods Are Everything**
   - They implement Python's protocols
   - They make operators and syntax work
   - They enable duck typing

4. **C Implementation**
   - Built-ins are C code for performance
   - You can't see the source in Python
   - But you can understand the API and behavior

5. **Inheritance Matters**
   - MRO determines method lookup
   - Exception hierarchy enables catch-all handlers
   - All classes inherit from `object`

---

## Questions This Tool Answers

✓ "How does `len()` actually work?"
✓ "What methods does `dict` have?"
✓ "What's the inheritance chain for `ValueError`?"
✓ "How many built-in exceptions are there?"
✓ "What magic methods do I need to implement for my custom class?"
✓ "What's the difference between a function and a class in builtins?"
✓ "Which built-in functions trigger magic methods?"

This tool gives you **interpreter-level understanding** of Python's foundations.
