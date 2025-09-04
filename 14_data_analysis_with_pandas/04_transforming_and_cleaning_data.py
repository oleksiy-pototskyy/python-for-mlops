#!/usr/bin/python3

"""
Transforming and Cleaning Data for MLOps - Educational Examples

Demonstrates Pandas data cleaning operations essential for MLOps:
- Handling missing values (NaN imputation)
- Data type conversions
- String data cleaning and normalization
- Column renaming for consistency
- Feature engineering and calculations
- Value replacement and mapping
"""

import pandas as pd

# ============================================================================
# SAMPLE DATA CREATION - Base DataFrame for transformation examples
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie"],  # String data
    "age": [25, 30, 35]                   # Numeric data
}

df = pd.DataFrame(data)  # Create sample DataFrame
# Base dataset for demonstrating cleaning operations
# MLOps use: any raw dataset requiring preprocessing

# ============================================================================
# MISSING VALUE IMPUTATION - Handle NaN values
# ============================================================================

df['age'] = df['age'].fillna(df['age'].mean())  # Fill missing ages with mean
# fillna() replaces NaN values with specified value or calculation
# mean() calculates average of non-null values
# MLOps use: impute missing features, handle incomplete training data

# ============================================================================
# DATA TYPE CONVERSION - Ensure correct data types
# ============================================================================

df['price'] = df['price'].astype(float)  # Convert price column to float
# astype() changes column data type
# Ensures numeric operations work correctly
# MLOps use: convert string numbers to numeric, ensure proper data types

# ============================================================================
# STRING DATA CLEANING - Normalize text data
# ============================================================================

df['name'] = df['name'].str.strip().str.lower()  # Remove whitespace and lowercase
# str.strip() removes leading/trailing whitespace
# str.lower() converts to lowercase for consistency
# MLOps use: clean text features, normalize categorical data

# ============================================================================
# COLUMN RENAMING - Standardize column names
# ============================================================================

df = df.rename(columns={"old_name": "new_name"})  # Rename columns
# rename() changes column names using dictionary mapping
# MLOps use: standardize feature names, improve readability

# ============================================================================
# FEATURE ENGINEERING - Create new calculated columns
# ============================================================================

df['total'] = df['quantity'] * df['price']  # Calculate total from existing columns
# Create new features from existing data
# MLOps use: derive features, create interaction terms, calculate metrics

# ============================================================================
# VALUE REPLACEMENT - Map categorical values
# ============================================================================

df['status'] = df['status'].replace({'ok': 'success', 'fail': 'error'})  # Map values
# replace() substitutes values using dictionary mapping
# MLOps use: standardize categorical labels, clean inconsistent values


