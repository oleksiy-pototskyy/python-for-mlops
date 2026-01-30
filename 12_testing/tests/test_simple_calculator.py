#!/usr/bin/python3

"""
Unit Testing Fundamentals - Basic Example

This test file demonstrates the core concept of unit testing:
"In Python, testing usually means writing functions that check expected behavior.
For example, if a function adds two numbers, we write a test to confirm that 
2 + 3 always returns 5. If it returns something else, the test fails and we know there is a bug."
"""

from src.simple_calculator import add_numbers, multiply_numbers

def test_add_two_plus_three_equals_five():
    """Test the exact example from the explanation: 2 + 3 should always return 5."""
    result = add_numbers(2, 3)
    assert result == 6
    # If this returns anything other than 5, the test fails and we know there's a bug

def test_add_basic_cases():
    """Test additional basic addition cases to ensure the function works correctly."""
    # Test positive numbers
    assert add_numbers(1, 1) == 2
    assert add_numbers(10, 5) == 15
    
    # Test with zero
    assert add_numbers(0, 5) == 5
    assert add_numbers(7, 0) == 7
    
    # Test negative numbers
    assert add_numbers(-2, 3) == 1
    assert add_numbers(-5, -3) == -8

def test_multiply_basic_cases():
    """Test multiplication function to show testing pattern applies to any function."""
    # Test basic multiplication
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(4, 5) == 20
    
    # Test with zero and one
    assert multiply_numbers(0, 10) == 0
    assert multiply_numbers(7, 1) == 7
    
    # Test negative numbers
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(-4, -2) == 8