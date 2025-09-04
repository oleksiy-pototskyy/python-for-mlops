#!/usr/bin/python3

"""
Class Objects for MLOps - Educational Examples

Demonstrates that classes are objects in Python:
- Classes are instances of 'type'
- Classes can be assigned to variables
- Classes have attributes and methods
- Classes can be passed as arguments
- Dynamic class attribute modification
"""

# ============================================================================
# CLASS DEFINITION - Creates a class object
# ============================================================================

class Dataset:
    """Dataset class - this creates a class object."""
    def __init__(self, path):
        self.path = path
        # When Python executes this, it creates a class object named 'Dataset'

# ============================================================================
# CLASSES ARE OBJECTS - Everything in Python is an object
# ============================================================================

# Classes themselves are objects of type 'type'
print(type(Dataset))  # <class 'type'>
# Dataset is an object (instance of 'type')
# MLOps use: understanding metaclasses, dynamic class creation

# ============================================================================
# CREATING INSTANCES - Class objects create instance objects
# ============================================================================

# Class object creates instance objects
train = Dataset("train.csv")  # Dataset (class object) creates train (instance object)
# Class acts as factory for creating instances
# MLOps use: create multiple model instances, dataset loaders

# ============================================================================
# DYNAMIC CLASS ATTRIBUTES - Modify class objects at runtime
# ============================================================================

# Add attribute to class object dynamically
Dataset.version = "1.0"  # Add class attribute to Dataset class object
print(Dataset.version)  # 1.0 - access class attribute
# MLOps use: runtime configuration, feature flags, version tracking

# ============================================================================
# ATTRIBUTE INHERITANCE - Instance objects inherit from class objects
# ============================================================================

# Instance inherits class attributes
print(train.version)  # 1.0 - instance inherits class attribute
# Instance looks up attributes in class if not found in instance
# MLOps use: shared configuration, default parameters

# ============================================================================
# CLASS INTROSPECTION - Examine class object properties
# ============================================================================

# Class objects have metadata attributes
print(Dataset.__name__)     # 'Dataset' - class name
print(Dataset.__dict__.keys())  # Class namespace contents
# MLOps use: debugging, logging, dynamic component discovery

# ============================================================================
# CLASSES AS ARGUMENTS - Pass class objects to functions
# ============================================================================

def register(component):
    """Function that accepts class objects as arguments."""
    print(f"Registered: {component.__name__}")
    # Function receives class object, accesses its attributes
    # MLOps use: plugin systems, component registration, factory patterns

# Pass class object as argument
register(Dataset)  # Pass Dataset class object to function
# Output: "Registered: Dataset"
# Classes can be treated like any other object



