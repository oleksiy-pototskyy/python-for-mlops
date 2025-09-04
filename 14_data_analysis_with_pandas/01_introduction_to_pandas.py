#!/usr/bin/python3

"""
Introduction to Pandas for MLOps - Educational Examples

Demonstrates Pandas fundamentals essential for MLOps:
- DataFrame creation from dictionaries
- Tabular data structure and display
- Boolean indexing for data filtering
- Data selection and querying
"""

import pandas as pd

# ============================================================================
# DATAFRAME CREATION - Building structured data from dictionaries
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie"],  # Column 1: names
    "age": [25, 30, 35]                   # Column 2: ages
}
# Dictionary structure: keys become column names, values become column data
# MLOps use: create datasets from Python data, experiment results, metrics

df = pd.DataFrame(data)  # Convert dictionary to DataFrame
print(df)
# Output:
#      name  age
# 0   Alice   25
# 1     Bob   30
# 2 Charlie   35
# DataFrame: 2D labeled data structure with rows and columns
# MLOps use: structured datasets, feature matrices, model results

# ============================================================================
# BOOLEAN INDEXING - Filter data based on conditions
# ============================================================================

print(df[df["age"] > 28])  # Select rows where age > 28
# Output:
#      name  age
# 1     Bob   30
# 2 Charlie   35
# Boolean indexing: df[condition] returns rows matching the condition
# MLOps use: filter training data, select validation samples, data quality checks



