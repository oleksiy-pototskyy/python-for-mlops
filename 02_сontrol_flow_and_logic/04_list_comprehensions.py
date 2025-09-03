#!/usr/bin/python3

"""
Python List Comprehensions for MLOps - Educational Examples

Demonstrates comprehension patterns essential for:
- Data transformation and preprocessing
- Filtering and selection operations
- Metric calculations and conversions
- Efficient collection processing
"""

# ============================================================================
# TRADITIONAL LOOP vs LIST COMPREHENSION - Performance comparison
# ============================================================================

# Traditional approach - verbose and slower
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16]
# MLOps use: feature engineering, data preprocessing (traditional way)

# List comprehension - concise and faster
squares = [x**2 for x in range(5)]
# Syntax: [expression for item in iterable]
# MLOps use: efficient data transformations, feature scaling

# ============================================================================
# FILTERING WITH CONDITIONS - Selective data processing
# ============================================================================

# Filter even numbers - common pattern for data selection
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
# Syntax: [expression for item in iterable if condition]
# MLOps use: filter valid samples, select specific epochs, data quality checks

# Filter files by extension - practical MLOps example
files = ["train.csv", "test.json", "logs.txt", "validate.csv"]
csv_files = [f for f in files if f.endswith(".csv")]
print(csv_files)  # ['train.csv', 'validate.csv']
# MLOps use: filter dataset files, select model checkpoints, log processing

# ============================================================================
# DATA TRANSFORMATION - Converting and processing values
# ============================================================================

# Convert scores to percentages - metric transformation
scores = [0.83, 0.91, 0.77]
percentages = [round(s * 100, 1) for s in scores]
print(percentages)  # [83.0, 91.0, 77.0]
# MLOps use: metric conversions, normalization, feature scaling

# ============================================================================
# NESTED COMPREHENSIONS - Cartesian products and combinations
# ============================================================================

# Generate coordinate pairs - hyperparameter grid search pattern
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)  # [(0, 0), (0, 1), (1, 0), (1, 1)]
# Syntax: [expression for item1 in iterable1 for item2 in iterable2]
# MLOps use: hyperparameter combinations, grid search, cross-validation splits

# ============================================================================
# DICTIONARY COMPREHENSIONS - Key-value pair generation
# ============================================================================

# Create metrics dictionary - experiment tracking pattern
metrics = {"epoch_" + str(i): i*0.1 for i in range(3)}
print(metrics)  # {'epoch_0': 0.0, 'epoch_1': 0.1, 'epoch_2': 0.2}
# Syntax: {key_expression: value_expression for item in iterable}
# MLOps use: experiment logging, metric tracking, configuration mapping

