#!/usr/bin/python3

"""
Working with JSON for MLOps - Educational Examples

Demonstrates JSON operations essential for MLOps:
- Python to JSON serialization
- JSON string manipulation
- Direct file serialization
- File deserialization
- Data type handling in JSON
"""

import json

# ============================================================================
# PYTHON DATA STRUCTURE - Mixed data types for MLOps
# ============================================================================

data = {"experiment": 1, "accuracy": 0.95, "valid": True}
# Python dict with int, float, and boolean values
# MLOps use: experiment metadata, model performance, validation flags

# ============================================================================
# SERIALIZE TO JSON STRING - Convert Python object to JSON text
# ============================================================================

# Serialize to JSON string
json_string = json.dumps(data)  # Convert Python dict to JSON string
print(json_string)  # Output: {"experiment": 1, "accuracy": 0.95, "valid": true}
# Note: Python True becomes JSON true (lowercase)
# MLOps use: API responses, logging structured data, configuration export

# ============================================================================
# DIRECT FILE SERIALIZATION - Save Python object directly to JSON file
# ============================================================================

# Save JSON to file
with open("result.json", "w") as f:
    json.dump(data, f)  # Serialize and write to file in one step
    # json.dump() (no 's') writes directly to file
    # More efficient than dumps() + write() for file operations
    # MLOps use: save experiment results, export model metadata, backup configs

# ============================================================================
# FILE DESERIALIZATION - Load JSON file directly to Python object
# ============================================================================

# Load JSON back from file
with open("result.json", "r") as f:
    loaded = json.load(f)  # Read and deserialize from file in one step
    # json.load() (no 's') reads directly from file
    # Returns Python object identical to original

print(loaded)  # {'experiment': 1, 'accuracy': 0.95, 'valid': True}
# MLOps use: load experiment results, import configurations, restore metadata



