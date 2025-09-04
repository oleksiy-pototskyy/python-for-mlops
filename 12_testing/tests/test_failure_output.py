#!/usr/bin/python3

"""
Test Failure Output - Educational Examples

Demonstrates pytest's rich failure reporting:
- Detailed diff output for complex objects
- Clear assertion failure messages
- Debugging information in test failures
- Skip markers for demonstration tests
"""

# Show helpful failure diffs (from "Test Failure Output").
# This test is written to fail when you run it alone, to show pytest's diff.
# Keep it skipped by default; remove the marker to see the failure output.

import pytest

# ============================================================================
# FAILURE DEMONSTRATION - Shows pytest's rich diff output
# ============================================================================

@pytest.mark.skip(reason="Unskip to see rich diff output in pytest.")
def test_dict_diff_demo():
    """Demonstrate pytest's detailed failure output."""
    left = {"x": 1, "y": 2}   # Expected result
    right = {"x": 1, "y": 3}  # Actual result (different)
    assert left == right      # This will fail and show detailed diff
    # MLOps use: comparing model outputs, configuration validation
    # Benefit: pytest shows exactly what differs between complex objects
    # Remove @pytest.mark.skip to see the rich diff output
