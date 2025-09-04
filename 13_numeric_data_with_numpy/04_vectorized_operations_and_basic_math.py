#!/usr/bin/python3

"""
Vectorized Operations and Basic Math for MLOps - Educational Examples

Demonstrates NumPy mathematical operations essential for MLOps:
- Element-wise arithmetic operations
- Mathematical functions (sqrt, log, exp)
- Broadcasting with scalars and arrays
- Practical ML calculations (MSE)
"""

import numpy as np

# ============================================================================
# ELEMENT-WISE ARITHMETIC - Operations between arrays of same shape
# ============================================================================

a = np.array([1, 2, 3])     # First array
b = np.array([10, 20, 30])  # Second array (same shape)

print(a + b)   # [11 22 33] - element-wise addition
print(a * b)   # [10 40 90] - element-wise multiplication
# Operations applied to corresponding elements: a[i] op b[i]
# Much faster than Python loops for large arrays
# MLOps use: feature combinations, data transformations, model computations

# ============================================================================
# MATHEMATICAL FUNCTIONS - Built-in math operations
# ============================================================================

arr = np.array([1, 4, 9, 16])  # Input array

print(np.sqrt(arr))   # square root: [1. 2. 3. 4.]
print(np.log(arr))    # natural log: [0.    1.386 2.197 2.773]
print(np.exp(arr))    # exponential: [2.718e+00 5.460e+01 8.103e+03 8.886e+06]
# Vectorized math functions - no loops needed
# MLOps use: activation functions, loss calculations, feature engineering

# ============================================================================
# SCALAR BROADCASTING - Operations between array and single value
# ============================================================================

a = np.array([1, 2, 3])  # Array
b = 10                   # Scalar value
print(a + b)   # [11 12 13] - scalar added to each element
# Broadcasting: scalar automatically applied to all array elements
# MLOps use: normalization, scaling, bias addition

# ============================================================================
# ARRAY BROADCASTING - Operations between different shaped arrays
# ============================================================================

matrix = np.array([[1, 2, 3],    # 2x3 matrix
                   [4, 5, 6]])
print(matrix + a)  # Add 1D array [1,2,3] to each row of matrix
# Output: [[2 4 6]
#          [5 7 9]]
# Broadcasting rules: smaller array stretched to match larger array shape
# MLOps use: batch normalization, adding biases to layers

# ============================================================================
# PRACTICAL ML EXAMPLE - Mean Squared Error calculation
# ============================================================================

pred = np.array([2.5, 0.0, 2, 8])    # Model predictions
label = np.array([3, -0.5, 2, 7])    # True labels

error = (pred - label) ** 2  # Element-wise squared differences
print(error)        # [0.25 0.25 0.   1.  ] - squared errors per sample
print(error.mean()) # 0.375 - mean squared error (MSE)
# Vectorized MSE calculation: no explicit loops needed
# MLOps use: loss functions, model evaluation, performance metrics


