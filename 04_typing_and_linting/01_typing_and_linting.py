#!/usr/bin/python3

"""
Python Typing and Linting for MLOps - Educational Examples

Demonstrates code quality patterns essential for:
- Type safety and documentation
- Code readability and maintenance
- Team collaboration and debugging
- Production-ready MLOps code
"""

# ============================================================================
# UNTYPED FUNCTIONS - Dynamic but unclear
# ============================================================================

def add(a, b):
    """Function without type hints - unclear what types are expected."""
    return a + b
    # Problem: unclear what types a and b should be
    # MLOps issue: leads to runtime errors, hard to debug

# Function works with different types (Python's dynamic nature)
print(add(2, 3))      # 5 - works with integers
print(add("a", "b"))  # ab - works with strings
# This flexibility can cause bugs in ML pipelines!

# ============================================================================
# TYPED FUNCTIONS - Clear and safe
# ============================================================================

def add(a: int, b: int) -> int:
    """Function with type hints - clear expectations and return type."""
    return a + b
    # Type hints: a and b must be int, returns int
    # MLOps benefit: prevents type-related bugs, improves IDE support

# ============================================================================
# COMPLEX TYPE HINTS - Collections and imports
# ============================================================================

from typing import List

def load_files(paths: List[str]) -> List[str]:
    """Function with complex type hints for collections."""
    ...  # Placeholder implementation
    # Type hints: paths is list of strings, returns list of strings
    # MLOps use: data loading, file processing, batch operations

# ============================================================================
# LINTING ISSUES - Code style problems
# ============================================================================

# Poor formatting - linting tools would flag these issues
x=10          # Missing spaces around operator
print( x )    # Extra spaces inside parentheses
# MLOps impact: inconsistent code style hurts team collaboration
# Solution: use tools like flake8, black, pylint for consistent formatting


