#!/usr/bin/python3

def demo_values():
    # ============================================================================
    # BASIC DATA TYPES - Essential for ML model parameters and configurations
    # ============================================================================
    
    # Integer - Used for epochs, batch sizes, model dimensions
    steps = 100             # Training steps or epochs
    steps2 = int(2)

    # Float - Critical for loss values, learning rates, metrics
    loss = 0.123            # Model loss value (always float for precision)
    loss2 = float(0.123)
    
    # Boolean - For flags, convergence status, feature toggles
    is_converged = False    # Training convergence flag
    is_converged2 = bool(False)

    # String - For model names, file paths, experiment descriptions
    note = "epoch finished"  # Log messages, experiment notes
    note2 = str("epoch finished")
    
    # None - Represents absence of value, useful for optional parameters
    nothing = None  # Uninitialized model weights, missing data

    # Bytes - For binary data, model serialization, image processing
    blob = b"bytes"  # Raw model data, binary file content

    # ============================================================================
    # TYPE INSPECTION - Debug and validate data types in ML pipelines
    # ============================================================================
    print("Data Types:")
    print(type(steps), type(loss), type(is_converged), type(note), type(nothing), type(blob))
    # Output: <class 'int'> <class 'float'> <class 'bool'> <class 'str'> <class 'NoneType'> <class 'bytes'>
    
    # ============================================================================
    # F-STRING FORMATTING - Modern Python string formatting for logging/reporting
    # ============================================================================
    print("\nF-string Formatting:")
    # F-strings provide clean, readable formatting for ML experiment logging
    print(f"steps={steps} loss={loss:.4f} converged={is_converged} note='{note}'")
    # :.4f formats float to 4 decimal places - crucial for loss precision
    # Output: steps=100 loss=0.1230 converged=False note='epoch finished'

    # ============================================================================
    # MATHEMATICAL OPERATIONS - Core calculations for ML algorithms
    # ============================================================================
    print("\nMath Operations:")
    print(5 + 2, 5 - 2, 5 * 2, 5 / 2, 5 // 2, 5 % 2, 2 ** 3)
    # Addition, Subtraction, Multiplication, Division, Floor Division, Modulo, Exponentiation
    # Output: 7 3 10 2.5 2 1 8
    # Note: / always returns float, // returns integer division
    
    # ============================================================================
    # COMPARISON OPERATIONS - Essential for conditional logic in ML workflows
    # ============================================================================
    print("\nComparisons:")
    print(3 < 5, 3 == 3, 3 != 4)
    # Less than, Equal to, Not equal to
    # Output: True True True
    # Used for threshold checks, validation, early stopping conditions

    # ============================================================================
    # TRUTHINESS - Python's boolean evaluation rules for control flow
    # ============================================================================
    print("\nTruthiness (Falsy vs Truthy):")
    # Understanding what evaluates to True/False is crucial for conditional logic
    for v in [0, 1, "", "x", [], [1], None, True, False]:
        print(f"{repr(v):>8} => {bool(v)}")
    # Falsy values: 0, "", [], None, False
    # Truthy values: non-zero numbers, non-empty strings/lists, True
    # Critical for: data validation, empty dataset checks, model state verification

if __name__ == "__main__":
    # This block runs only when script is executed directly (not imported)
    # Standard Python pattern for executable scripts
    demo_values()
