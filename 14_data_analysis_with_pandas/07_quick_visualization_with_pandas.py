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
import matplotlib.pyplot as plt

# ============================================================================
# SAMPLE DATA CREATION - DataFrame for visualization examples
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"],
    "age": [25, 30, 35, 28, 32, 45, 29, 38],
    "sales": [100, 150, 200, 120, 180, 250, 130, 190],
    "city": ["NYC", "LA", "NYC", "Chicago", "LA", "NYC", "Chicago", "LA"],
    "income": [50000, 60000, 70000, 55000, 65000, 80000, 52000, 68000]
}

df = pd.DataFrame(data)
# Complete dataset with all columns needed for visualization examples
# MLOps use: any dataset requiring quick visual exploration

# ============================================================================
# HISTOGRAM PLOT - Distribution analysis of numeric data
# ============================================================================

df["age"].plot(kind="hist")  # Create histogram of age distribution
plt.show()
# kind="hist": histogram shows frequency distribution of values
# Useful for understanding data distribution and identifying outliers
# MLOps use: analyze feature distributions, detect skewness, identify outliers

# ============================================================================
# LINE PLOT - Time series and trend analysis
# ============================================================================

df["sales"].plot(kind="line")  # Create line plot of sales over time
plt.show()
# kind="line": connects data points to show trends and patterns
# Ideal for time series data and sequential measurements
# MLOps use: model performance over time, training metrics, data trends

# ============================================================================
# BAR PLOT - Categorical data frequency analysis
# ============================================================================

df["city"].value_counts().plot(kind="bar")  # Bar chart of city frequencies
plt.show()
# value_counts() counts occurrences of each unique value
# kind="bar": vertical bars show frequency of categorical values
# MLOps use: class distribution, categorical feature analysis, label balance

# ============================================================================
# SCATTER PLOT - Relationship analysis between two variables
# ============================================================================

df.plot(x="age", y="income", kind="scatter")  # Scatter plot of age vs income
plt.show()
# kind="scatter": shows relationship between two numeric variables
# Each point represents one data sample with x,y coordinates
# MLOps use: feature correlation, relationship exploration, outlier detection


