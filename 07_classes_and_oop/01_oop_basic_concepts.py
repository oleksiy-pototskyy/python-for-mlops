#!/usr/bin/python3

"""
OOP Basic Concepts for MLOps - Educational Examples

Demonstrates object-oriented programming fundamentals:
- Classes and objects (instances)
- Constructors and attributes
- Methods and behavior
- Inheritance and polymorphism
"""

# ============================================================================
# CLASS DEFINITION - Blueprint for objects
# ============================================================================

class Dataset:
    """Basic dataset class - template for dataset objects."""
    def __init__(self, path):
        """Constructor - initializes new Dataset instance."""
        self.path = path  # Instance attribute - each object has its own path
        # MLOps use: model classes, data loaders, experiment trackers

# ============================================================================
# OBJECT CREATION - Instantiating classes
# ============================================================================

# Create object (instance) from class
train = Dataset("train.csv")  # Calls __init__ with "train.csv"
print(train.path)  # Access instance attribute
# MLOps use: create dataset objects, model instances, pipeline components

# ============================================================================
# METHODS - Functions that belong to objects
# ============================================================================

class Dataset:
    """Dataset class with methods for behavior."""
    def __init__(self, path):
        """Initialize dataset with file path."""
        self.path = path

    def load(self):
        """Method to load dataset - defines object behavior."""
        print(f"Loading data from {self.path}")
        # Methods can access instance attributes via self
        # MLOps use: train(), predict(), evaluate(), save() methods

# ============================================================================
# INHERITANCE - Creating specialized classes
# ============================================================================

class CSVDataset(Dataset):  # CSVDataset inherits from Dataset
    """Specialized dataset for CSV files."""
    def parse(self):
        """CSV-specific parsing method."""
        print("Parsing CSV file")
        # Inherits __init__ and load() from Dataset
        # Adds CSV-specific functionality
        # MLOps use: specialized model types, different data formats

# ============================================================================
# POLYMORPHISM - Same interface, different behavior
# ============================================================================

# Note: JSONDataset would need to be defined for this to work
# This demonstrates polymorphism - different classes, same method name
for d in [CSVDataset("train.csv")]:
    d.parse()  # Each class implements parse() differently
    # MLOps use: different models with same interface (train, predict)


