#!/usr/bin/python3

"""
Python Comparison Operators for MLOps - Educational Examples

Demonstrates comparison operators essential for:
- Model validation and thresholds
- Data quality checks
- Training condition monitoring
- Performance evaluation
"""

# ============================================================================
# COMPARISON OPERATORS - Essential for conditional logic in MLOps
# ============================================================================

"""
The most common operators are:
•	== equal
•	!= not equal
•	> greater than
•	< less than
•	>= greater or equal
•	<= less or equal
"""

# ============================================================================
# EQUALITY AND INEQUALITY - Exact value comparisons
# ============================================================================

# Integer comparison - exact matching for epochs, batch counts, etc.
epoch = 5
print(epoch == 5)   # True - exact equality check
print(epoch > 10)   # False - greater than comparison
# MLOps use: check current epoch, validate batch sizes, count iterations

# ============================================================================
# THRESHOLD COMPARISONS - Critical for model validation
# ============================================================================

# Float comparison for model performance metrics
accuracy = 0.92

# Threshold validation - common pattern in MLOps
if accuracy >= 0.90:
    print("Model passed validation")
    # MLOps use: model acceptance criteria, early stopping conditions

# ============================================================================
# STRING COMPARISONS - Dataset splits, file types, model names
# ============================================================================

# String equality for dataset identification
dataset = "train"
print(dataset == "test")  # False - string comparison
# MLOps use: validate dataset splits, check file extensions, model types

# ============================================================================
# FLOATING POINT PRECISION - Critical issue in ML computations
# ============================================================================

# Floating point arithmetic precision problem
value = 0.1 + 0.2
print(value == 0.3)  # False - floating point precision issue!
# Output: False (value is actually 0.30000000000000004)
# This is a common source of bugs in ML pipelines!

# SOLUTION: Use math.isclose() for float comparisons
import math
print(math.isclose(value, 0.3))  # True - proper float comparison
# MLOps use: compare loss values, learning rates, model weights

# ============================================================================
# IDENTITY COMPARISONS - None checks and object identity
# ============================================================================

# None comparison - use 'is' not '=='
result = None
print(result is None)   # True - correct way to check for None
# MLOps use: check uninitialized models, missing data, optional parameters

# Avoid using == None; prefer is None for clarity and reliability.
# Why 'is None' is better:
# - 'is' checks object identity (faster)
# - '==' can be overridden by classes (unreliable)
# - 'is None' is the Python standard

# ============================================================================
# CHAINED COMPARISONS - Elegant range checking
# ============================================================================

# Chained comparison - Pythonic way to check ranges
score = 75
if 50 <= score <= 100:
    print("Score is in range")
# Equivalent to: if score >= 50 and score <= 100
# More readable and efficient than separate comparisons
# MLOps use: validate learning rates, batch sizes, dropout rates
