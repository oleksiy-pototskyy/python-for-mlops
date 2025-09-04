#!/usr/bin/python3

"""
Class Definition Syntax for MLOps - Educational Examples

Demonstrates Python class definition syntax:
- Empty class definition
- Constructor (__init__) method
- Instance attributes
- Instance methods
"""

# ============================================================================
# EMPTY CLASS - Minimal class definition
# ============================================================================

class Dataset:
    """Empty class - placeholder for future implementation."""
    pass  # Placeholder - class body cannot be empty
    # MLOps use: initial class structure, abstract base classes

# Create instance of empty class
train = Dataset()  # Calls default constructor (no arguments)
print(type(train))  # <class '__main__.Dataset'> - shows object type
# Even empty classes can be instantiated

# ============================================================================
# CLASS WITH CONSTRUCTOR - Initialize instance attributes
# ============================================================================

class Dataset:
    """Dataset class with constructor for initialization."""
    def __init__(self, path):
        """Constructor method - called when creating new instance."""
        self.path = path  # Instance attribute - unique to each object
        # self refers to the current instance being created
        # MLOps use: initialize model parameters, dataset paths, configurations

# Create instance with constructor argument
train = Dataset("train.csv")  # Passes "train.csv" to __init__
print(train.path)  # train.csv - access instance attribute
# Each instance has its own copy of attributes

# ============================================================================
# CLASS WITH METHODS - Add behavior to objects
# ============================================================================

class Dataset:
    """Complete dataset class with constructor and methods."""
    def __init__(self, path):
        """Initialize dataset with file path."""
        self.path = path  # Store path as instance attribute

    def load(self):
        """Instance method - defines object behavior."""
        print(f"Loading data from {self.path}")
        # Methods can access instance attributes through self
        # MLOps use: train(), predict(), evaluate(), save() operations

# Create instance and call method
train = Dataset("train.csv")  # Initialize with path
train.load()  # Call method on instance
# Method automatically receives 'self' as first argument


