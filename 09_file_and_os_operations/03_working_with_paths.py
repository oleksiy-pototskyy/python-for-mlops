#!/usr/bin/python3

"""
Working with Paths (pathlib) for MLOps - Educational Examples

Demonstrates modern path handling with pathlib:
- Path construction and manipulation
- File and directory existence checking
- Directory creation
- File operations with Path objects
- Cross-platform path handling
"""

from pathlib import Path

# ============================================================================
# PATH CONSTRUCTION - Modern, cross-platform path building
# ============================================================================

data_path = Path("data") / "raw" / "dataset.csv"
print(data_path)  # Outputs: data/raw/dataset.csv (or data\raw\dataset.csv on Windows)
# Path objects use '/' operator for joining - works on all platforms
# MLOps use: dataset paths, model directories, output locations

# ============================================================================
# PATH EXISTENCE CHECKING - Validate files and directories
# ============================================================================

if data_path.exists():
    print("Dataset is ready")
else:
    print("Dataset not found")
    # Path.exists() returns True if file or directory exists
    # MLOps use: validate datasets before training, check model files

# ============================================================================
# DIRECTORY CREATION - Create directory structures safely
# ============================================================================

log_dir = Path("logs")  # Create Path object for logs directory
log_dir.mkdir(parents=True, exist_ok=True)
# parents=True: create parent directories if they don't exist
# exist_ok=True: don't raise error if directory already exists
# MLOps use: create output directories, experiment folders, checkpoint dirs

# ============================================================================
# FILE OPERATIONS - Write and read files using Path methods
# ============================================================================

log_file = log_dir / "training.log"  # Construct file path
log_file.write_text("Training started...\n")  # Write text to file
# Path.write_text() creates file and writes content in one operation
# MLOps use: save logs, write configuration files, export results

# ============================================================================
# READING FILES - Read file content using Path methods
# ============================================================================

content = log_file.read_text()  # Read entire file as string
print(content)  # Display file content
# Path.read_text() reads entire file content in one operation
# MLOps use: load configurations, read experiment results, process logs



