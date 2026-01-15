#!/usr/bin/env python3
"""
Python Built-ins Inspector Tool
================================
A deep inspection tool for understanding Python's builtins module at the interpreter level.

This tool goes beyond simple listing - it classifies, analyzes, and explains
every object in the builtins namespace with educational clarity.
"""

import builtins
import inspect
import textwrap
from typing import Any, Dict, List, Tuple, Optional
from collections import defaultdict


class BuiltinsInspector:
    """Main inspector class for analyzing Python's builtins module."""
    
    # Magic methods that correspond to built-in functions
    FUNCTION_TO_MAGIC = {
        'len': '__len__',
        'str': '__str__',
        'repr': '__repr__',
        'int': '__int__',
        'float': '__float__',
        'bool': '__bool__',
        'bytes': '__bytes__',
        'hash': '__hash__',
        'iter': '__iter__',
        'next': '__next__',
        'reversed': '__reversed__',
        'abs': '__abs__',
        'round': '__round__',
        'divmod': '__divmod__',
        'pow': '__pow__',
        'getattr': '__getattribute__',
        'setattr': '__setattr__',
        'delattr': '__delattr__',
        'dir': '__dir__',
        'format': '__format__',
    }
    
    def __init__(self):
        self.names = []
        self.objects = {}
        self.classified = defaultdict(list)
        
    def collect_names(self) -> List[str]:
        """Collect all names from the builtins module."""
        self.names = sorted(dir(builtins))
        return self.names
    
    def resolve_object(self, name: str) -> Any:
        """Resolve a name to its actual object in builtins."""
        return getattr(builtins, name)
    
    def classify_object(self, name: str, obj: Any) -> str:
        """
        Classify an object into one of these categories:
        - Built-in Function
        - Built-in Class
        - Exception Class
        - Constant
        - Other
        """
        # Check if it's a constant
        if name in ('True', 'False', 'None', 'Ellipsis', 'NotImplemented', '__debug__'):
            return 'Constant'
        
        # Check if it's a class/type
        if isinstance(obj, type):
            # Check if it's an exception class
            if issubclass(obj, BaseException):
                return 'Exception Class'
            return 'Built-in Class'
        
        # Check if it's a callable (function)
        if callable(obj) and not isinstance(obj, type):
            return 'Built-in Function'
        
        return 'Other'
    
    def get_clean_docstring(self, obj: Any, max_lines: int = 3) -> str:
        """Extract and clean the first paragraph of a docstring."""
        doc = inspect.getdoc(obj)
        if not doc:
            return "No documentation available."
        
        # Take first paragraph (up to first double newline or max_lines)
        lines = doc.split('\n')
        paragraph = []
        for line in lines[:max_lines]:
            if not line.strip() and paragraph:
                break
            if line.strip():
                paragraph.append(line.strip())
        
        return ' '.join(paragraph) if paragraph else doc.split('\n')[0]
    
    def get_inheritance_chain(self, cls: type) -> List[str]:
        """Get the Method Resolution Order (MRO) for a class."""
        return [c.__name__ for c in cls.__mro__]
    
    def get_methods(self, cls: type) -> Tuple[List[str], List[str]]:
        """
        Separate class methods into public and special methods.
        Returns: (public_methods, special_methods)
        """
        public = []
        special = []
        
        for name in dir(cls):
            if name.startswith('_'):
                if name.startswith('__') and name.endswith('__'):
                    special.append(name)
            else:
                attr = getattr(cls, name, None)
                if callable(attr):
                    public.append(name)
        
        return sorted(public), sorted(special)
    
    def inspect_function(self, name: str, obj: Any) -> Dict[str, Any]:
        """Deep inspection of a built-in function."""
        info = {
            'name': name,
            'type': type(obj).__name__,
            'module': getattr(obj, '__module__', 'builtins'),
            'callable': callable(obj),
            'docstring': self.get_clean_docstring(obj),
            'implemented_in': 'C (CPython interpreter)',
        }
        
        # Check if this function triggers a magic method
        if name in self.FUNCTION_TO_MAGIC:
            info['triggers_magic'] = self.FUNCTION_TO_MAGIC[name]
        
        return info
    
    def inspect_class(self, name: str, cls: type) -> Dict[str, Any]:
        """Deep inspection of a built-in class."""
        public_methods, special_methods = self.get_methods(cls)
        
        info = {
            'name': name,
            'type': type(cls).__name__,
            'module': getattr(cls, '__module__', 'builtins'),
            'callable': callable(cls),
            'docstring': self.get_clean_docstring(cls),
            'mro': self.get_inheritance_chain(cls),
            'public_methods': public_methods,
            'special_methods': special_methods,
        }
        
        return info
    
    def inspect_constant(self, name: str, obj: Any) -> Dict[str, Any]:
        """Inspect a built-in constant."""
        return {
            'name': name,
            'value': repr(obj),
            'type': type(obj).__name__,
            'module': 'builtins',
            'callable': callable(obj),
            'docstring': self.get_clean_docstring(obj) if hasattr(obj, '__doc__') else 'Singleton constant.',
        }
    
    def inspect_single(self, name: str) -> Optional[Dict[str, Any]]:
        """Inspect a single built-in by name."""
        try:
            obj = self.resolve_object(name)
            category = self.classify_object(name, obj)
            
            if category == 'Built-in Function':
                return {'category': category, 'info': self.inspect_function(name, obj)}
            elif category in ('Built-in Class', 'Exception Class'):
                return {'category': category, 'info': self.inspect_class(name, obj)}
            elif category == 'Constant':
                return {'category': category, 'info': self.inspect_constant(name, obj)}
            else:
                return {
                    'category': category,
                    'info': {
                        'name': name,
                        'type': type(obj).__name__,
                        'value': repr(obj),
                    }
                }
        except Exception as e:
            return None
    
    def inspect_all(self):
        """Inspect all built-ins and classify them."""
        self.collect_names()
        
        for name in self.names:
            try:
                obj = self.resolve_object(name)
                self.objects[name] = obj
                category = self.classify_object(name, obj)
                self.classified[category].append(name)
            except Exception as e:
                print(f"Error inspecting {name}: {e}")
    
    def get_summary(self) -> Dict[str, int]:
        """Get a summary count of all categories."""
        return {
            'Total Built-ins': len(self.names),
            'Built-in Functions': len(self.classified['Built-in Function']),
            'Built-in Classes': len(self.classified['Built-in Class']),
            'Exception Classes': len(self.classified['Exception Class']),
            'Constants': len(self.classified['Constant']),
            'Other': len(self.classified['Other']),
        }


class OutputFormatter:
    """Formats inspection results for human-readable output."""
    
    @staticmethod
    def format_section_header(title: str, char: str = '=') -> str:
        """Create a section header."""
        return f"\n{title}\n{char * len(title)}"
    
    @staticmethod
    def format_function(info: Dict[str, Any]) -> str:
        """Format built-in function information."""
        output = []
        output.append(OutputFormatter.format_section_header(f"Function: {info['name']}", '-'))
        output.append(f"Type: {info['type']}")
        output.append(f"Module: {info['module']}")
        output.append(f"Callable: {info['callable']}")
        output.append(f"Implementation: {info['implemented_in']}")
        
        if 'triggers_magic' in info:
            output.append(f"Triggers Magic Method: {info['triggers_magic']}")
            output.append(f"  └─ When you call {info['name']}(obj), Python looks for obj.{info['triggers_magic']}()")
        
        output.append(f"\nDocumentation:\n  {info['docstring']}")
        
        return '\n'.join(output)
    
    @staticmethod
    def format_class(info: Dict[str, Any]) -> str:
        """Format built-in class information."""
        output = []
        output.append(OutputFormatter.format_section_header(f"Class: {info['name']}", '-'))
        output.append(f"Type: {info['type']}")
        output.append(f"Module: {info['module']}")
        output.append(f"Callable: {info['callable']} (creates instances)")
        
        output.append(f"\nInheritance Chain (MRO):")
        for i, cls in enumerate(info['mro']):
            prefix = '  └─' if i == len(info['mro']) - 1 else '  ├─'
            output.append(f"{prefix} {cls}")
        
        if info['public_methods']:
            output.append(f"\nPublic Methods ({len(info['public_methods'])}):")
            output.append("  " + ", ".join(info['public_methods'][:10]))
            if len(info['public_methods']) > 10:
                output.append(f"  ... and {len(info['public_methods']) - 10} more")
            output.append("  Note: These are called on instances, e.g., my_obj.method()")
        
        if info['special_methods']:
            output.append(f"\nSpecial Methods ({len(info['special_methods'])}):")
            # Show important ones
            important = [m for m in info['special_methods'] if m in [
                '__init__', '__str__', '__repr__', '__len__', '__getitem__',
                '__setitem__', '__iter__', '__next__', '__contains__', '__call__'
            ]]
            if important:
                output.append("  Important: " + ", ".join(important))
            output.append("  All: " + ", ".join(info['special_methods'][:15]))
            if len(info['special_methods']) > 15:
                output.append(f"  ... and {len(info['special_methods']) - 15} more")
        
        output.append(f"\nDocumentation:\n  {info['docstring']}")
        
        return '\n'.join(output)
    
    @staticmethod
    def format_constant(info: Dict[str, Any]) -> str:
        """Format built-in constant information."""
        output = []
        output.append(OutputFormatter.format_section_header(f"Constant: {info['name']}", '-'))
        output.append(f"Value: {info['value']}")
        output.append(f"Type: {info['type']}")
        output.append(f"Module: {info['module']}")
        output.append(f"\nDocumentation:\n  {info['docstring']}")
        
        return '\n'.join(output)
    
    @staticmethod
    def format_summary(summary: Dict[str, int]) -> str:
        """Format the summary statistics."""
        output = []
        output.append(OutputFormatter.format_section_header("SUMMARY", '='))
        for key, value in summary.items():
            output.append(f"{key}: {value}")
        return '\n'.join(output)
    
    @staticmethod
    def format_category_list(category: str, names: List[str]) -> str:
        """Format a list of names in a category."""
        output = []
        output.append(OutputFormatter.format_section_header(f"{category} ({len(names)})", '='))
        
        # Group in lines of 5
        for i in range(0, len(names), 5):
            chunk = names[i:i+5]
            output.append("  " + ", ".join(chunk))
        
        return '\n'.join(output)


def main():
    """Main entry point for the inspector tool."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Python Built-ins Inspector Tool - Deep analysis of builtins module',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''
        Examples:
          python builtins_inspector.py --summary
          python builtins_inspector.py --inspect dict
          python builtins_inspector.py --inspect print
          python builtins_inspector.py --category "Built-in Function"
          python builtins_inspector.py --all
        ''')
    )
    
    parser.add_argument('--summary', action='store_true',
                       help='Show summary statistics')
    parser.add_argument('--inspect', type=str, metavar='NAME',
                       help='Inspect a specific built-in by name')
    parser.add_argument('--category', type=str,
                       help='List all built-ins in a category')
    parser.add_argument('--all', action='store_true',
                       help='Show detailed inspection of ALL built-ins (very long!)')
    
    args = parser.parse_args()
    
    inspector = BuiltinsInspector()
    formatter = OutputFormatter()
    
    # Always run the inspection
    inspector.inspect_all()
    
    # Handle commands
    if args.summary:
        print(formatter.format_summary(inspector.get_summary()))
    
    elif args.inspect:
        result = inspector.inspect_single(args.inspect)
        if result:
            info = result['info']
            category = result['category']
            
            if category == 'Built-in Function':
                print(formatter.format_function(info))
            elif category in ('Built-in Class', 'Exception Class'):
                print(formatter.format_class(info))
            elif category == 'Constant':
                print(formatter.format_constant(info))
            else:
                print(f"Name: {info['name']}")
                print(f"Type: {info['type']}")
                print(f"Value: {info['value']}")
        else:
            print(f"Could not inspect '{args.inspect}'")
    
    elif args.category:
        if args.category in inspector.classified:
            print(formatter.format_category_list(args.category, inspector.classified[args.category]))
        else:
            print(f"Unknown category: {args.category}")
            print(f"Available categories: {', '.join(inspector.classified.keys())}")
    
    elif args.all:
        print(formatter.format_summary(inspector.get_summary()))
        
        for category in ['Built-in Function', 'Built-in Class', 'Exception Class', 'Constant', 'Other']:
            if category in inspector.classified:
                print(f"\n\n{formatter.format_section_header(category, '=')}\n")
                for name in inspector.classified[category]:
                    result = inspector.inspect_single(name)
                    if result:
                        info = result['info']
                        if category == 'Built-in Function':
                            print(formatter.format_function(info))
                        elif category in ('Built-in Class', 'Exception Class'):
                            print(formatter.format_class(info))
                        elif category == 'Constant':
                            print(formatter.format_constant(info))
                        print()  # Blank line between items
    
    else:
        # Default: show summary
        print(formatter.format_summary(inspector.get_summary()))
        print("\nUse --help to see available options")


if __name__ == '__main__':
    main()
