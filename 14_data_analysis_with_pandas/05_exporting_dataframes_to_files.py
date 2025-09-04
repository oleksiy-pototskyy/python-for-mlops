#!/usr/bin/python3

"""
Exporting DataFrames to Files for MLOps - Educational Examples

Demonstrates Pandas export methods essential for MLOps:
- CSV export for universal compatibility
- Excel export for business reporting
- JSON export for web APIs and configuration
- Parquet export for efficient storage
- Encoding options for international data
"""

import pandas as pd

# ============================================================================
# SAMPLE DATA CREATION - DataFrame for export demonstrations
# ============================================================================

data = {
    "name": ["Alice", "Bob", "Charlie"],  # String column
    "age": [25, 30, 35]                   # Numeric column
}

df = pd.DataFrame(data)  # Create sample DataFrame
# Sample dataset for demonstrating various export formats
# MLOps use: processed datasets, model results, feature matrices

# ============================================================================
# CSV EXPORT - Universal text format for data exchange
# ============================================================================

df.to_csv("output.csv", index=False)  # Export to CSV without row indices
# index=False: exclude row numbers from output file
# CSV: comma-separated values, readable by most tools
# MLOps use: share datasets, export training data, model predictions

# ============================================================================
# EXCEL EXPORT - Spreadsheet format for business users
# ============================================================================

df.to_excel("output.xlsx", index=False)  # Export to Excel format
# Creates .xlsx file compatible with Microsoft Excel
# MLOps use: business reports, stakeholder presentations, data summaries

# ============================================================================
# JSON EXPORT - Structured format for APIs and configuration
# ============================================================================

df.to_json("output.json", orient="records", lines=True)  # Export to JSON Lines
# orient="records": each row as separate JSON object
# lines=True: one JSON object per line (JSONL format)
# MLOps use: API responses, configuration files, model metadata

# ============================================================================
# PARQUET EXPORT - Efficient columnar storage format
# ============================================================================

df.to_parquet("output.parquet")  # Export to Parquet format
# Parquet: compressed columnar format, preserves data types
# MLOps use: large datasets, data lakes, efficient storage and retrieval

# ============================================================================
# ENCODING OPTIONS - Handle international characters
# ============================================================================

df.to_csv("output.csv", index=False, encoding="utf-8")  # Specify UTF-8 encoding
# encoding="utf-8": support international characters and symbols
# MLOps use: multilingual datasets, global applications, text data with accents


