#!/usr/bin/python3

"""
Standard Modules - Educational Examples

Demonstrates Python's built-in standard library modules essential for MLOps:
- File system operations
- System interaction
- Logging and monitoring
- Configuration management
- Process execution
"""

# ============================================================================
# OS MODULE - Operating system interface
# ============================================================================

import os
# Access environment variables - common for MLOps configuration
print(os.environ.get("HOME"))  # Get home directory
# Build cross-platform file paths
print(os.path.join("data", "train.csv"))  # Creates "data/train.csv" or "data\train.csv"
# MLOps use: environment config, file paths, system variables

# ============================================================================
# SYS MODULE - System-specific parameters and functions
# ============================================================================

import sys
# Access command line arguments passed to script
print(sys.argv)  # list of arguments passed to the script
# MLOps use: script parameters, configuration flags, debugging info

# ============================================================================
# PATHLIB MODULE - Object-oriented file system paths
# ============================================================================

from pathlib import Path
# Modern way to handle file paths
path = Path("data/train.csv")
print(path.exists())  # Check if file exists
# MLOps use: file validation, path manipulation, cross-platform compatibility

# ============================================================================
# LOGGING MODULE - Structured logging for applications
# ============================================================================

import logging
# Configure logging for MLOps monitoring
logging.basicConfig(level=logging.INFO)
logging.info("Training started")  # Log training events
# MLOps use: experiment tracking, error monitoring, audit trails

# ============================================================================
# JSON MODULE - JSON data serialization
# ============================================================================

import json
# Save/load configuration as JSON
config = {"lr": 0.01, "batch": 32}
with open("config.json", "w") as f:
    json.dump(config, f)  # Save config to file
# MLOps use: configuration files, experiment parameters, API communication

# ============================================================================
# SUBPROCESS MODULE - Execute external commands
# ============================================================================

import subprocess
# Run system commands from Python
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)  # Print command output
# MLOps use: run training scripts, execute data pipelines, system integration


