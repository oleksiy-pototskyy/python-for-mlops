#!/usr/bin/python3

"""
Python Collections for MLOps - Educational Examples

Demonstrates the four core collection types essential for MLOps:
- Lists: ordered, mutable sequences (datasets, metrics)
- Tuples: ordered, immutable sequences (shapes, coordinates)
- Sets: unordered, unique collections (labels, processed IDs)
- Dictionaries: key-value mappings (configs, metadata)
"""

def demo_values():
    """
    Demonstrates Python collections with practical MLOps use cases.
    """
    
    # ============================================================================
    # LISTS - Ordered, mutable sequences for dynamic data
    # ============================================================================
    
    # Lists store ordered collections that can be modified
    # Perfect for: file lists, training metrics, batch data, feature names
    files = ["train.csv", "test.csv", "validate.csv"]
    
    # Access elements by index (0-based)
    print(files[0])      # train.csv - first element
    # MLOps use: access specific dataset splits, get first/last metrics
    
    # Lists are mutable - can add, remove, modify elements
    files.append("logs.csv")  # Add new file to the list
    # Output: ["train.csv", "test.csv", "validate.csv", "logs.csv"]
    # MLOps use: dynamically add new data files, accumulate training losses
    
    # More list operations for MLOps:
    # files.extend(["model.pkl", "config.json"])  # Add multiple files
    # files.remove("logs.csv")  # Remove specific file
    # files[1] = "test_v2.csv"  # Replace element
    # len(files)  # Get number of files
    
    # ============================================================================
    # TUPLES - Ordered, immutable sequences for fixed data
    # ============================================================================
    
    # Tuples store ordered collections that CANNOT be modified
    # Perfect for: image dimensions, model shapes, coordinates, RGB values
    shape = (224, 224, 3)  # Height, Width, Channels for image models
    
    # Access elements like lists, but cannot modify
    # height = shape[0]  # 224
    # width = shape[1]   # 224
    # channels = shape[2] # 3
    
    # Tuple unpacking - elegant way to extract values
    # height, width, channels = shape
    
    # MLOps use cases:
    # - Model input/output shapes: (batch_size, sequence_length, features)
    # - Image dimensions: (height, width, channels)
    # - Coordinate pairs: (latitude, longitude)
    # - Version numbers: (major, minor, patch)
    
    # ============================================================================
    # SETS - Unordered collections of unique elements
    # ============================================================================
    
    # Sets automatically remove duplicates and provide fast membership testing
    # Perfect for: unique labels, processed file IDs, feature selection
    labels = {"cat", "dog", "fish"}  # Unique class labels
    
    # Add elements (duplicates ignored)
    labels.add("bird")  # Adds "bird" to the set
    # labels.add("cat")   # Would do nothing - "cat" already exists
    
    # Fast membership testing - O(1) average case vs O(n) for lists
    # has_cat = "cat" in labels  # True - very fast lookup
    
    # MLOps use cases:
    # - Track unique class labels in dataset
    # - Remove duplicate samples: set(sample_ids)
    # - Fast lookup of processed file IDs
    # - Feature selection: intersection of feature sets
    # - Data validation: ensure no duplicate entries
    
    # ============================================================================
    # DICTIONARIES - Key-value mappings for structured data
    # ============================================================================
    
    # Dictionaries store key-value pairs for fast lookups
    # Perfect for: configurations, hyperparameters, metadata, mappings
    config = {"lr": 0.01, "batch_size": 32, "optimizer": "adam"}
    
    # Access values by key
    print(config["lr"])  # 0.01 - get learning rate
    # Fast O(1) average case lookup by key
    
    # Safe access with .get() method (returns None if key missing)
    # dropout = config.get("dropout", 0.0)  # Returns 0.0 if "dropout" not found
    
    # Add or modify key-value pairs
    # config["epochs"] = 100  # Add new hyperparameter
    # config["lr"] = 0.001    # Update existing value
    
    # MLOps use cases:
    # - Model hyperparameters: {"lr": 0.01, "batch_size": 32}
    # - Experiment metadata: {"model_type": "transformer", "dataset": "imdb"}
    # - Feature mappings: {"feature_1": "age", "feature_2": "income"}
    # - Model registry: {"model_id": "path/to/model.pkl"}
    # - Performance metrics: {"accuracy": 0.95, "f1_score": 0.87}
    
    # ============================================================================
    # PRACTICAL MLOPS COLLECTION PATTERNS
    # ============================================================================
    
    print("\n=== Practical MLOps Collection Examples ===")
    
    # Training metrics accumulation (list)
    training_losses = [0.8, 0.6, 0.4, 0.3, 0.25]  # Loss per epoch
    print(f"Final loss: {training_losses[-1]}")  # Get last loss
    
    # Model architecture definition (tuple)
    layer_sizes = (784, 256, 128, 10)  # Input -> Hidden -> Hidden -> Output
    print(f"Input size: {layer_sizes[0]}, Output size: {layer_sizes[-1]}")
    
    # Unique class discovery (set)
    all_predictions = ["cat", "dog", "cat", "bird", "dog", "fish"]
    unique_classes = set(all_predictions)  # Removes duplicates
    print(f"Unique classes found: {len(unique_classes)}")
    
    # Experiment configuration (dictionary)
    experiment = {
        "model_name": "resnet50",
        "dataset": "cifar10",
        "batch_size": 64,
        "learning_rate": 0.001,
        "epochs": 50
    }
    print(f"Training {experiment['model_name']} for {experiment['epochs']} epochs")


if __name__ == "__main__":
    print("=== Python Collections for MLOps Demo ===")
    demo_values()
    
    print("\n=== Collection Type Summary ===")
    print("✓ Lists []: ordered, mutable - for dynamic data (metrics, files)")
    print("✓ Tuples (): ordered, immutable - for fixed data (shapes, coords)")
    print("✓ Sets {}: unordered, unique - for deduplication (labels, IDs)")
    print("✓ Dicts {key: value}: key-value mapping - for configs, metadata")
    
    print("\n=== Key MLOps Use Cases ===")
    print("• Lists: training metrics, file paths, batch data")
    print("• Tuples: model shapes, image dimensions, coordinates")
    print("• Sets: unique labels, processed IDs, feature selection")
    print("• Dicts: hyperparameters, experiment configs, model metadata")
