#!/usr/bin/python3

"""
Context Managers for MLOps - Educational Examples

Demonstrates context manager patterns essential for MLOps:
- Built-in context managers (file handling)
- Custom context managers with @contextmanager
- Resource management and cleanup
- Performance monitoring patterns
"""

# ============================================================================
# BUILT-IN CONTEXT MANAGER - File handling with automatic cleanup
# ============================================================================

with open("example.txt", "r") as f:
    content = f.read()  # Read file content
    print(content)      # Process content
    # File automatically closed when exiting 'with' block
    # Even if exception occurs, cleanup is guaranteed
    # MLOps use: safe file operations, dataset loading, model saving

# ============================================================================
# CUSTOM CONTEXT MANAGER - Performance monitoring decorator
# ============================================================================

from contextlib import contextmanager
import time

@contextmanager
def log_time(name):
    """Context manager to measure and log execution time."""
    start = time.time()  # Setup: record start time
    yield                # Yield control to 'with' block
    end = time.time()    # Cleanup: record end time and log duration
    print(f"{name} took {end - start:.2f} seconds")
    # MLOps use: performance monitoring, training time tracking

# ============================================================================
# USING CUSTOM CONTEXT MANAGER - Automatic timing and logging
# ============================================================================

# Usage of custom context manager
with log_time("data processing"):
    # Code block to be timed
    result = sum([i for i in range(1000000)])  # Heavy operation
    # Context manager automatically logs execution time
    # MLOps use: time model training, data preprocessing, inference

