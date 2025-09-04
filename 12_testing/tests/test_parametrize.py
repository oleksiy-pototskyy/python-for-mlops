#!/usr/bin/python3

"""
Parametrized Tests - Educational Examples

Demonstrates pytest parametrization:
- Testing multiple input combinations
- Reducing test code duplication
- Comprehensive edge case coverage
- Data-driven testing patterns
"""

# Parametrized pytest tests (from "Parameterizing Tests").

import pytest
from src.math_ops import add, is_even

# ============================================================================
# MULTIPLE PARAMETER PARAMETRIZATION - Test many input combinations
# ============================================================================

@pytest.mark.parametrize(
    "a,b,expected",  # Parameter names
    [
        (0, 0, 0),      # Edge case: zeros
        (2, 3, 5),      # Normal case: positive numbers
        (-1, 1, 0),     # Edge case: negative and positive
        (10, -2, 8),    # Mixed case: positive and negative
    ],
)
def test_add_parametrized(a, b, expected):
    """Test addition with multiple parameter combinations."""
    assert add(a, b) == expected
    # Single test function runs 4 times with different inputs
    # MLOps use: test model with different hyperparameters, data ranges
    # Benefit: comprehensive coverage, less code duplication

# ============================================================================
# SIMPLE PARAMETRIZATION - Test boolean function with various inputs
# ============================================================================

@pytest.mark.parametrize("value,expected", [(2, True), (3, False), (100, True)])
def test_is_even_parametrized(value, expected):
    """Test even number detection with parametrized inputs."""
    assert is_even(value) is expected
    # Tests: 2 (even), 3 (odd), 100 (large even)
    # MLOps use: validation functions, data quality checks, feature engineering
    # Benefit: test edge cases, boundary conditions, various data types
