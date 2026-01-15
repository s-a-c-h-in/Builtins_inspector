# Python Built-ins Inspector Tool - Technical Documentation

## Overview

This tool provides **interpreter-level understanding** of Python's `builtins` module. It doesn't just list objects—it classifies, analyzes, and explains them the way Python itself understands them.

## How It Works Internally

### 1. Architecture

The tool uses object-oriented design with two main classes:

- **`BuiltinsInspector`**: Core inspection engine
- **`OutputFormatter`**: Presentation layer

### 2. Inspection Pipeline

```
collect_names() → resolve_object() → classify_object() → inspect_*() → format_output()
```

#### Step-by-Step Process:

**A. Name Collection**
```python
def collect_names(self) -> List[str]:
    self.names = sorted(dir(builtins))
```
Uses `dir(builtins)` to get all attribute names in the builtins namespace.

**B. Object Resolution**
```python
def resolve_object(self, name: str) -> Any:
    return getattr(builtins, name)
```
Converts each name string into the actual Python object it refers to.

**C. Classification**
```python
def classify_object(self, name: str, obj: Any) -> str:
```
This is where the magic happens. The classifier uses Python's introspection:

1. **Constants**: Hardcoded check for `True`, `False`, `None`, `Ellipsis`, etc.
2. **Classes vs Functions**: Uses `isinstance(obj, type)` to detect classes
3. **Exception Classes**: Uses `issubclass(obj, BaseException)` 
4. **Functions**: Anything `callable()` that isn't a type
5. **Other**: Fallback category

**D. Specialized Inspection**

Depending on category, different inspection methods are called:

- `inspect_function()`: For built-in functions like `print`, `len`
- `inspect_class()`: For classes like `dict`, `list`, `str`
- `inspect_constant()`: For singletons like `True`, `None`

### 3. Deep Inspection Details

#### For Functions:
```python
def inspect_function(self, name: str, obj: Any) -> Dict[str, Any]:
```

Extracts:
- **Type information**: Uses `type(obj).__name__`
- **Module**: Uses `getattr(obj, '__module__', 'builtins')`
- **Documentation**: Uses `inspect.getdoc(obj)` with smart truncation
- **Magic method mapping**: Cross-references with `FUNCTION_TO_MAGIC` dict

**Key Insight**: Built-in functions are implemented in C, not Python, so they have no Python source code. We explain which magic methods they trigger (e.g., `len()` → `__len__()`).

#### For Classes:
```python
def inspect_class(self, name: str, cls: type) -> Dict[str, Any]:
```

Extracts:
- **MRO (Method Resolution Order)**: Uses `cls.__mro__` to show inheritance chain
- **Method separation**: Splits into public methods and special (`__dunder__`) methods
- **Callable detection**: Uses `callable(attr)` on each attribute

**Key Insight**: Classes are blueprints. Methods belong to the class but are called on *instances*. The tool clearly explains this distinction.

### 4. Smart Docstring Extraction

```python
def get_clean_docstring(self, obj: Any, max_lines: int = 3) -> str:
```

Challenges with built-in docstrings:
- Often very long and technical
- Multiple paragraphs
- C-style formatting

Solution:
1. Use `inspect.getdoc()` to normalize whitespace
2. Extract only first paragraph (up to blank line)
3. Limit to `max_lines` to prevent overwhelming output
4. Join lines into readable prose

### 5. Method Categorization

```python
def get_methods(self, cls: type) -> Tuple[List[str], List[str]]:
```

Separates class methods into:
- **Public methods**: User-facing API (e.g., `append`, `sort`)
- **Special methods**: Protocol implementation (e.g., `__len__`, `__iter__`)

Uses name-based filtering:
- Starts with `_` but not `__...__`: private (excluded)
- Starts and ends with `__`: special (magic methods)
- Everything else: public

### 6. Magic Method Mapping

The tool maintains a dictionary mapping built-in functions to their corresponding magic methods:

```python
FUNCTION_TO_MAGIC = {
    'len': '__len__',
    'str': '__str__',
    'iter': '__iter__',
    # ... etc
}
```

This explains **how Python actually works**:
- When you call `len(my_list)`, Python calls `my_list.__len__()`
- When you call `str(my_obj)`, Python calls `my_obj.__str__()`

This is the interpreter-level understanding the tool provides.

## Output Design Philosophy

### Principles:

1. **Hierarchical Structure**: Information organized from general to specific
2. **Visual Separation**: Clear headers, indentation, tree structures
3. **Selective Detail**: Show what matters, hide noise
4. **Educational Context**: Explain *why* things work, not just *what* they are

### Example Output Structure:

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

Notice:
- Clear hierarchy
- Type information
- Implementation detail (C code)
- Practical explanation of magic method
- Concise documentation

## Categories Explained

### 1. Built-in Function
Objects like `print`, `len`, `isinstance`.
- Implemented in C for performance
- Often trigger magic methods
- Not classes, cannot be inherited

### 2. Built-in Class
Objects like `dict`, `list`, `str`, `int`.
- Can be instantiated
- Can be inherited
- Define data structures and types
- Have rich method APIs

### 3. Exception Class
Objects like `ValueError`, `TypeError`, `Exception`.
- Inherit from `BaseException`
- Used for error handling
- Form an inheritance hierarchy

### 4. Constant
Objects like `True`, `False`, `None`, `Ellipsis`.
- Singletons (only one instance exists)
- Identity-based (use `is`, not `==`)
- Immutable by nature

### 5. Other
Rare edge cases that don't fit above categories.

## Advanced Features

### Single Object Inspection
```bash
python builtins_inspector.py --inspect dict
```
Deep-dives into one specific built-in with full detail.

### Category Listing
```bash
python builtins_inspector.py --category "Built-in Function"
```
Shows all objects in a specific category.

### Summary Statistics
```bash
python builtins_inspector.py --summary
```
Quick overview of how many built-ins exist in each category.

### Full Inspection
```bash
python builtins_inspector.py --all
```
Comprehensive report of every single built-in (very long output).

## Technical Insights

### Why This Matters

Understanding builtins is fundamental because:

1. **These are Python's primitives**: Everything else is built on these
2. **Performance critical**: Built-ins are optimized C code
3. **Protocol implementation**: Shows how Python's protocols (iteration, containment, etc.) work
4. **Language design**: Reveals Python's core design philosophy

### What Makes This Tool Different

Most tools just list objects. This tool:
- **Classifies** using Python's own type system
- **Explains** the relationship between functions and magic methods
- **Educates** about how Python works internally
- **Organizes** information for human understanding

### Limitations

- Built-in functions have no Python source (they're in C)
- Docstrings vary in quality and completeness
- Some objects are implementation details, not meant for direct use
- Module-level introspection can't reveal everything about C internals

## Code Quality Features

1. **Type Hints**: All functions have proper type annotations
2. **Docstrings**: Every class and method documented
3. **Error Handling**: Graceful failures with try-except blocks
4. **Separation of Concerns**: Inspection logic separate from formatting
5. **Extensibility**: Easy to add new categories or inspection methods

## Performance Characteristics

- **Fast**: Entire inspection runs in milliseconds
- **Memory Efficient**: Objects are inspected lazily
- **No Side Effects**: Pure introspection, no state modification
- **Deterministic**: Same results every time (sorted output)

## Future Enhancements

Potential additions:
- Interactive mode with REPL
- Search/filter capabilities
- Comparison between Python versions
- Export to JSON/HTML formats
- Built-in function signature inspection (where available)
- Performance profiling of built-ins
