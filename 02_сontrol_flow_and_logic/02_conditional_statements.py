#!/usr/bin/python3

"""
Python Conditional Statements for MLOps - Educational Examples

Demonstrates conditional logic essential for:
- Model validation and acceptance criteria
- Performance-based decision making
- Pipeline flow control
- Automated quality gates
"""

# ============================================================================
# SIMPLE IF STATEMENTS - Basic conditional execution
# ============================================================================

# Single condition check - most common pattern in MLOps
accuracy = 0.92
if accuracy > 0.90:
    print("Model passed validation")
    # MLOps use: model acceptance gates, quality thresholds

# ============================================================================
# IF-ELIF-ELSE CHAINS - Multiple condition handling
# ============================================================================

# Multi-tier evaluation system - common for model grading
score = 0.85

# Cascading conditions - checks from top to bottom, stops at first match
if score >= 0.90:
    print("Excellent model")     # Top tier: production-ready
elif score >= 0.80:
    print("Good model")          # Middle tier: staging-ready
else:
    print("Needs improvement")   # Catch-all: requires retraining

# ============================================================================
# COMPOUND CONDITIONS - Multiple criteria evaluation
# ============================================================================

# Multiple conditions with logical operators
loss = 0.05  # Define loss for compound condition

if accuracy > 0.90 and loss < 0.1:
    print("Ready for production")
    # MLOps use: multi-metric validation gates
    # Both conditions must be True for deployment

# ============================================================================
# TERNARY OPERATOR - Compact conditional assignment
# ============================================================================

# Conditional expression - compact if-else for simple assignments
status = "success" if accuracy > 0.90 else "retry"
print(status)
# Syntax: value_if_true if condition else value_if_false
# MLOps use: status flags, quick decisions, configuration switches

