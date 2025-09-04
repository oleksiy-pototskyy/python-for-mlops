#!/usr/bin/python3

"""
Attributes & @property for MLOps - Educational Examples

Demonstrates attribute management in Python classes:
- Public attributes (direct access)
- Private attributes (naming convention)
- Property decorators for controlled access
- Getters and setters with validation
- Computed properties
"""

# ============================================================================
# PUBLIC ATTRIBUTES - Direct access to instance data
# ============================================================================

class Dataset:
    """Dataset with public attributes - direct access."""
    def __init__(self, path, size):
        self.path = path  # Public attribute - can be accessed directly
        self.size = size  # Public attribute - no access control
        # MLOps use: simple data storage, configuration parameters

# Direct attribute access
train = Dataset("train.csv", 1000)
print(train.path)  # train.csv - direct access
print(train.size)  # 1000 - direct access
# Problem: no validation, can be modified without control

# ============================================================================
# PRIVATE ATTRIBUTES - Naming convention for internal data
# ============================================================================

# Private attribute example (would be inside a class)
# self._cache = None  # Single underscore = "internal use" convention
# MLOps use: internal state, cached data, implementation details

# ============================================================================
# PROPERTY GETTER - Controlled read access
# ============================================================================

class Dataset:
    """Dataset with property getter - controlled access."""
    def __init__(self, path):
        self._path = path  # Private attribute (underscore convention)

    @property
    def path(self):
        """Property getter - controls how attribute is accessed."""
        return self._path
        # Acts like attribute but is actually a method
        # MLOps use: computed values, validated access, logging access

# Usage looks like attribute access but goes through property
# train = Dataset("train.csv")
# print(train.path)  # Calls the property getter method

# ============================================================================
# PROPERTY SETTER - Controlled write access with validation
# ============================================================================

class Dataset:
    """Dataset with property getter and setter - full control."""
    def __init__(self, path):
        self._path = path  # Store in private attribute

    @property
    def path(self):
        """Get the dataset path."""
        return self._path

    @path.setter
    def path(self, value):
        """Set the dataset path with validation."""
        if not value.endswith(".csv"):
            raise ValueError("Dataset must be a CSV file")
        self._path = value
        # MLOps use: validate file formats, check paths, enforce constraints

# Property setter enables validation during assignment
train = Dataset("train.csv")
# train.path = "data.json"  # ValueError - validation prevents invalid assignment
# MLOps benefit: prevents invalid configurations, ensures data integrity

# ============================================================================
# COMPUTED PROPERTIES - Dynamic values calculated on access
# ============================================================================

class Dataset:
    """Dataset with computed property - calculated on demand."""
    def __init__(self, samples):
        self.samples = samples  # Store actual data

    @property
    def size(self):
        """Computed property - calculates size dynamically."""
        return len(self.samples)
        # No stored size attribute - calculated each time
        # MLOps use: dynamic metrics, computed statistics, derived values

# Computed properties always reflect current state
# dataset = Dataset([1, 2, 3])
# print(dataset.size)  # 3 - calculated from current samples
# dataset.samples.append(4)
# print(dataset.size)  # 4 - automatically updated
