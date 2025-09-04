#!/usr/bin/python3

"""
Math Operations - Source Code for Testing Examples

Simple functions to demonstrate testing concepts:
- Basic arithmetic operations
- Boolean logic functions
- Type hints for clarity
- Functions under test (FUT)
"""

# ============================================================================
# BASIC ARITHMETIC - Simple function for testing fundamentals
# ============================================================================

def add(a, b):
    """Add two numbers together."""
    return a + b
    # MLOps use: metric calculations, loss functions, aggregations
    # Testing: verify correct arithmetic, edge cases, type handling

# ============================================================================
# BOOLEAN LOGIC - Function returning boolean for testing assertions
# ============================================================================

def is_even(x: int) -> bool:
    """Check if a number is even."""
    return x % 2 == 0
    # MLOps use: data filtering, batch processing, validation logic
    # Testing: verify True/False returns, boundary conditions
