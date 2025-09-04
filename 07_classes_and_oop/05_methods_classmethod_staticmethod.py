#!/usr/bin/python3

"""
Methods & @classmethod / @staticmethod for MLOps - Educational Examples

Demonstrates different types of methods in Python classes:
- Instance methods (work with specific object instances)
- Class methods (work with the class itself)
- Static methods (utility functions grouped with class)
"""

# ============================================================================
# INSTANCE METHODS - Work with specific object instances
# ============================================================================

class Dataset:
    """Dataset class with instance methods."""
    def __init__(self, path):
        self.path = path  # Instance attribute

    def load(self):
        """Instance method - operates on specific dataset instance."""
        print(f"Loading data from {self.path}")
        # Has access to instance attributes via 'self'
        # MLOps use: train(), predict(), save() - operations on specific models

# Instance methods called on specific objects
# train = Dataset("train.csv")
# train.load()  # Operates on this specific dataset instance

# ============================================================================
# CLASS METHODS - Work with the class itself, not instances
# ============================================================================

class Dataset:
    """Dataset class with class method."""
    version = "1.0"  # Class attribute - shared by all instances

    @classmethod
    def info(cls):
        """Class method - operates on the class, not instance."""
        print(f"Dataset class version {cls.version}")
        # Receives 'cls' (class) instead of 'self' (instance)
        # Has access to class attributes and can create new instances
        # MLOps use: factory methods, class configuration, metadata

# Class methods called on the class itself
Dataset.info()  # Called on class, not instance
# Output: "Dataset class version 1.0"
# No need to create instance first

# ============================================================================
# STATIC METHODS - Utility functions grouped with class
# ============================================================================

class Metrics:
    """Utility class with static methods for ML metrics."""
    @staticmethod
    def accuracy(y_true, y_pred):
        """Static method - pure function, no access to class or instance."""
        return sum(y_true == y_pred) / len(y_true)
        # No 'self' or 'cls' parameter - just a regular function
        # Grouped with class for organization, but independent
        # MLOps use: utility functions, mathematical operations, validators

# Static methods called on class (or instance, but typically on class)
print(Metrics.accuracy([1,0,1],[1,1,1]))  # Called on class
# Output: 0.6666666666666666
# Could also be called on instance, but usually called on class



