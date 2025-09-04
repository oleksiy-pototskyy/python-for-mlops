#!/usr/bin/python3

"""
Quick Visualization with Pandas for MLOps - Educational Examples

Demonstrates Pandas built-in plotting for MLOps data exploration:
- Histogram plots for distribution analysis
- Line plots for time series and trends
- Bar plots for categorical data frequency
- Scatter plots for relationship analysis
"""

import pandas as pd

# ============================================================================
# SAMPLE DATA CREATION - DataFrame for visualization examples
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie"],  # Categorical data
    "age": [25, 30, 35]                   # Numeric data for plotting
}

df = pd.DataFrame(data)  # Create sample DataFrame
# Sample dataset for demonstrating built-in plotting capabilities
# MLOps use: any dataset requiring quick visual exploration

# ============================================================================
# HISTOGRAM PLOT - Distribution analysis of numeric data
# ============================================================================

df["age"].plot(kind="hist")  # Create histogram of age distribution
# kind="hist": histogram shows frequency distribution of values
# Useful for understanding data distribution and identifying outliers
# MLOps use: analyze feature distributions, detect skewness, identify outliers

# ============================================================================
# LINE PLOT - Time series and trend analysis
# ============================================================================

df["sales"].plot(kind="line")  # Create line plot of sales over time
# kind="line": connects data points to show trends and patterns
# Ideal for time series data and sequential measurements
# MLOps use: model performance over time, training metrics, data trends

# ============================================================================
# BAR PLOT - Categorical data frequency analysis
# ============================================================================

df["city"].value_counts().plot(kind="bar")  # Bar chart of city frequencies
# value_counts() counts occurrences of each unique value
# kind="bar": vertical bars show frequency of categorical values
# MLOps use: class distribution, categorical feature analysis, label balance

# ============================================================================
# SCATTER PLOT - Relationship analysis between two variables
# ============================================================================

df.plot(x="age", y="income", kind="scatter")  # Scatter plot of age vs income
# kind="scatter": shows relationship between two numeric variables
# Each point represents one data sample with x,y coordinates
# MLOps use: feature correlation, relationship exploration, outlier detection


