#!/usr/bin/python3

"""
Introduction to NumPy for MLOps - Educational Examples

Demonstrates NumPy fundamentals essential for MLOps:
- Array creation and basic operations
- Vectorized operations for performance
- Multi-dimensional arrays (matrices)
- Shape inspection and data structure
"""

import numpy as np

# ============================================================================
# ARRAY CREATION - Converting Python lists to NumPy arrays
# ============================================================================

arr = np.array([1, 2, 3, 4, 5])  # Create 1D array from Python list
print(arr)  # Output: [1 2 3 4 5]
# NumPy arrays are homogeneous (same data type) and more efficient than lists
# MLOps use: feature vectors, model predictions, training data

# ============================================================================
# VECTORIZED OPERATIONS - Element-wise operations without loops
# ============================================================================

print(arr * 2)  # Output: [ 2  4  6  8 10]
# Multiplies each element by 2 - no explicit loop needed
# Much faster than Python list comprehensions for large datasets
# MLOps use: data normalization, feature scaling, batch processing

# ============================================================================
# MULTI-DIMENSIONAL ARRAYS - Matrices for complex data structures
# ============================================================================

matrix = np.array([[1, 2, 3],    # 2D array (matrix)
                   [4, 5, 6]])   # 2 rows, 3 columns
print(matrix.shape)  # Output: (2, 3) - dimensions of the array
# Shape shows (rows, columns) for 2D arrays
# MLOps use: datasets (samples x features), model weights, image data


