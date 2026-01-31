#!/usr/bin/python3

"""
Exploring and Inspecting DataFrames for MLOps - Educational Examples

Demonstrates DataFrame inspection methods essential for MLOps:
- Data preview and structure examination
- Data type and memory usage analysis
- Quick data quality assessment
- Initial data exploration workflow
"""

import pandas as pd

# ============================================================================
# SAMPLE DATA CREATION - Create DataFrame for exploration
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [25, 30, 35, 28, 32, 45],
    "salary": [50000, 60000, 70000, 55000, 65000, 80000],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT"]
}

df = pd.DataFrame(data)
# Expanded dataset for comprehensive inspection examples
# MLOps use: any dataset loaded for analysis and preprocessing

# ============================================================================
# DATA PREVIEW - Quick look at DataFrame structure and content
# ============================================================================

print("First 5 rows (default):")
print(df.head())
# Shows first 5 rows by default

print("\nFirst 3 rows:")
print(df.head(3))
# Pass number for specific row count

print("\nLast 3 rows:")
print(df.tail(3))
# Shows last rows of DataFrame
# MLOps use: quick data inspection, verify data loading, check structure

# ============================================================================
# DATASET SHAPE - Quick size check
# ============================================================================

print(f"\nDataset shape: {df.shape}")
# Returns tuple (rows, columns)
# MLOps use: understand dataset size, memory planning

# ============================================================================
# DATA INFORMATION - Comprehensive DataFrame metadata
# ============================================================================

print("\nDataFrame info:")
print(df.info())
# Shows column names, data types, non-null counts, memory usage
# MLOps use: data quality assessment, type validation, missing data detection

# ============================================================================
# STATISTICAL SUMMARY - Numeric column statistics
# ============================================================================

print("\nStatistical summary:")
print(df.describe())
# Shows count, mean, std, min, 25%, 50%, 75%, max for numeric columns
# MLOps use: detect outliers, understand data distribution, data validation

# ============================================================================
# COLUMN INSPECTION - Names and data types
# ============================================================================

print("\nColumn names:")
print(df.columns.tolist())
# Shows all column names as list

print("\nData types:")
print(df.dtypes)
# Shows data type for each column
# MLOps use: verify correct data types, identify type conversion needs

# ============================================================================
# CATEGORICAL DATA EXPLORATION - Value counts for categories
# ============================================================================

print("\nDepartment value counts:")
print(df['department'].value_counts())
# Shows frequency of each unique value in categorical column
# MLOps use: understand class distribution, detect imbalanced data