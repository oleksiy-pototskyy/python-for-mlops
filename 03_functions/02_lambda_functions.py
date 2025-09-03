#!/usr/bin/python3

"""
Python Lambda Functions for MLOps - Educational Examples

Demonstrates lambda patterns essential for:
- Inline function definitions
- Data processing and transformations
- Sorting and filtering operations
- Functional programming patterns
"""

# ============================================================================
# REGULAR FUNCTION vs LAMBDA - Comparison
# ============================================================================

# Traditional function definition
def square(x):
    return x**2
    # MLOps use: reusable operations, complex logic

# Lambda function - anonymous, inline function
square = lambda x: x**2
print(square(5))  # 25
# Syntax: lambda parameters: expression
# MLOps use: simple transformations, one-time operations

# ============================================================================
# LAMBDA WITH SORTING - Custom sort keys
# ============================================================================

# Sort files by extension using lambda
files = ["train.csv", "validate.json", "test.csv"]
files.sort(key=lambda f: f.split(".")[-1])  # Extract file extension
print(files)  # Sorted by extension: .csv, .csv, .json
# MLOps use: sort datasets by type, models by performance, logs by timestamp

# ============================================================================
# LAMBDA WITH FILTER - Data selection
# ============================================================================

# Filter high-performing models using lambda
scores = [0.91, 0.83, 0.95, 0.76]
high = list(filter(lambda s: s > 0.9, scores))  # Keep scores > 0.9
print(high)  # [0.91, 0.95]
# filter() applies lambda to each item, keeps items where lambda returns True
# MLOps use: filter good models, select valid data, threshold-based selection

# ============================================================================
# LAMBDA WITH MAP - Data transformation
# ============================================================================

# Transform data using lambda
values = [1, 2, 3]
squares = list(map(lambda x: x**2, values))  # Apply x**2 to each value
print(squares)  # [1, 4, 9]
# map() applies lambda to each item, returns transformed results
# MLOps use: feature scaling, metric conversion, data normalization


