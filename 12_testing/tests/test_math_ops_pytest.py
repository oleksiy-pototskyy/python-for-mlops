#!/usr/bin/python3

"""
Pytest Style Tests - Educational Examples

Demonstrates pytest testing patterns:
- Simple assert statements (no special methods)
- Clear, readable test functions
- Fixture usage for test data
- Boolean assertion patterns
"""

# Plain pytest tests using simple assert (from "Using plain assert in pytest").

from src.math_ops import add, is_even

# ============================================================================
# BASIC ASSERTIONS - Simple pytest assert patterns
# ============================================================================

def test_add_returns_sum():
    """Test basic arithmetic function."""
    assert add(2, 3) == 5
    # Pytest uses plain Python assert - no special methods needed
    # MLOps use: test metric calculations, loss functions, aggregations

# ============================================================================
# FIXTURE-BASED TESTS - Using shared test data
# ============================================================================

def test_list_membership_and_length(sample_numbers):
    """Test using fixture data with multiple assertions."""
    assert 2 in sample_numbers      # Test membership
    assert len(sample_numbers) == 3 # Test length
    # Multiple related assertions in single test
    # MLOps use: validate dataset properties, batch sizes, feature counts

# ============================================================================
# BOOLEAN ASSERTIONS - Testing True/False returns
# ============================================================================

def test_is_even_true():
    """Test function returns True for even numbers."""
    assert is_even(4) is True
    # Use 'is True' for explicit boolean testing
    # MLOps use: validation functions, feature flags, condition checks

def test_is_even_false():
    """Test function returns False for odd numbers."""
    assert is_even(5) is False
    # Use 'is False' for explicit boolean testing
    # MLOps use: data quality checks, model validation, pipeline conditions
