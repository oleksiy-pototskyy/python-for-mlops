#!/usr/bin/python3

"""
mlops_utils/__init__.py - Package Initialization

Makes mlops_utils a Python package:
- Defines what gets imported when using 'from mlops_utils import ...'
- Controls package's public API
- Allows convenient imports without specifying submodules
"""

# Import functions from submodules to make them available at package level
from .data import preprocess      # Import preprocess from data.py
from .logging import log_metric   # Import log_metric from logging.py

# Now users can do: from mlops_utils import preprocess, log_metric
# Instead of: from mlops_utils.data import preprocess

