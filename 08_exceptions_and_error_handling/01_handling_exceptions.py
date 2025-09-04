#!/usr/bin/python3

"""
Handling Exceptions (try/except/else/finally) for MLOps - Educational Examples

Demonstrates exception handling patterns essential for:
- Robust error handling in ML pipelines
- Graceful failure recovery
- Resource cleanup and management
- Production-ready MLOps code
"""

# ============================================================================
# BASIC TRY/EXCEPT - Handle specific exceptions
# ============================================================================

try:
    # Code that may fail - risky operations
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("You cannot divide by zero")
    # Handle specific exception type
    # MLOps use: division by zero in metrics, loss calculations

# ============================================================================
# MULTIPLE EXCEPT BLOCKS - Handle different exception types
# ============================================================================

try:
    # Attempt to read dataset file
    with open("data.csv") as f:
        data = f.read()
except FileNotFoundError:
    print("File is missing")
    # Handle missing dataset files
except PermissionError:
    print("No permission to read this file")
    # Handle access permission issues
    # MLOps use: dataset loading, model file access, log file operations

# ============================================================================
# TRY/EXCEPT/ELSE - Execute code only if no exceptions occurred
# ============================================================================

try:
    # Attempt data conversion
    value = int("42")  # This will succeed
except ValueError:
    print("Not a number")
    # Handle conversion errors
else:
    print("Conversion successful:", value)
    # Execute only if try block succeeded (no exceptions)
    # MLOps use: process data only if validation passes

# ============================================================================
# TRY/EXCEPT/FINALLY - Always execute cleanup code
# ============================================================================

try:
    # Open resource that needs cleanup
    conn = open("temp.log", "w")
    conn.write("log entry")
except OSError as e:
    print("File error:", e)
    # Handle file operation errors
    # 'as e' captures exception object for detailed error info
finally:
    conn.close()  # Always executed, even if exception occurs
    print("Connection closed")
    # MLOps use: cleanup database connections, close model files, release GPU memory



