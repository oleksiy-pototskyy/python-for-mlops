#!/usr/bin/python3

"""
Python Scope and Namespaces for MLOps - Practical Demonstration

This script demonstrates LEGB rule and namespace concepts covered in the video lecture
with practical MLOps examples showing why scope matters in ML pipelines.
"""

# ============================================================================
# GLOBAL SCOPE - Module-level variables (avoid mutation in production)
# ============================================================================

# Global variables - accessible throughout the module
MODEL_CONFIG = {"lr": 0.001, "batch_size": 32}  # Good: configuration constant
counter = 0  # Global variable (avoid modifying in functions)

# More global examples for MLOps
CHECKPOINT_DIR = "/models/checkpoints"
MAX_RETRIES = 3


# ============================================================================
# LEGB RULE DEMONSTRATION - Local, Enclosing, Global, Built-in
# ============================================================================

def demonstrate_legb():
    """Shows Python's LEGB scope resolution order."""
    
    # Global variable
    x = 10  # This is GLOBAL scope
    
    def outer_function():
        """Demonstrates ENCLOSING scope."""
        # This variable is in ENCLOSING scope for inner_function
        y = 20  # ENCLOSING scope variable
        
        def inner_function():
            """Demonstrates LOCAL scope and LEGB lookup."""
            # This is LOCAL scope
            z = 30  # LOCAL variable
            
            # Python searches for variables in LEGB order:
            print(f"Local z: {z}")        # L - Local scope
            print(f"Enclosing y: {y}")    # E - Enclosing scope  
            print(f"Global x: {x}")       # G - Global scope
            print(f"Built-in len: {len}")  # B - Built-in scope
            
        return inner_function
    
    # Execute the nested function
    inner_func = outer_function()
    inner_func()


def scope_error_example():
    """Shows what happens when accessing variables outside their scope."""
    
    def create_local_variable():
        local_var = "I only exist inside this function"
        print(f"Inside function: {local_var}")
    
    create_local_variable()
    
    # This would cause NameError - local_var doesn't exist here
    # print(local_var)  # NameError: name 'local_var' is not defined
    print("Cannot access local_var outside the function (would cause NameError)")


# ============================================================================
# NAMESPACE INSPECTION - Understanding Python's namespace system
# ============================================================================

def demonstrate_namespaces():
    """Shows how to inspect global and local namespaces."""
    
    # Global variable for demonstration
    global_example = "I'm in global namespace"
    
    print("=== Namespace Inspection ===")
    
    # Show some global namespace contents
    print("Some global names:")
    global_names = [name for name in globals().keys() 
                   if not name.startswith('__')][:5]  # First 5 non-special names
    for name in global_names:
        print(f"  {name}")
    
    def local_namespace_demo():
        """Function to demonstrate local namespace."""
        local_var = "I'm in local namespace"
        another_local = 42
        
        print("\nLocal namespace contents:")
        for name, value in locals().items():
            print(f"  {name}: {value}")
        
        # Check if variables exist in different namespaces
        print(f"\n'local_var' in locals(): {'local_var' in locals()}")
        print(f"'MODEL_CONFIG' in globals(): {'MODEL_CONFIG' in globals()}")
        print(f"'len' in dir(__builtins__): {'len' in dir(__builtins__)}")
    
    local_namespace_demo()


# ============================================================================
# GLOBAL AND NONLOCAL KEYWORDS - Modifying outer scope variables
# ============================================================================

def demonstrate_global_keyword():
    """Shows how global keyword works (and why to avoid it)."""
    
    print("\n=== Global Keyword Demonstration ===")
    print(f"Counter before: {counter}")
    
    def increment_counter():
        """Function that modifies global variable."""
        global counter  # Required to modify global variable
        counter += 1    # Without 'global', this would create local variable
        print(f"Inside function, counter: {counter}")
    
    increment_counter()
    print(f"Counter after: {counter}")
    
    # WARNING: This pattern is problematic in MLOps!
    print("WARNING: Modifying globals creates side effects - avoid in production!")


def demonstrate_nonlocal_keyword():
    """Shows nonlocal keyword for nested functions."""
    
    print("\n=== Nonlocal Keyword Demonstration ===")
    
    def create_model_trainer():
        """Factory function that creates a trainer with internal state."""
        # This variable is in ENCLOSING scope
        training_step = 0
        best_loss = float('inf')
        
        def train_epoch(current_loss):
            """Inner function that modifies enclosing scope variables."""
            nonlocal training_step, best_loss  # Access enclosing scope
            
            training_step += 1
            if current_loss < best_loss:
                best_loss = current_loss
                print(f"New best loss: {best_loss} at step {training_step}")
            else:
                print(f"Step {training_step}, loss: {current_loss}")
        
        def get_stats():
            """Another inner function accessing enclosing scope."""
            return {"step": training_step, "best_loss": best_loss}
        
        return train_epoch, get_stats
    
    # Create trainer functions
    train_fn, stats_fn = create_model_trainer()
    
    # Simulate training
    train_fn(0.8)  # Step 1
    train_fn(0.6)  # Step 2, new best
    train_fn(0.7)  # Step 3
    
    print(f"Final stats: {stats_fn()}")


# ============================================================================
# MLOPS BEST PRACTICES - Avoiding scope problems
# ============================================================================

def mlops_scope_best_practices():
    """Demonstrates better patterns for MLOps code."""
    
    print("\n=== MLOps Best Practices ===")
    
    # GOOD: Pass values as parameters, return results
    def calculate_accuracy(predictions, labels):
        """Pure function - no side effects."""
        correct = sum(1 for p, l in zip(predictions, labels) if p == l)
        return correct / len(labels)
    
    # GOOD: Use class for stateful operations
    class ExperimentTracker:
        """Better alternative to global variables."""
        
        def __init__(self):
            self.metrics = []
            self.best_score = 0.0
        
        def log_metric(self, metric_name, value):
            """Log metrics without global state."""
            self.metrics.append({"name": metric_name, "value": value})
            if metric_name == "accuracy" and value > self.best_score:
                self.best_score = value
                print(f"New best accuracy: {value}")
        
        def get_summary(self):
            """Get experiment summary."""
            return {
                "total_metrics": len(self.metrics),
                "best_score": self.best_score
            }
    
    # Demonstrate better patterns
    predictions = [1, 0, 1, 1, 0]
    labels = [1, 0, 1, 0, 0]
    
    accuracy = calculate_accuracy(predictions, labels)
    print(f"Model accuracy: {accuracy:.2f}")
    
    # Use class instead of global state
    tracker = ExperimentTracker()
    tracker.log_metric("accuracy", accuracy)
    tracker.log_metric("loss", 0.3)
    
    print(f"Experiment summary: {tracker.get_summary()}")


def import_namespace_example():
    """Shows how imports affect namespaces."""
    
    print("\n=== Import Namespace Example ===")
    
    # Different import styles create different namespace entries
    import os                    # Creates 'os' in global namespace
    import json as js           # Creates 'js' in global namespace
    from math import sqrt       # Creates 'sqrt' in global namespace
    
    print("After imports, these names are in global namespace:")
    import_names = ['os', 'js', 'sqrt']
    for name in import_names:
        if name in globals():
            print(f"  {name}: {type(globals()[name])}")
    
    # Use the imported functions
    print(f"Current directory: {os.getcwd()}")
    print(f"Square root of 16: {sqrt(16)}")


if __name__ == "__main__":
    print("=== Python Scope and Namespaces for MLOps ===")
    
    # Demonstrate LEGB rule
    print("\n1. LEGB Rule (Local, Enclosing, Global, Built-in):")
    demonstrate_legb()
    
    # Show scope errors
    print("\n2. Scope Boundaries:")
    scope_error_example()
    
    # Namespace inspection
    print("\n3. Namespace Inspection:")
    demonstrate_namespaces()
    
    # Global keyword (problematic pattern)
    print("\n4. Global Keyword (avoid in production):")
    demonstrate_global_keyword()
    
    # Nonlocal keyword (useful for closures)
    print("\n5. Nonlocal Keyword (useful for nested functions):")
    demonstrate_nonlocal_keyword()
    
    # Import namespaces
    print("\n6. Import Namespaces:")
    import_namespace_example()
    
    # Best practices for MLOps
    print("\n7. MLOps Best Practices:")
    mlops_scope_best_practices()
    
    print("\n=== Key Takeaways ===")
    print("✓ LEGB: Local → Enclosing → Global → Built-in")
    print("✓ Use globals() and locals() to inspect namespaces")
    print("✓ Avoid modifying global variables in functions")
    print("✓ Use 'nonlocal' for nested function state")
    print("✓ Prefer function parameters over global access")
    print("✓ Use classes for stateful operations in MLOps")
    print("✓ Be consistent with import styles in teams")