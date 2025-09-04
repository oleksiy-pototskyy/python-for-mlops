#!/usr/bin/python3

"""
Text Utils - Source Code for Class-based Testing Examples

Demonstrates testing object-oriented code:
- Class methods and state
- String processing functions
- Fixture usage patterns
- Setup and teardown concepts
"""

# ============================================================================
# DATA PROCESSING CLASS - Demonstrates testing class methods
# ============================================================================

class DataCleaner:
    """Text processing utility for data cleaning."""
    
    def strip_lower(self, s: str) -> str:
        """Remove whitespace and convert to lowercase."""
        # Remove spaces at both ends and make lower-case
        return s.strip().lower()
        # MLOps use: text preprocessing, data normalization, feature engineering
        # Testing: verify string transformations, edge cases, empty strings

