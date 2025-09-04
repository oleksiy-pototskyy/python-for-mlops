#!/usr/bin/python3

"""
Basic Logging for MLOps - Educational Examples

Demonstrates Python logging essentials for MLOps:
- Basic logging configuration
- Different log levels (info, warning, error)
- Custom log formatting
- Structured logging for monitoring
"""

import logging

# ============================================================================
# BASIC LOGGING SETUP - Simple configuration for immediate use
# ============================================================================

logging.basicConfig(level=logging.INFO)  # Set minimum log level to INFO
# Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
# Only messages at INFO level and above will be displayed

# ============================================================================
# LOGGING DIFFERENT LEVELS - Categorize messages by severity
# ============================================================================

logging.info("Pipeline started")          # Informational message
logging.warning("Missing value in dataset") # Warning - potential issue
logging.error("Model file not found")      # Error - something went wrong
# MLOps use: track pipeline progress, data issues, model problems

# ============================================================================
# CUSTOM LOG FORMATTING - Structured log output with timestamps
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"  # Custom format string
)
# %(asctime)s: timestamp when log was created
# %(levelname)s: log level (INFO, WARNING, ERROR, etc.)
# %(message)s: the actual log message
# MLOps use: structured logs for monitoring, debugging, audit trails


