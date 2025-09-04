#!/usr/bin/python3

"""
Introduction to Serialization for MLOps - Educational Examples

Demonstrates serialization fundamentals:
- Converting Python objects to storable format (serialization)
- Converting stored format back to Python objects (deserialization)
- Persistent storage and data exchange
- JSON as a common serialization format
"""

import json

# ============================================================================
# PYTHON OBJECT - In-memory data structure
# ============================================================================

data = {"experiment": 1, "accuracy": 0.92}  # Python dictionary in memory
# MLOps use: experiment results, model metrics, configuration parameters
# Problem: exists only in memory, lost when program ends

# ============================================================================
# SERIALIZATION - Convert Python object to storable format
# ============================================================================

# Serialize to JSON string
json_string = json.dumps(data)  # Convert dict to JSON string
# json.dumps() = "dump string" - serialize to string format
# Result: '{"experiment": 1, "accuracy": 0.92}'
# MLOps use: prepare data for storage, API communication, logging

# ============================================================================
# PERSISTENT STORAGE - Save serialized data to file
# ============================================================================

# Save to file
with open("result.json", "w") as f:
    f.write(json_string)  # Write JSON string to file
    # Data now persists on disk, survives program termination
    # MLOps use: save experiment results, model metadata, configurations

# ============================================================================
# DESERIALIZATION - Convert stored format back to Python object
# ============================================================================

# Load back from file
with open("result.json", "r") as f:
    loaded = json.load(f)  # Read file and convert JSON back to Python dict
    # json.load() reads from file and deserializes in one step
    # Result: Python dictionary identical to original

print(loaded)  # {'experiment': 1, 'accuracy': 0.92}
# MLOps use: load saved results, restore configurations, share data between systems





