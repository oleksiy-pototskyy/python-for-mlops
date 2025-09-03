#!/usr/bin/python3

"""
Python Function Definition Syntax for MLOps - Educational Examples

Demonstrates function patterns essential for:
- Modular code organization
- Reusable ML operations
- Parameter handling and configuration
- Clean API design
"""

# ============================================================================
# BASIC FUNCTION SYNTAX - Foundation pattern
# ============================================================================

def function_name(parameters):
    """Basic function structure."""
    # code block
    return value
# Syntax: def function_name(parameters): body with optional return
# MLOps use: encapsulate operations, create reusable components

# ============================================================================
# FUNCTIONS WITH PARAMETERS - Input handling
# ============================================================================

def load_dataset(path):
    """Load dataset from file path."""
    print(f"Loading dataset from {path}")
    return open(path).readlines()
    # MLOps use: data loading, file processing, model loading

# ============================================================================
# MULTIPLE PARAMETERS - Complex operations
# ============================================================================

def train_model(epochs, learning_rate):
    """Train model with specified parameters."""
    print(f"Training for {epochs} epochs with lr={learning_rate}")
    # MLOps use: model training, hyperparameter configuration

# Function call - passing arguments by position
train_model(5, 0.001)
# Arguments passed in order: epochs=5, learning_rate=0.001

# ============================================================================
# DEFAULT PARAMETERS - Optional configuration
# ============================================================================

def connect_db(host="localhost", port=5432):
    """Connect to database with default values."""
    print(f"Connecting to {host}:{port}")
    # MLOps use: database connections, API endpoints, model configs

# Function calls with defaults
connect_db()                # uses defaults: localhost:5432
connect_db("mlops-db", 5433)  # overrides both defaults
# Default parameters allow flexible function usage

# ============================================================================
# KEYWORD ARGUMENTS - Flexible parameter passing
# ============================================================================

def log_metrics(**kwargs):
    """Log arbitrary metrics using keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # **kwargs accepts any number of keyword arguments as dictionary
    # MLOps use: flexible metric logging, configuration handling

# Call with any number of named arguments
log_metrics(loss=0.15, accuracy=0.92)
# Creates kwargs = {"loss": 0.15, "accuracy": 0.92}

# ============================================================================
# FUNCTIONS WITHOUT RETURN - Side effects only
# ============================================================================

def say_hello():
    """Function that performs action but returns nothing."""
    print("Hello")
    # No explicit return statement

# Functions without return automatically return None
result = say_hello()  # Prints "Hello"
print(result)  # None
# MLOps use: logging, printing, file operations, side effects



