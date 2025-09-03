#!/usr/bin/python3

"""
Python F-strings and String Formatting for MLOps - Educational Examples

Demonstrates modern string formatting techniques essential for:
- Training logs and metrics reporting
- Configuration display
- Progress tracking
- Debug output
"""

def demo_values():
    """
    Demonstrates f-string formatting with MLOps use cases.
    """
    
    # ============================================================================
    # BASIC F-STRING SYNTAX - Modern Python string formatting (Python 3.6+)
    # ============================================================================
    
    epoch = 5
    loss = 0.134
    
    # F-strings: f"text {variable}" - most readable and efficient
    # Simple variable insertion for training logs
    print(f"Epoch {epoch}: loss={loss}")
    # Output: Epoch 5: loss=0.134
    # MLOps use: training progress logs, experiment tracking
    
    # ============================================================================
    # NUMERIC FORMATTING - Precision control for metrics and measurements
    # ============================================================================
    
    accuracy = 0.93456
    
    # Format floats with specific decimal places using :.Nf syntax
    print(f"Accuracy: {accuracy:.2f}")  # Accuracy: 0.93
    # Syntax: {variable:.Nf} where N = number of decimal places
    # Critical for MLOps: model metrics need consistent precision for comparison
    
    # ============================================================================
    # EXPRESSIONS IN F-STRINGS - Calculations and function calls
    # ============================================================================
    
    samples = 1200
    
    # Perform calculations directly inside f-strings
    print(f"Samples per worker: {samples/4}")
    # Output: Samples per worker: 300.0
    # MLOps use: dynamic calculations, data statistics, real-time metrics
    
    # ============================================================================
    # COMPARISON: OLD vs NEW FORMATTING STYLES
    # ============================================================================
    
    # OLD STYLE: % formatting (avoid in new code)
    print("Epoch %d: loss=%.2f" % (epoch, loss))
    # Problems: hard to read, error-prone, limited functionality
    
    # MIDDLE STYLE: .format() method (Python 2.7+)
    print("Epoch {}: loss={:.2f}".format(epoch, loss))
    # Better than %, but still verbose compared to f-strings
    
    # MODERN STYLE: f-strings (Python 3.6+) - RECOMMENDED for MLOps
    # Benefits: readable, fast, supports expressions, less error-prone

    # ============================================================================
    # ADVANCED F-STRING FEATURES - Debugging and representation
    # ============================================================================
    
    config = {"lr": 0.01, "batch": 32}
    
    # !r modifier - calls repr() for debugging output
    print(f"Loaded config: {config!r}")
    # Output: Loaded config: {'lr': 0.01, 'batch': 32}
    # Shows exact representation with quotes - useful for debugging MLOps configs
    # Alternative modifiers: !s (str), !a (ascii)


if __name__ == "__main__":
    print("=== Python F-strings and String Formatting for MLOps ===")
    demo_values()
    
    print("\n=== Key F-string Concepts ===")
    print("✓ f-strings are fastest and most readable (use them!)")
    print("✓ {variable:.Nf} controls decimal places for metrics")
    print("✓ {variable!r} shows debug representation")
    print("✓ Can include expressions: {value * 100}")
    print("✓ Perfect for MLOps logging and progress tracking")
