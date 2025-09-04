#!/usr/bin/python3

"""
HTTP Clients (requests, httpx) for MLOps - Educational Examples

Demonstrates HTTP client libraries essential for MLOps:
- Synchronous HTTP requests with requests library
- Modern HTTP client with httpx
- Asynchronous HTTP requests for performance
- Timeout handling for reliable API calls
"""

# ============================================================================
# REQUESTS LIBRARY - Traditional synchronous HTTP client
# ============================================================================

import requests
response = requests.get("https://api.github.com")  # Make GET request
print(response.status_code)  # HTTP status code (200, 404, etc.)
print(response.json())       # Parse JSON response to Python dict
# requests: most popular HTTP library, simple synchronous API
# MLOps use: API calls to ML services, data fetching, model serving endpoints

# ============================================================================
# HTTPX LIBRARY - Modern HTTP client with sync/async support
# ============================================================================

import httpx
response = httpx.get("https://api.github.com")  # Similar API to requests
print(response.status_code)  # Same response interface
# httpx: modern alternative with HTTP/2 support and async capabilities
# MLOps use: high-performance API calls, modern ML service integration

# ============================================================================
# ASYNCHRONOUS HTTP - Non-blocking requests for better performance
# ============================================================================

import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:  # Async context manager
        r = await client.get("https://api.github.com")  # Await async request
        print(r.status_code)

asyncio.run(main())  # Run async function
# Async HTTP allows multiple concurrent requests without blocking
# MLOps use: batch API calls, parallel model inference, high-throughput services

# ============================================================================
# TIMEOUT HANDLING - Prevent hanging requests in production
# ============================================================================

r = requests.get("https://api.github.com", timeout=5)  # 5-second timeout
# timeout parameter prevents requests from hanging indefinitely
# Critical for production MLOps systems to avoid blocking operations
# MLOps use: reliable API calls, service health checks, model endpoint calls


