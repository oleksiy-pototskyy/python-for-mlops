#!/usr/bin/python3

"""
Applying Functions and Simple Data Validation for MLOps - Educational Examples

Demonstrates Pandas function application and validation essential for MLOps:
- Custom function application to columns
- Data transformation and mapping
- Missing value detection and counting
- Data quality validation checks
- Missing value handling strategies
"""

import pandas as pd

# ============================================================================
# SAMPLE DATA CREATION - DataFrame for function application examples
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie"],  # String data for transformation
    "age": [25, 30, 35]                   # Numeric data for validation
}

df = pd.DataFrame(data)  # Create sample DataFrame
# Sample dataset for demonstrating function application and validation
# MLOps use: any dataset requiring transformation and quality checks

# ============================================================================
# APPLY FUNCTION - Transform column values with custom functions
# ============================================================================

df["name"] = df["name"].apply(lambda x: x.lower())  # Convert names to lowercase
# apply() executes function on each element in the column
# lambda x: x.lower() creates anonymous function for lowercase conversion
# MLOps use: text preprocessing, feature normalization, data standardization

# ============================================================================
# MAP FUNCTION - Create categorical features from numeric data
# ============================================================================

df["age_group"] = df["age"].map(lambda x: "adult" if x >= 18 else "child")  # Categorize ages
# map() applies function and creates new column with transformed values
# Conditional logic creates categorical features from continuous data
# MLOps use: feature engineering, binning continuous variables, label creation

# ============================================================================
# MISSING VALUE DETECTION - Count null values for data quality assessment
# ============================================================================

df["age"].isnull().sum()  # Count missing values in age column
# isnull() returns boolean mask for missing values
# sum() counts True values (missing entries)
# MLOps use: data quality assessment, missing data analysis, preprocessing planning

# ============================================================================
# DATA VALIDATION - Check for invalid values
# ============================================================================

(df["age"] < 0).sum()  # Count negative age values (invalid)
# Boolean condition creates mask for invalid data
# sum() counts violations of business rules
# MLOps use: data validation, outlier detection, quality control

# ============================================================================
# MISSING VALUE IMPUTATION - Fill missing values with default
# ============================================================================

df["age"] = df["age"].fillna(0)  # Replace missing ages with 0
# fillna() replaces NaN values with specified value
# MLOps use: handle missing features, prepare data for models that can't handle NaN

# ============================================================================
# MISSING VALUE REMOVAL - Drop rows with missing data
# ============================================================================

df = df.dropna(subset=["age"])  # Remove rows where age is missing
# dropna() removes rows with NaN values in specified columns
# subset parameter limits removal to specific columns
# MLOps use: clean datasets, remove incomplete samples, ensure data completeness
