#!/usr/bin/python3

"""
Python Strings for MLOps - Educational Examples

Demonstrates string operations essential for MLOps workflows:
- File paths and names
- Log processing
- Configuration parsing
- Data validation
"""

def demo_values():
    """
    Demonstrates Python string operations with MLOps use cases.
    """
    
    # ============================================================================
    # STRING CREATION - Different quote styles for different purposes
    # ============================================================================
    
    # Double quotes - most common, allows single quotes inside
    dataset = "customers.csv"  # File names, paths
    
    # Single quotes - when string contains double quotes
    message = 'Training finished'  # Log messages, status updates
    
    # Triple quotes - multi-line strings for documentation, SQL, etc.
    description = """This is a multi-line string"""  # Model descriptions, configs
    
    print("=== String Creation ===")
    print(f"Dataset: {dataset}")
    print(f"Message: {message}")
    print(f"Description: {description}")
    
    # ============================================================================
    # STRING CONCATENATION - Combining strings (avoid + in production)
    # ============================================================================
    
    project = "MLOps"
    status = "running"
    
    # String concatenation with + operator
    # Note: Inefficient for many operations, use f-strings instead
    print("\n=== String Concatenation ===")
    print(project + " is " + status)  # Basic concatenation
    # Better: print(f"{project} is {status}")  # f-string (more efficient)
    
    # ============================================================================
    # STRING LENGTH - Useful for validation and limits
    # ============================================================================
    
    name = "pipeline"
    print("\n=== String Length ===")
    print(f"Pipeline name '{name}' has {len(name)} characters")  # 8 characters
    # MLOps use: validate model names, check path lengths, limit log messages
    
    # ============================================================================
    # STRING INDEXING - Accessing individual characters
    # ============================================================================
    
    text = "model"
    print("\n=== String Indexing ===")
    print(f"First character: {text[0]}")   # 'm' - index 0 (first)
    print(f"Last character: {text[-1]}")   # 'l' - index -1 (last)
    # MLOps use: extract file extensions, check prefixes/suffixes
    
    # ============================================================================
    # STRING SLICING - Extracting substrings
    # ============================================================================
    
    print("\n=== String Slicing ===")
    print(f"First 3 characters: {text[0:3]}")  # 'mod' - characters 0,1,2
    # Slicing syntax: string[start:end] (end is exclusive)
    # MLOps use: extract model prefixes, parse version numbers, truncate logs
    
    # ============================================================================
    # STRING CLEANING - Essential for log processing and data validation
    # ============================================================================
    
    log = "  ERROR: file not found  "  # Raw log entry with whitespace
    print("\n=== String Cleaning ===")
    
    # Remove leading/trailing whitespace - critical for data cleaning
    cleaned_log = log.strip()
    print(f"Original: '{log}'")
    print(f"Stripped: '{cleaned_log}'")
    
    # Convert to lowercase - for case-insensitive comparisons
    lower_log = log.lower()
    print(f"Lowercase: '{lower_log}'")
    # MLOps use: normalize file names, standardize labels, process user input
    
    # Replace text - useful for log sanitization and data transformation
    warning_log = log.replace("ERROR", "WARNING")
    print(f"Replaced: '{warning_log}'")
    # MLOps use: sanitize sensitive data, standardize formats, fix common typos
    
    # ============================================================================
    # STRING SPLITTING - Parse paths, configs, and structured data
    # ============================================================================
    
    path = "data/train/images"  # Typical MLOps file path
    print("\n=== String Splitting ===")
    path_parts = path.split("/")  # Split on delimiter
    print(f"Path: {path}")
    print(f"Parts: {path_parts}")  # ['data', 'train', 'images']
    # MLOps use: parse file paths, extract directory names, process CSV data
    
    # Practical example: extract components
    data_dir = path_parts[0]      # 'data'
    split_type = path_parts[1]    # 'train'
    data_type = path_parts[2]     # 'images'
    print(f"Data dir: {data_dir}, Split: {split_type}, Type: {data_type}")
    
    # ============================================================================
    # STRING MEMBERSHIP - Check if substring exists (case-sensitive)
    # ============================================================================
    
    print("\n=== String Membership ===")
    has_error = "error" in log.lower()  # Case-insensitive search
    print(f"Log contains 'error': {has_error}")  # True
    # MLOps use: filter logs by level, validate file types, check configurations
    
    # More membership examples:
    is_csv = ".csv" in dataset.lower()  # Check file extension
    is_training = "train" in path       # Check if training data
    print(f"Is CSV file: {is_csv}")
    print(f"Is training path: {is_training}")
    
    # ============================================================================
    # STRING IMMUTABILITY - Strings don't change, methods return new strings
    # ============================================================================
    
    text = "model"
    new_text = text.upper()  # Creates NEW string, doesn't modify original
    print("\n=== String Immutability ===")
    print(f"Original: {text}")      # 'model' - unchanged!
    print(f"Uppercase: {new_text}")  # 'MODEL' - new string
    # Important: String methods return new strings, original stays the same
    
    # ============================================================================
    # PRACTICAL MLOPS STRING PATTERNS
    # ============================================================================
    
    print("\n=== Practical MLOps String Patterns ===")
    
    # File extension checking
    filename = "model_v2.pkl"
    is_pickle = filename.endswith(".pkl")
    print(f"Is pickle file: {is_pickle}")
    
    # Model name validation
    model_name = "bert-base-uncased"
    is_valid_name = "-" in model_name and len(model_name) > 5
    print(f"Valid model name: {is_valid_name}")
    
    # Log level extraction
    log_entry = "[INFO] Model training completed successfully"
    if log_entry.startswith("[INFO]"):
        level = "INFO"
        message = log_entry[6:].strip()  # Remove "[INFO]" and whitespace
        print(f"Log level: {level}, Message: {message}")
    
    # Configuration parsing
    config_line = "learning_rate=0.001"
    key, value = config_line.split("=")  # Split on equals sign
    print(f"Config - {key}: {value}")

if __name__ == "__main__":
    print("=== Python Strings for MLOps Demo ===")
    demo_values()
    
    print("\n=== Key String Concepts ===")
    print("✓ Strings are immutable - methods return new strings")
    print("✓ Use strip() to clean whitespace from data")
    print("✓ Use split() to parse paths and structured data")
    print("✓ Use 'in' operator for substring searches")
    print("✓ Use lower()/upper() for case-insensitive operations")
    print("✓ Use slicing [start:end] to extract parts")
    print("✓ Prefer f-strings over + concatenation for performance")
