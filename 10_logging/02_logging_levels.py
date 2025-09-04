#!/usr/bin/python3

"""
Logging Levels for MLOps - Educational Examples

Demonstrates the five standard logging levels:
- DEBUG: Detailed diagnostic information
- INFO: General informational messages
- WARNING: Potential problems or issues
- ERROR: Serious problems that prevent functionality
- CRITICAL: Very serious errors that may stop the program
"""

import logging

# ============================================================================
# LOGGING LEVEL CONFIGURATION - Set minimum level to capture all messages
# ============================================================================

logging.basicConfig(level=logging.DEBUG)  # Capture all levels (DEBUG and above)
# Level hierarchy: DEBUG < INFO < WARNING < ERROR < CRITICAL
# Setting DEBUG level shows all messages for demonstration

# ============================================================================
# ALL LOGGING LEVELS - Different severity categories for MLOps
# ============================================================================

logging.debug("Loading configuration file")      # DEBUG: Detailed diagnostic info
# Use for: variable values, function entry/exit, detailed flow tracking
# MLOps: hyperparameter values, data shapes, model architecture details

logging.info("Pipeline started")                 # INFO: General information
# Use for: major milestones, successful operations, status updates
# MLOps: training started, epoch completed, model saved successfully

logging.warning("Dataset has missing values")     # WARNING: Potential problems
# Use for: recoverable issues, data quality concerns, deprecated features
# MLOps: missing data, low accuracy warnings, resource usage alerts

logging.error("Failed to open model file")       # ERROR: Serious problems
# Use for: exceptions, failed operations, broken functionality
# MLOps: file access errors, training failures, prediction errors

logging.critical("System crash – stopping pipeline")  # CRITICAL: System failure
# Use for: severe errors that stop the program, system-level failures
# MLOps: out of memory, corrupted models, infrastructure failures





