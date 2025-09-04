#!/usr/bin/python3

"""
Python Regular Expressions for MLOps - Educational Examples

Demonstrates regex patterns essential for:
- Log parsing and metric extraction
- File validation and pattern matching
- Structured data extraction
- ID and timestamp parsing
"""

import re

# ============================================================================
# BASIC PATTERN SEARCH - Find first match
# ============================================================================

# Search for first number in text
line = "Epoch 5: loss=0.134"
match = re.search(r"\d+", line)  # \d+ matches one or more digits
if match:
    print(match.group())  # 5 - returns the matched text
    # MLOps use: extract epoch numbers, batch counts, iteration numbers

# ============================================================================
# FIND ALL MATCHES - Extract multiple patterns
# ============================================================================

# Find all decimal numbers in text
line = "loss=0.134 accuracy=0.92"
values = re.findall(r"\d+\.\d+", line)  # \d+\.\d+ matches decimal numbers
print(values)  # ['0.134', '0.92'] - returns list of all matches
# MLOps use: extract all metrics, performance values, hyperparameters

# ============================================================================
# PATTERN MATCHING - Validate format from start
# ============================================================================

# Validate filename format from beginning
filename = "model.pkl"
if re.match(r".+\.pkl$", filename):  # .+ any chars, \. literal dot, $ end
    print("Valid model artifact")
    # re.match() checks pattern from start of string
    # MLOps use: validate file formats, check naming conventions

# ============================================================================
# SPECIFIC PATTERN EXTRACTION - Complex ID formats
# ============================================================================

# Extract run ID with specific format
log = "Run ID: run_20250101_153045"
match = re.search(r"run_\d{8}_\d{6}", log)  # \d{n} matches exactly n digits
print(match.group())  # run_20250101_153045
# Pattern: "run_" + 8 digits + "_" + 6 digits
# MLOps use: extract experiment IDs, timestamps, version numbers

# ============================================================================
# CAPTURE GROUPS - Extract multiple parts
# ============================================================================

# Extract multiple values using parentheses groups
line = "epoch=5, loss=0.134"
match = re.search(r"epoch=(\d+), loss=(\d+\.\d+)", line)
print(match.groups())  # ('5', '0.134') - tuple of captured groups
# Parentheses () create capture groups for extracting specific parts
# MLOps use: parse structured logs, extract key-value pairs, config parsing


