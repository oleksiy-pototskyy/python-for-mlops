#!/usr/bin/python3

"""
Loading Data with Pandas for MLOps - Educational Examples

Demonstrates Pandas data loading patterns essential for MLOps:
- Basic CSV file loading
- Custom delimiters and headers
- Chunked reading for large datasets
- Memory-efficient data processing
"""

import pandas as pd

# ============================================================================
# BASIC CSV LOADING - Standard file reading
# ============================================================================

df = pd.read_csv("data.csv")  # Load CSV file into DataFrame
print(df.head())              # Display first 5 rows
# read_csv() automatically detects comma separators and uses first row as headers
# head() shows sample of data for quick inspection
# MLOps use: load training datasets, feature files, experiment results

# ============================================================================
# CUSTOM FILE FORMATS - Handle different delimiters and headers
# ============================================================================

df = pd.read_csv("data.txt", sep="\t", header=None)
# sep="\t": use tab separator instead of comma
# header=None: no header row, creates default column names (0, 1, 2, ...)
# MLOps use: load TSV files, custom formats, headerless data files

# ============================================================================
# CHUNKED READING - Process large files in memory-efficient chunks
# ============================================================================

for chunk in pd.read_csv("big_data.csv", chunksize=10000):
    process(chunk)  # Process each chunk separately
# chunksize=10000: read file in chunks of 10,000 rows
# Returns iterator of DataFrames instead of single large DataFrame
# MLOps use: process large datasets, streaming data, memory-constrained environments




