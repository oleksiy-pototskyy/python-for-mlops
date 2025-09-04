#!/usr/bin/python3

"""
Config & Structured Data (INI/TOML/YAML) for MLOps - Educational Examples

Demonstrates configuration file formats essential for MLOps:
- INI files for simple key-value configurations
- TOML files for modern structured configuration
- YAML files for human-readable hierarchical data
- Reading and parsing different config formats
"""

# ============================================================================
# INI FILE FORMAT - Simple section-based configuration
# ============================================================================

# Example config.ini file content:
# [database]
# user = admin
# password = secret

import configparser
config = configparser.ConfigParser()  # Create INI parser
config.read("config.ini")              # Read INI file
print(config["database"]["user"])      # Access: section["key"]
# INI format: sections in brackets, key=value pairs
# MLOps use: simple app configs, database settings, basic parameters

# ============================================================================
# TOML FILE FORMAT - Modern configuration with data types
# ============================================================================

# Example config.toml file content:
# [server]
# host = "localhost"
# port = 8080

import tomllib  # from Python 3.11+
with open("config.toml", "rb") as f:   # Open in binary mode
    data = tomllib.load(f)             # Parse TOML to Python dict
print(data["server"]["host"])         # Access nested data
# TOML format: supports data types, arrays, nested structures
# MLOps use: complex configurations, tool configs (pyproject.toml)

# ============================================================================
# YAML FILE FORMAT - Human-readable hierarchical configuration
# ============================================================================

# Example config.yaml file content:
# database:
#   user: admin
#   password: secret

import yaml
with open("config.yaml", "r") as f:   # Open in text mode
    data = yaml.safe_load(f)           # Parse YAML to Python dict
print(data["database"]["user"])       # Access nested dictionary
# YAML format: indentation-based, supports complex data structures
# MLOps use: ML pipelines, Kubernetes configs, experiment parameters



