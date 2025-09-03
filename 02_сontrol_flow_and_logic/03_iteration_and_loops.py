#!/usr/bin/python3

"""
Python Iteration and Loops for MLOps - Educational Examples

Demonstrates loop patterns essential for:
- Data processing and batch operations
- Training iterations and epochs
- File processing workflows
- Conditional loop control
"""

# ============================================================================
# FOR LOOPS WITH LISTS - Iterating over collections
# ============================================================================

# Iterate over data files - common MLOps pattern
files = ["train.csv", "test.csv", "validate.csv"]
for f in files:
    print(f"Processing {f}")
    # MLOps use: process dataset splits, batch files, model checkpoints

# ============================================================================
# FOR LOOPS WITH RANGE - Numeric iterations
# ============================================================================

# Training loop with epoch counting
for epoch in range(1, 6):  # range(start, stop) - stop is exclusive
    print(f"Training epoch {epoch}")
    # MLOps use: training epochs, batch iterations, hyperparameter sweeps

# ============================================================================
# WHILE LOOPS - Condition-based iteration
# ============================================================================

# Iterative improvement until threshold reached
accuracy = 0.85
while accuracy < 0.90:  # Continue until condition becomes False
    accuracy += 0.01
    print(f"Improved accuracy: {accuracy:.2f}")
    # MLOps use: convergence loops, early stopping, adaptive learning

# ============================================================================
# BREAK STATEMENT - Early loop termination
# ============================================================================

# Stop processing when encountering invalid data
for value in [1, 2, 0, 3]:
    if value == 0:
        break  # Exit loop immediately when condition met
    print(value)
    # Output: 1, 2 (stops at 0)
    # MLOps use: error handling, early stopping, resource limits

# ============================================================================
# CONTINUE STATEMENT - Skip current iteration
# ============================================================================

# Skip invalid data but continue processing
for value in [1, 2, 0, 3]:
    if value == 0:
        continue  # Skip rest of current iteration, go to next
    print(value)
    # Output: 1, 2, 3 (skips 0)
    # MLOps use: data filtering, error recovery, selective processing

