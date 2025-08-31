#!/usr/bin/python3

# ============================================================================
# CONSTANTS - ALL_CAPS with underscores (module-level configuration)
# ============================================================================

# Constants use ALL_CAPS - indicates "don't modify this value"
# Common in MLOps for: hyperparameters, thresholds, file paths, API keys
LEARNING_RATE = 0.01  # Model hyperparameter - treat as read-only
# More examples:
# MAX_EPOCHS = 100
# DEFAULT_BATCH_SIZE = 32
# MODEL_CHECKPOINT_PATH = "/models/checkpoints"


# ============================================================================
# FUNCTIONS - snake_case with descriptive action verbs
# ============================================================================

def load_dataset(path: str) -> list:
    """
    Functions use snake_case - all lowercase with underscores between words.
    
    Naming best practices:
    - Start with action verb (load, save, train, predict, validate)
    - Be descriptive but concise
    - Use full words, avoid abbreviations
    
    Good examples:
    ✓ load_dataset()     ✗ loadDataset() (camelCase)
    ✓ train_model()      ✗ trainModel() (camelCase) 
    ✓ calculate_loss()   ✗ calc_loss() (abbreviation)
    ✓ preprocess_data()  ✗ preprocessData() (camelCase)
    """
    # Local variables also use snake_case
    raw_data = []  # Clear, descriptive variable name
    
    with open(path, "r", encoding="utf-8") as f:
        for line in f:  # Short loop variables are acceptable
            raw_data.append(line.strip())
    return raw_data


# ============================================================================
# CLASSES - PascalCase (CapWords) for things/concepts
# ============================================================================

class DataLoader:
    """
    Classes use PascalCase - each word starts with capital letter, no underscores.
    
    Naming best practices:
    - Represent "things" or "concepts" (nouns)
    - Clear, descriptive names
    - Avoid abbreviations
    
    Good examples:
    ✓ DataLoader         ✗ dataLoader (camelCase)
    ✓ ModelTrainer       ✗ model_trainer (snake_case)
    ✓ FeatureExtractor   ✗ FeatExtractor (abbreviation)
    ✓ NeuralNetwork      ✗ neural_network (snake_case)
    """
    
    def __init__(self, data_path: str) -> None:
        """
        Instance attributes use snake_case.
        
        Attribute naming patterns:
        - Public attributes: regular snake_case (part of class interface)
        - Private attributes: _leading_underscore (internal implementation)
        """
        # Public attribute - part of the class's public interface
        self.data_path = data_path  # Users can access/modify this
        
        # Private attribute - internal implementation detail
        # Single underscore = "internal use" (Python convention, not enforced)
        self._cache = None  # Users shouldn't directly access this
        
        # More attribute examples:
        # self.batch_size = 32        # Public configuration
        # self.is_loaded = False      # Public state indicator
        # self._last_modified = None  # Private tracking variable

    def get(self) -> list:
        """
        Method names use snake_case like functions.
        
        Method naming follows same rules as functions:
        ✓ get_data()         ✗ getData() (camelCase)
        ✓ save_model()       ✗ saveModel() (camelCase)
        ✓ calculate_metrics() ✗ calculateMetrics() (camelCase)
        """
        if self._cache is None:
            # Accessing private attribute within the class is fine
            self._cache = load_dataset(self.data_path)
        return self._cache


# ============================================================================
# PRIVATE FUNCTIONS - Leading underscore for internal helpers
# ============================================================================

def _format_preview(items: list, n: int = 3) -> str:
    """
    Private/internal functions start with underscore.
    
    Use leading underscore for:
    - Helper functions not part of public API
    - Internal utilities
    - Implementation details
    
    Examples:
    ✓ _validate_input()    # Input validation helper
    ✓ _normalize_data()    # Internal data processing
    ✓ _log_debug_info()    # Internal logging utility
    ✓ _calculate_stats()   # Internal computation helper
    
    Convention meaning: "This is internal, don't use directly"
    """
    head = items[:n]  # Local variables still use snake_case
    return f"Preview({n}): {head}"


if __name__ == "__main__":
    print("=== Python Naming Conventions for MLOps ===")
    
    # Demonstrate each naming pattern
    print(f"Constant: LEARNING_RATE = {LEARNING_RATE}")
    
    # Create instances to show class naming
    loader = DataLoader("dummy_path.txt")
    print(f"Class: {loader.__class__.__name__} created")
    
    # Show private function usage
    sample_data = [1, 2, 3, 4, 5]
    preview = _format_preview(sample_data)
    print(f"Private function result: {preview}")
    
    print("\n=== Naming Convention Summary ===")
    print("✓ CONSTANTS: ALL_CAPS_WITH_UNDERSCORES")
    print("✓ functions: snake_case_with_verbs")
    print("✓ Classes: PascalCaseWithNouns")
    print("✓ variables: snake_case_descriptive")
    print("✓ _private: _leading_underscore_for_internals")
    
    print("\n=== Key Benefits for MLOps ===")
    print("• Consistent code style across team")
    print("• Clear distinction between public/private APIs")
    print("• Self-documenting variable purposes")
    print("• Easier code review and maintenance")
    print("• Better IDE support and autocompletion")
