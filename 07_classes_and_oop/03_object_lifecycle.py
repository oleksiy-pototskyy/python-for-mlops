#!/usr/bin/python3

"""
Object Lifecycle (__init__, __del__) for MLOps - Educational Examples

Demonstrates object creation and destruction:
- __init__ method for object initialization
- __del__ method for cleanup (destructor)
- Object creation and deletion lifecycle
- Resource management patterns
"""

# ============================================================================
# OBJECT INITIALIZATION - __init__ method (constructor)
# ============================================================================

class Dataset:
    """Dataset class demonstrating object initialization."""
    def __init__(self, path):
        """Constructor - called when object is created."""
        self.path = path  # Initialize instance attributes
        print(f"Dataset created with path: {self.path}")
        # MLOps use: open files, allocate memory, initialize connections

# Object creation triggers __init__
train = Dataset("train.csv")  # Prints: "Dataset created with path: train.csv"
# __init__ automatically called during instantiation

# ============================================================================
# OBJECT DESTRUCTION - __del__ method (destructor)
# ============================================================================

class Dataset:
    """Dataset class with both constructor and destructor."""
    def __init__(self, path):
        """Initialize dataset - acquire resources."""
        self.path = path
        print("Opening dataset")  # Simulate resource acquisition
        # MLOps use: open files, database connections, GPU memory allocation

    def __del__(self):
        """Destructor - called when object is destroyed."""
        print("Cleaning up dataset")  # Simulate resource cleanup
        # MLOps use: close files, release memory, cleanup connections
        # Important: __del__ not guaranteed to be called immediately

# Object lifecycle demonstration
train = Dataset("train.csv")  # Prints: "Opening dataset"
del train  # Explicitly delete object, triggers __del__
# Prints: "Cleaning up dataset"
# Note: __del__ also called automatically when object goes out of scope

