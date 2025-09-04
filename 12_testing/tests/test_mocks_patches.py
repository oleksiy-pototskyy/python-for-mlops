#!/usr/bin/python3

"""
Mocks & Patches - Educational Examples

Demonstrates mocking external dependencies:
- Patching time-dependent functions
- Mocking HTTP requests
- Avoiding real external calls in tests
- Verifying mock interactions
"""

# Mocks & Patches demos (from "Mocks & Patches").
# Show patching time.sleep and requests.get.

from unittest.mock import patch, Mock
from src.net_client import slow_add, fetch_json

# ============================================================================
# PATCHING TIME DEPENDENCIES - Avoid real delays in tests
# ============================================================================

def test_slow_add_without_real_sleep():
    """Test time-dependent function without actual delay."""
    with patch("src.net_client.time.sleep") as fake_sleep:
        result = slow_add(2, 3, delay_seconds=10.0)  # Would normally take 10 seconds
        fake_sleep.assert_called_once()  # Verify sleep was called
        assert result == 5               # Test actual functionality
    # MLOps use: model training timeouts, batch processing delays
    # Benefit: fast tests, no real waiting, verify timing logic

# ============================================================================
# MOCKING HTTP REQUESTS - Avoid real network calls
# ============================================================================

def test_fetch_json_mocks_requests_get():
    """Test HTTP function without real network requests."""
    # Create mock response object
    fake_response = Mock()
    fake_response.json.return_value = {"ok": True}        # Mock JSON response
    fake_response.raise_for_status.return_value = None    # Mock success status

    # Patch requests.get to return our mock
    with patch("src.net_client.requests.get", return_value=fake_response) as fake_get:
        data = fetch_json("https://example.com/data")  # No real HTTP call
        fake_get.assert_called_once()                  # Verify request was made
        assert data == {"ok": True}                    # Test response handling
    # MLOps use: API calls, model serving endpoints, data fetching
    # Benefits: fast tests, no network dependency, controlled responses

