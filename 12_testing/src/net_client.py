#!/usr/bin/python3

"""
Network Client - Source Code for Mocking/Patching Examples

Functions that demonstrate testing external dependencies:
- Time-dependent operations (sleep)
- Network requests (HTTP calls)
- External library usage
- Mocking and patching targets
"""

import time
import requests

# ============================================================================
# TIME-DEPENDENT FUNCTION - Demonstrates patching time.sleep
# ============================================================================

def slow_add(a, b, delay_seconds=1.0):
    """Add two numbers with artificial delay."""
    # Simulate slow work to show patching time.sleep in tests
    time.sleep(delay_seconds)  # External dependency to mock
    return a + b
    # MLOps use: model training, data processing, batch operations
    # Testing challenge: avoid real delays in tests

# ============================================================================
# NETWORK FUNCTION - Demonstrates mocking HTTP requests
# ============================================================================

def fetch_json(url: str) -> dict:
    """Fetch JSON data from URL."""
    # Very small wrapper to show how to mock requests.get
    resp = requests.get(url, timeout=5)  # External HTTP call to mock
    resp.raise_for_status()              # May raise HTTPError
    return resp.json()                   # Return parsed JSON
    # MLOps use: API calls, data fetching, model serving endpoints
    # Testing challenge: avoid real network calls, handle errors
