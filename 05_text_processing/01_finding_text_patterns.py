#!/usr/bin/python3

"""
Python Finding Text Patterns for MLOps - Educational Examples

Demonstrates text pattern matching essential for:
- Log analysis and error detection
- File type identification
- Configuration parsing
- Metric extraction from logs
"""

# ============================================================================
# SUBSTRING SEARCH - Basic pattern detection
# ============================================================================

# Check if substring exists in text
log = "ERROR: model training failed"
if "ERROR" in log:
    print("Found error in logs")
    # MLOps use: error detection, log filtering, alert triggering

# ============================================================================
# POSITION FINDING - Locate pattern position
# ============================================================================

# Find position of substring in text
message = "training completed at step 120"
pos = message.find("step")  # Returns index of first occurrence
print(pos)  # 23 - "step" starts at position 23
# find() returns -1 if not found
# MLOps use: parse structured logs, extract timestamps, locate metrics

# ============================================================================
# PREFIX/SUFFIX MATCHING - File type detection
# ============================================================================

# Check file extension using suffix matching
filename = "model.pkl"
if filename.endswith(".pkl"):
    print("Model artifact detected")
    # MLOps use: file type validation, model format detection, data filtering

# ============================================================================
# PATH ANALYSIS - Directory structure parsing
# ============================================================================

# Parse path components and check for specific directories
path = "data/train/images"
parts = path.split("/")  # Split path into components
if "train" in parts:
    print("Training dataset detected")
    # MLOps use: dataset identification, path validation, data organization

# ============================================================================
# PATTERN COUNTING - Frequency analysis
# ============================================================================

# Count occurrences of pattern in text
log = "warning, warning, error"
print(log.count("warning"))  # 2 - counts non-overlapping occurrences
# MLOps use: error frequency analysis, metric counting, log statistics

# ============================================================================
# VALUE EXTRACTION - Parse structured data
# ============================================================================

# Extract value after specific pattern
line = "epoch=5, loss=0.134"
start = line.find("loss=") + len("loss=")  # Find start of value
loss_value = line[start:]  # Extract everything after "loss="
print(loss_value)  # 0.134
# MLOps use: metric extraction, config parsing, log value retrieval

