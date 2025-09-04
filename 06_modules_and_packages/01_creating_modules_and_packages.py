#!/usr/bin/python3

"""
Creating Modules and Packages - Educational Examples

Demonstrates different ways to import and use:
- Simple modules (single .py files)
- Packages (directories with __init__.py)
- Specific functions from modules/packages
"""

# ============================================================================
# IMPORTING FROM SIMPLE MODULE - Single .py file
# ============================================================================

# Import function from utils.py module in same directory
from utils import load_dataset
load_dataset("data/train.csv")
# MLOps use: import utility functions, helper modules, custom tools

# ============================================================================
# IMPORTING FROM PACKAGE SUBMODULES - Specific module.function
# ============================================================================

# Import specific functions from package submodules
from mlops_utils.data import preprocess      # From mlops_utils/data.py
from mlops_utils.logging import log_metric   # From mlops_utils/logging.py
# MLOps use: import specific functionality, organized code structure

# ============================================================================
# IMPORTING FROM PACKAGE __init__.py - Convenient package-level imports
# ============================================================================

# Import functions made available through __init__.py
from mlops_utils import preprocess, log_metric
# This works because __init__.py imports these functions
# MLOps use: clean imports, package API design, user-friendly interfaces
