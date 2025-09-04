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
    "name": ["Alice", "Bob", "Charlie"],  # String column
    "age": [25, 30, 35]                   # Numeric column
}

df = pd.DataFrame(data)  # Create DataFrame from dictionary
# Sample dataset for demonstrating inspection methods
# MLOps use: any dataset loaded for analysis and preprocessing

# ============================================================================
# DATA PREVIEW - Quick look at DataFrame structure and content
# ============================================================================

print(df.head())  # Display first 5 rows (default)
# Output:
#      name  age
# 0   Alice   25
# 1     Bob   30
# 2 Charlie   35
# head() shows sample data with column names and row indices
# MLOps use: quick data inspection, verify data loading, check structure

# ============================================================================
# DATA INFORMATION - Comprehensive DataFrame metadata
# ============================================================================

print(df.info())  # Display DataFrame information summary
# Output includes:
# - DataFrame shape (rows x columns)
# - Column names and data types
# - Non-null value counts
# - Memory usage
# MLOps use: data quality assessment, memory planning, type validation



