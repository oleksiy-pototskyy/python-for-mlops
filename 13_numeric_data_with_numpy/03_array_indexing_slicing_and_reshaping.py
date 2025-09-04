#!/usr/bin/python3

"""
Array Indexing, Slicing, and Reshaping for MLOps - Educational Examples

Demonstrates NumPy array access and manipulation:
- Basic indexing for element access
- Slicing for extracting subarrays
- Multi-dimensional array indexing
- Array reshaping and flattening
- Automatic dimension inference
"""

import numpy as np

# ============================================================================
# BASIC INDEXING - Access individual elements
# ============================================================================

arr = np.array([10, 20, 30, 40, 50])  # 1D array
print(arr[0])   # first element: 10
print(arr[-1])  # last element: 50 (negative indexing from end)
# Zero-based indexing like Python lists
# MLOps use: access specific predictions, feature values, model parameters

# ============================================================================
# ARRAY SLICING - Extract subarrays
# ============================================================================

print(arr[1:4])   # elements from index 1 up to 3: [20 30 40]
print(arr[:3])    # first three elements: [10 20 30]
print(arr[2:])    # from index 2 to the end: [30 40 50]
# Slicing syntax: [start:stop] (stop is exclusive)
# MLOps use: extract data batches, feature subsets, time windows

# ============================================================================
# MULTI-DIMENSIONAL INDEXING - Access matrix elements
# ============================================================================

matrix = np.array([[1, 2, 3],    # 3x3 matrix
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[0, 1])    # element at row 0, column 1: 2
print(matrix[1, :])    # full row at index 1: [4 5 6]
print(matrix[:, 2])    # full column at index 2: [3 6 9]
# Syntax: [row, column] or [row, :] for full row, [:, column] for full column
# MLOps use: access dataset samples, feature columns, model weight matrices

# ============================================================================
# ARRAY RESHAPING - Change array dimensions
# ============================================================================

arr = np.arange(12)           # Create [0, 1, 2, ..., 11]
reshaped = arr.reshape((3, 4))  # Reshape to 3x4 matrix
print(reshaped)
# Output: [[ 0  1  2  3]
#          [ 4  5  6  7]
#          [ 8  9 10 11]]
# Total elements must remain the same (12 = 3 × 4)
# MLOps use: reshape data for model input, convert between tensor dimensions

# ============================================================================
# ARRAY FLATTENING - Convert to 1D array
# ============================================================================

print(reshaped.ravel())  # Flatten to 1D: [ 0  1  2  3  4  5  6  7  8  9 10 11]
# ravel() returns flattened view of the array
# MLOps use: flatten image data, convert matrices to vectors for processing

# ============================================================================
# AUTOMATIC DIMENSION INFERENCE - Let NumPy calculate dimensions
# ============================================================================

arr = np.arange(16)           # Create [0, 1, 2, ..., 15]
reshaped = arr.reshape((4, -1))  # 4 rows, auto-calculate columns
print(reshaped)
# Output: [[ 0  1  2  3]
#          [ 4  5  6  7]
#          [ 8  9 10 11]
#          [12 13 14 15]]
# -1 means "calculate this dimension automatically" (16 ÷ 4 = 4 columns)
# MLOps use: flexible reshaping when one dimension is known


