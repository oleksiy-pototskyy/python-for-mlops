#!/usr/bin/python3

def demo_collections():
    # ============================================================================
    # LISTS - Mutable sequences for dynamic data (training batches, metrics, etc.)
    # ============================================================================
    print("=== LISTS - Dynamic Arrays for ML Data ===")
    
    # Lists are ordered, mutable collections - perfect for:
    # - Training loss history
    # - Batch processing queues
    # - Feature lists that change during preprocessing
    xs = [1, 2, 3]  # Initial loss values or feature indices
    
    # Adding single elements (new epoch loss, additional feature)
    xs.append(4)  # Add one item to end - O(1) operation
    print(f"After append(4): {xs}")
    
    # Adding multiple elements (batch of losses, feature engineering results)
    xs.extend([5, 6])  # Add multiple items - more efficient than multiple appends
    print(f"After extend([5, 6]): {xs}")
    
    # Modifying existing elements (updating hyperparameters, correcting data)
    xs[0] = 10  # Lists are mutable - can change values in-place
    print(f"After xs[0] = 10: {xs}")
    
    print(f"Final list: {xs}, length: {len(xs)}")
    # Output: [10, 2, 3, 4, 5, 6], length: 6
    
    # ============================================================================
    # TUPLES - Immutable sequences for fixed data (coordinates, RGB values, etc.)
    # ============================================================================
    print("\n=== TUPLES - Immutable Data Structures ===")
    
    # Tuples are ordered, immutable collections - ideal for:
    # - Model input/output shapes: (batch_size, features)
    # - Coordinate pairs: (x, y) or (latitude, longitude)
    # - Fixed configurations that shouldn't change
    point = (3, 4)  # Image coordinates, tensor dimensions
    
    # Tuple unpacking - elegant way to extract multiple values
    x, y = point  # Destructuring assignment - very Pythonic
    print(f"Tuple: {point}")
    print(f"Unpacked - x: {x}, y: {y}")
    
    # Common MLOps use case: unpacking model dimensions
    model_shape = (224, 224, 3)  # Height, Width, Channels for image models
    height, width, channels = model_shape
    print(f"Image shape - H: {height}, W: {width}, C: {channels}")
    
    # ============================================================================
    # DICTIONARIES - Key-value mappings for configurations and metadata
    # ============================================================================
    print("\n=== DICTIONARIES - Configuration and Metadata Storage ===")
    
    # Dicts are unordered (Python 3.7+ maintains insertion order), mutable
    # Perfect for:
    # - Model hyperparameters
    # - Experiment configurations
    # - Feature mappings
    # - Model metadata
    cfg = {"batch_size": 32, "lr": 0.001}  # Training configuration
    
    # Adding new key-value pairs (expanding configuration)
    cfg["epochs"] = 5  # Dynamic configuration updates
    cfg["optimizer"] = "adam"  # Adding new hyperparameters
    
    print(f"Configuration keys: {list(cfg.keys())}")
    # Output: ['batch_size', 'lr', 'epochs', 'optimizer']
    
    # Safe value retrieval with .get() - prevents KeyError
    learning_rate = cfg.get("lr")  # Returns value or None if key missing
    dropout_rate = cfg.get("dropout", 0.0)  # Default value if key missing
    print(f"Learning rate: {learning_rate}")
    print(f"Dropout rate (with default): {dropout_rate}")
    
    # Dictionary comprehension for data transformation
    scaled_cfg = {k: v * 2 if isinstance(v, (int, float)) else v for k, v in cfg.items()}
    print(f"Scaled numeric values: {scaled_cfg}")
    
    # ============================================================================
    # SETS - Unique collections for deduplication and membership testing
    # ============================================================================
    print("\n=== SETS - Unique Collections for Data Deduplication ===")
    
    # Sets are unordered collections of unique elements - excellent for:
    # - Removing duplicate samples
    # - Tracking processed file IDs
    # - Feature selection (unique feature names)
    # - Fast membership testing
    
    # Creating set from list automatically removes duplicates
    seen = set([1, 1, 2, 3])  # Duplicates automatically removed
    print(f"Set from [1, 1, 2, 3]: {seen}")
    # Output: {1, 2, 3} - order not guaranteed
    
    # Adding elements (tracking processed items)
    seen.add(3)  # Adding existing element has no effect
    seen.add(4)  # Adding new element
    print(f"After adding 3 and 4: {seen}")
    
    # Fast membership testing - O(1) average case vs O(n) for lists
    print(f"Contains 2? {2 in seen}")  # True
    print(f"Contains 5? {5 in seen}")  # False
    
    # Practical MLOps example: tracking processed file IDs
    processed_files = set()
    file_batch = ["img_001.jpg", "img_002.jpg", "img_001.jpg"]  # Duplicate!
    
    for file_id in file_batch:
        if file_id not in processed_files:
            print(f"Processing {file_id}")
            processed_files.add(file_id)
        else:
            print(f"Skipping duplicate {file_id}")
    
    print(f"Total unique files processed: {len(processed_files)}")

if __name__ == "__main__":
    # Execute demo when script is run directly
    # Standard Python pattern for executable modules
    demo_collections()
