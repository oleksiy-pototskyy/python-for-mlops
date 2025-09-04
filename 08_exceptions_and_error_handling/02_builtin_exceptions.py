#!/usr/bin/python3

"""
Built-in Exceptions for MLOps - Educational Examples

Demonstrates common Python exceptions encountered in MLOps:
- ValueError: invalid value conversions
- TypeError: incompatible type operations
- FileNotFoundError: missing files
- KeyError: missing dictionary keys
- IndexError: invalid list/array indices
- ZeroDivisionError: division by zero
"""

# ============================================================================
# ValueError - Invalid value for correct type
# ============================================================================

int("abc")  # Attempting to convert invalid string to integer
# raises ValueError: invalid literal for int() with base 10: 'abc'
# MLOps use: parsing configuration files, converting user input, data validation

# ============================================================================
# TypeError - Operation on incompatible types
# ============================================================================

3 + "test"  # Attempting to add number and string
# raises TypeError: unsupported operand type(s) for +: 'int' and 'str'
# MLOps use: mixing data types in calculations, incorrect function arguments

# ============================================================================
# FileNotFoundError - Missing file or directory
# ============================================================================

open("data.csv")  # Attempting to open non-existent file
# raises FileNotFoundError if the file does not exist
# MLOps use: loading datasets, model files, configuration files

# ============================================================================
# KeyError - Missing dictionary key
# ============================================================================

config = {"lr": 0.01}  # Configuration dictionary
print(config["batch_size"])  # Accessing non-existent key
# raises KeyError: 'batch_size'
# MLOps use: accessing configuration parameters, hyperparameter dictionaries

# ============================================================================
# IndexError - Invalid list/array index
# ============================================================================

data = [1, 2]  # List with 2 elements (indices 0, 1)
print(data[5])  # Accessing index beyond list bounds
# raises IndexError: list index out of range
# MLOps use: accessing batch elements, array slicing, data processing

# ============================================================================
# ZeroDivisionError - Division by zero
# ============================================================================

# accuracy = correct / total  # Division operation
# raises ZeroDivisionError if total is 0
# MLOps use: calculating metrics, loss functions, normalization operations


