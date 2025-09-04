#!/usr/bin/python3

"""
Creating and Manipulating Arrays for MLOps - Educational Examples

Demonstrates NumPy array operations essential for MLOps:
- Array creation methods
- Specialized array generation functions
- Array reshaping and transformation
- Array concatenation and stacking
- Element modification and operations
"""

import numpy as np

# ============================================================================
# BASIC ARRAY CREATION - From Python lists
# ============================================================================

arr = np.array([1, 2, 3, 4, 5])  # Create array from list
print(arr)  # Output: [1 2 3 4 5]
# Most common way to create arrays from existing data
# MLOps use: convert Python lists to NumPy for processing

# ============================================================================
# SPECIALIZED ARRAY CREATION - Pre-filled arrays
# ============================================================================

zeros = np.zeros(5)        # Array of zeros, shape (5,)
ones = np.ones((2, 3))     # Array of ones, shape (2, 3)
print(zeros)  # Output: [0. 0. 0. 0. 0.]
print(ones)   # Output: [[1. 1. 1.] [1. 1. 1.]]
# MLOps use: initialize weights, create masks, placeholder arrays

# ============================================================================
# RANGE AND SEQUENCE ARRAYS - Generated sequences
# ============================================================================

range_arr = np.arange(0, 10, 2)  # Start, stop, step: [0, 2, 4, 6, 8]
lin_arr = np.linspace(0, 1, 5)   # 5 evenly spaced values from 0 to 1
print(range_arr)  # Output: [0 2 4 6 8]
print(lin_arr)    # Output: [0.   0.25 0.5  0.75 1.  ]
# MLOps use: create feature ranges, learning rate schedules, time series

# ============================================================================
# ARRAY RESHAPING - Change array dimensions
# ============================================================================

arr = np.arange(6)           # Create [0, 1, 2, 3, 4, 5]
reshaped = arr.reshape((2, 3))  # Reshape to 2x3 matrix
print(reshaped)
# Output: [[0 1 2]
#          [3 4 5]]
# MLOps use: reshape data for model input, convert vectors to matrices

# ============================================================================
# ARRAY STACKING - Combine arrays
# ============================================================================

a = np.array([1, 2, 3])  # First array
b = np.array([4, 5, 6])  # Second array

vertical = np.vstack([a, b])    # Stack vertically (rows)
horizontal = np.hstack([a, b])  # Stack horizontally (columns)

print(vertical)
# Output: [[1 2 3]
#          [4 5 6]]
print(horizontal)  # Output: [1 2 3 4 5 6]
# MLOps use: combine datasets, concatenate features, batch processing

# ============================================================================
# ELEMENT MODIFICATION - Change individual elements
# ============================================================================

arr = np.array([10, 20, 30, 40])  # Original array
arr[2] = 99                       # Modify element at index 2
print(arr)  # Output: [10 20 99 40]
# Direct indexing for element access and modification
# MLOps use: data cleaning, outlier correction, feature engineering

# ============================================================================
# ARRAY OPERATIONS - Mathematical transformations
# ============================================================================

arr = np.array([1, 2, 3, 4])  # Original array
arr = arr * 10                # Multiply all elements by 10
print(arr)  # Output: [10 20 30 40]
# Vectorized operations apply to all elements simultaneously
# MLOps use: feature scaling, normalization, data preprocessing



