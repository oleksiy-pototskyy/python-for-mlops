#!/usr/bin/python3

"""
Pytest Configuration - Shared Fixtures for Testing

Demonstrates pytest fixture patterns:
- Shared test setup across multiple files
- Dependency injection for tests
- Reusable test data and objects
- Central fixture management
"""

import pytest
from src.text_utils import DataCleaner

# ============================================================================
# OBJECT FIXTURE - Provides reusable class instances
# ============================================================================

@pytest.fixture
def cleaner():
    """Provide a DataCleaner instance to tests."""
    # Provide a DataCleaner instance to tests
    return DataCleaner()
    # MLOps use: model instances, data processors, pipeline components
    # Benefit: consistent setup, no duplication across test files

# ============================================================================
# DATA FIXTURE - Provides reusable test data
# ============================================================================

@pytest.fixture
def sample_numbers():
    """Provide sample numeric data for tests."""
    # Small list for simple checks
    return [1, 2, 3]
    # MLOps use: sample datasets, test arrays, validation data
    # Benefit: centralized test data, easy to modify across all tests
