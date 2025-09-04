#!/usr/bin/python3

"""
Raising Exceptions for MLOps - Educational Examples

Demonstrates how to raise exceptions in Python:
- Raising built-in exceptions
- Raising exceptions in functions
- Raising custom exceptions
- Re-raising caught exceptions
"""

# ============================================================================
# RAISING BUILT-IN EXCEPTIONS - Use standard Python exceptions
# ============================================================================

raise ValueError("Invalid input value")
# Explicitly raise built-in exception with custom message
# Syntax: raise ExceptionType("message")
# MLOps use: input validation, parameter checking, data format errors

# ============================================================================
# RAISING EXCEPTIONS IN FUNCTIONS - Validate inputs and conditions
# ============================================================================

def load_dataset(path):
    """Load dataset with input validation."""
    if not path:
        raise FileNotFoundError("Dataset path is missing")
        # Raise exception when preconditions not met
    # Continue with normal execution if validation passes
    # MLOps use: validate file paths, check data availability

# ============================================================================
# RAISING CUSTOM EXCEPTIONS - Use domain-specific error types
# ============================================================================

class TrainingError(Exception):
    """Custom exception for training-related errors."""
    pass

def train_model(data):
    """Train model with data validation."""
    if len(data) == 0:
        raise TrainingError("Training data is empty")
        # Raise custom exception for domain-specific errors
    # Continue with training if data is valid
    # MLOps use: training validation, model-specific errors

# ============================================================================
# RE-RAISING EXCEPTIONS - Log and propagate errors
# ============================================================================

try:
    result = 1 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError as e:
    print("Log the error:", e)  # Log error for debugging
    raise  # Re-raise the same exception to stop execution
    # 'raise' without arguments re-raises the caught exception
    # MLOps use: log errors while still failing fast, error monitoring


