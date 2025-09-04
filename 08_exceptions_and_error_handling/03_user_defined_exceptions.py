#!/usr/bin/python3

"""
User-defined Exceptions for MLOps - Educational Examples

Demonstrates creating custom exceptions for MLOps workflows:
- Simple custom exceptions
- Exceptions with additional data
- Exception hierarchies for organized error handling
- Domain-specific error types
"""

# ============================================================================
# SIMPLE CUSTOM EXCEPTION - Basic exception class
# ============================================================================

class ConfigError(Exception):
    """Custom exception for configuration-related errors."""
    pass  # Inherits all functionality from Exception
    # MLOps use: configuration validation, parameter errors

# ============================================================================
# USING CUSTOM EXCEPTIONS - Raise domain-specific errors
# ============================================================================

def load_config(path):
    """Load configuration with custom error handling."""
    if not path.endswith(".yaml"):
        raise ConfigError("Configuration must be a YAML file")
        # Raise custom exception with descriptive message
    # load the file...
    # MLOps use: validate file formats, check configuration requirements

# ============================================================================
# EXCEPTION WITH ADDITIONAL DATA - Store extra error information
# ============================================================================

class DataValidationError(Exception):
    """Custom exception with additional error context."""
    def __init__(self, message, rows_failed=None):
        super().__init__(message)  # Call parent Exception constructor
        self.rows_failed = rows_failed  # Store additional error data
        # MLOps use: track failed samples, validation statistics

# ============================================================================
# USING EXCEPTIONS WITH DATA - Provide detailed error context
# ============================================================================

def validate_data(data):
    """Validate dataset with detailed error information."""
    if len(data) == 0:
        raise DataValidationError("Dataset is empty")
        # Could also include: rows_failed=[list of problematic rows]
    # MLOps use: data quality checks, preprocessing validation

# ============================================================================
# EXCEPTION HIERARCHY - Organized error handling structure
# ============================================================================

class PipelineError(Exception):
    """Base exception for all pipeline-related errors."""
    pass  # Parent class for all pipeline exceptions

class TrainingError(PipelineError):
    """Exception for training-specific errors."""
    pass  # Inherits from PipelineError

class DeploymentError(PipelineError):
    """Exception for deployment-specific errors."""
    pass  # Inherits from PipelineError

# Exception hierarchy allows catching at different levels:
# - catch PipelineError: handles all pipeline errors
# - catch TrainingError: handles only training errors
# - catch DeploymentError: handles only deployment errors
# MLOps use: organized error handling, different recovery strategies



