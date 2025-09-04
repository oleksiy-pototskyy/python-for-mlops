#!/usr/bin/python3

"""
Working with YAML for MLOps - Educational Examples

Demonstrates YAML operations essential for MLOps:
- Human-readable configuration format
- Python to YAML serialization
- YAML file operations
- Safe deserialization practices
- Configuration management
"""

import yaml  # Requires: pip install PyYAML

# ============================================================================
# CONFIGURATION DATA - Typical MLOps configuration structure
# ============================================================================

config = {
    "experiment": "test_01",     # Experiment identifier
    "batch_size": 32,            # Training batch size
    "learning_rate": 0.001,      # Model learning rate
    "use_gpu": True              # Hardware configuration
}
# MLOps use: hyperparameters, model configs, pipeline settings
# YAML advantage: more readable than JSON for complex configurations

# ============================================================================
# YAML SERIALIZATION - Write Python object to YAML file
# ============================================================================

# Write YAML to file
with open("config.yaml", "w") as f:
    yaml.dump(config, f)  # Serialize Python dict to YAML format
    # Creates human-readable YAML file with proper indentation
    # YAML output is cleaner and more readable than JSON
    # MLOps use: save experiment configs, model parameters, pipeline settings

# ============================================================================
# YAML DESERIALIZATION - Read YAML file back to Python object
# ============================================================================

# Read YAML back
with open("config.yaml", "r") as f:
    loaded = yaml.safe_load(f)  # Safely deserialize YAML to Python dict
    # safe_load() prevents execution of arbitrary Python code
    # More secure than yaml.load() for untrusted YAML files
    # Returns Python object identical to original

print(loaded)  # {'experiment': 'test_01', 'batch_size': 32, ...}
# MLOps use: load experiment configs, import model settings, restore parameters


