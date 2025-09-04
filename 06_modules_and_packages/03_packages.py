#!/usr/bin/python3

"""
Packages - Educational Examples

Demonstrates different ways to import from Python packages:
- Absolute imports (full package path)
- Relative imports (within package)
- Package-level imports (via __init__.py)
"""

# ============================================================================
# ABSOLUTE IMPORTS - Full package.module.function path
# ============================================================================

# Import specific functions from package submodules using full path
from mlops_utils.data import load_data      # mlops_utils/data.py
from mlops_utils.logging import log_metric  # mlops_utils/logging.py
# MLOps use: clear, explicit imports; works from anywhere in project

# ============================================================================
# RELATIVE IMPORTS - Used within packages (commented - would cause error here)
# ============================================================================

# from .data import load_data        # Import from same package level
# from .logging import log_metric    # Dot notation for relative imports
# Note: Relative imports only work when this file is part of a package
# MLOps use: internal package organization, cleaner imports within packages

# ============================================================================
# PACKAGE-LEVEL IMPORTS - Via __init__.py convenience
# ============================================================================

# Import functions made available at package level through __init__.py
from mlops_utils import load_data, log_metric
# This works because __init__.py imports these functions from submodules
# MLOps use: simplified API, user-friendly package interface, clean imports



