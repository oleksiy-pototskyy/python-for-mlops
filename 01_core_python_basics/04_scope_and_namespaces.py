#!/usr/bin/python3

# ============================================================================
# GLOBAL SCOPE - Module-level namespace
# ============================================================================

# Global variable - accessible throughout the module
# In MLOps: used for configuration, constants, shared state (avoid mutation!)
COUNTER = 0  # Global variable - avoid mutating in production code


# ============================================================================
# ENCLOSING SCOPE - Nested function closures
# ============================================================================

def outer():
    """
    Demonstrates ENCLOSING scope and 'nonlocal' keyword.
    
    Common in MLOps for:
    - Factory functions that create specialized processors
    - Callback functions with shared state
    - Progress tracking in nested operations
    """
    # ENCLOSING scope variable - accessible to nested functions
    message = "hello"  # This variable lives in the enclosing scope

    def inner():
        """
        LOCAL scope function that modifies ENCLOSING scope variable.
        
        Without 'nonlocal': assignment creates new local variable
        With 'nonlocal': modifies the enclosing scope variable
        """
        nonlocal message  # Declares intent to modify enclosing variable
        message = message.upper()  # Modifies enclosing 'message', not local
        return message

    return inner()  # Call inner function and return result


# ============================================================================
# GLOBAL MODIFICATION - Use with caution in MLOps
# ============================================================================

def bump_global_bad():
    """
    Demonstrates global variable modification.
    
    Problems in MLOps:
    - Makes testing difficult (state persists between tests)
    - Creates hidden dependencies between functions
    - Dangerous in parallel/distributed training
    - Reduces code reusability and modularity
    """
    global COUNTER  # Required keyword to modify global variables
    COUNTER += 1    # Modifies the global COUNTER variable
    # This creates side effects - function changes global state!


# ============================================================================
# NAMESPACE INSPECTION - Debugging and introspection
# ============================================================================

def find_name():
    """
    Demonstrates namespace inspection using locals() and globals().
    
    Useful for:
    - Debugging scope issues in complex ML pipelines
    - Dynamic variable access in configuration systems
    - Understanding what variables are available
    """
    # LOCAL scope variable - only exists within this function
    local_x = 42
    
    # Inspect different namespaces
    print("Namespace inspection:")
    
    # locals() returns dict of current function's local variables
    print("has local_x?", "local_x" in locals())     # True - local_x exists here
    
    # globals() returns dict of module-level global variables  
    print("has COUNTER?", "COUNTER" in globals())   # True - COUNTER is global
    
    # Show the difference:
    print("COUNTER in locals()?", "COUNTER" in locals())   # False - not local
    print("local_x in globals()?", "local_x" in globals()) # False - not global


if __name__ == "__main__":
    print("=== Python Scope and Namespaces Demo ===")
    
    # 1. Demonstrate enclosing scope with nonlocal
    print("\n1. Enclosing scope (nonlocal):")
    result = outer()  # Returns "HELLO" - inner() modified enclosing 'message'
    print(f"Result: {result}")
    
    # 2. Show global variable modification (problematic pattern)
    print("\n2. Global modification:")
    print(f"COUNTER before: {COUNTER}")  # 0
    bump_global_bad()  # Increments global COUNTER
    print(f"COUNTER after: {COUNTER}")   # 1
    
    # 3. Namespace inspection
    print("\n3. Namespace inspection:")
    find_name()  # Shows locals() vs globals() differences
    
    print("\n=== Key Concepts ===")
    print("✓ LEGB Rule: Local -> Enclosing -> Global -> Built-in")
    print("✓ 'nonlocal' modifies enclosing scope variables")
    print("✓ 'global' modifies module-level variables")
    print("✓ locals()/globals() inspect current namespaces")
    print("✓ Avoid global mutation in production MLOps code")