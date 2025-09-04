#!/usr/bin/python3

"""
Unittest Style Tests - Educational Examples

Demonstrates unittest framework patterns:
- Class-based test structure
- Special assertion methods (assertEqual, etc.)
- Traditional Python testing approach
- Comparison with pytest style
"""

# unittest style tests (from "Using unittest and pytest").

import unittest
from src.math_ops import add

# ============================================================================
# UNITTEST CLASS - Traditional Python testing framework
# ============================================================================

class TestMathOps(unittest.TestCase):
    """Test class using unittest framework."""
    
    def test_add(self):
        """Test addition function using unittest assertions."""
        self.assertEqual(add(2, 3), 5)
        # unittest uses special assertion methods (assertEqual, assertTrue, etc.)
        # MLOps use: legacy codebases, traditional Python projects
        # Comparison: more verbose than pytest's plain assert

# ============================================================================
# UNITTEST RUNNER - Direct execution support
# ============================================================================

if __name__ == "__main__":
    unittest.main()
    # Allows running tests directly: python test_math_ops_unittest.py
    # pytest can also run unittest-style tests automatically

