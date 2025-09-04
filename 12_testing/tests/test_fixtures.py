#!/usr/bin/python3

"""
Pytest Fixtures - Educational Examples

Demonstrates fixture usage patterns:
- Custom fixtures from conftest.py
- Built-in pytest fixtures (tmp_path)
- Dependency injection in tests
- Combining multiple fixtures
"""

# Using fixtures (from "pytest Fixtures").

from pathlib import Path

# ============================================================================
# CUSTOM FIXTURE USAGE - Using fixtures from conftest.py
# ============================================================================

def test_cleaner_fixture(cleaner):
    """Test using custom cleaner fixture."""
    assert cleaner.strip_lower("  A B C  ") == "a b c"
    # 'cleaner' parameter automatically injected by pytest
    # MLOps use: model instances, data processors, test configurations
    # Benefit: no manual setup, consistent test environment

# ============================================================================
# BUILT-IN FIXTURE USAGE - Using pytest's built-in fixtures
# ============================================================================

def test_tmp_path_fixture_writes_file(tmp_path, cleaner):
    """Test using built-in tmp_path fixture with custom fixture."""
    # Create a small file and read it back
    p: Path = tmp_path / "sample.txt"  # tmp_path provides temporary directory
    p.write_text("  HeLLo  ", encoding="utf-8")  # Write test data
    raw = p.read_text(encoding="utf-8")           # Read back
    assert cleaner.strip_lower(raw) == "hello"    # Test processing
    # MLOps use: temporary model files, test datasets, output validation
    # Benefits: automatic cleanup, isolated file operations, no conflicts
