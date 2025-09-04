#!/usr/bin/python3

"""
Environment Variables for MLOps - Educational Examples

Demonstrates environment variable usage essential for MLOps:
- Reading environment variables
- Default values for missing variables
- Setting environment variables
- Loading variables from .env files
- Secure configuration management
"""

import os

# ============================================================================
# READING ENVIRONMENT VARIABLES - Access system configuration
# ============================================================================

db_user = os.getenv("DB_USER")  # Get environment variable value
db_pass = os.getenv("DB_PASS")  # Returns None if variable doesn't exist

print("Database user:", db_user)
# MLOps use: database credentials, API endpoints, service URLs
# Keeps sensitive data out of source code

# ============================================================================
# DEFAULT VALUES - Provide fallbacks for missing variables
# ============================================================================

timeout = os.getenv("TIMEOUT", "30")  # Use "30" if TIMEOUT not set
print("Timeout is:", timeout)
# Second parameter provides default value if environment variable missing
# MLOps use: configuration with sensible defaults, optional parameters

# ============================================================================
# SETTING ENVIRONMENT VARIABLES - Modify runtime environment
# ============================================================================

os.environ["MODEL_PATH"] = "/mnt/models/latest.pkl"
# Set environment variable for current process and child processes
# MLOps use: dynamic configuration, passing paths to subprocesses

# ============================================================================
# LOADING FROM .env FILES - Manage development configurations
# ============================================================================

from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file in current directory
api_key = os.getenv("API_KEY")  # Now can access variables from .env file
print("API Key:", api_key)
# MLOps use: development environments, local testing, team configurations

# ============================================================================
# .env FILE FORMAT - Configuration file structure
# ============================================================================

# Example of .env file content:
# API_KEY=12345
# DB_USER=mlops
# DB_PASS=secret
# Format: VARIABLE_NAME=value (no spaces around =)
# MLOps use: store secrets locally, environment-specific configs