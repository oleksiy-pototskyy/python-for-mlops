#!/usr/bin/python3

"""
Test Classes vs Functions - Educational Examples

Demonstrates different test organization patterns:
- Function-based tests (simple, isolated)
- Class-based tests (grouped, shared setup)
- Setup and teardown methods
- When to use each approach
"""

from src.text_utils import DataCleaner

# ============================================================================
# FUNCTION-BASED TESTS - Simple, isolated test functions
# ============================================================================

# --- Function style ---
def test_strip_lower_function_style():
    """Test using function-based approach."""
    c = DataCleaner()  # Create instance for each test
    assert c.strip_lower("  HeLLo  ") == "hello"
    # MLOps use: simple unit tests, isolated functionality
    # Benefits: easy to understand, no shared state, independent

# ============================================================================
# CLASS-BASED TESTS - Grouped tests with shared setup
# ============================================================================

# --- Class style (pytest discovers methods that start with 'test_') ---
class TestDataCleaner:
    """Test class for DataCleaner functionality."""
    
    def setup_method(self):
        """Setup method called before each test method."""
        self.c = DataCleaner()  # Shared instance across test methods
        # MLOps use: expensive setup (model loading, data preparation)

    def test_strip_lower_class_style(self):
        """Test using class-based approach with shared setup."""
        assert self.c.strip_lower("  WORLD  ") == "world"
        # MLOps use: related tests, shared expensive setup, test suites
        # Benefits: grouped related tests, shared setup/teardown, organization
