#!/usr/bin/python3

"""
File I/O for MLOps - Educational Examples

Demonstrates file operations essential for MLOps:
- Basic file reading and writing
- Context managers for safe file handling
- Line-by-line processing
- Writing multiple lines
- Binary file operations
"""

# ============================================================================
# BASIC FILE OPERATIONS - Manual file handling (not recommended)
# ============================================================================

# Writing a file - manual approach
f = open("example.txt", "w")  # Open file in write mode
f.write("Hello MLOps")        # Write content to file
f.close()                     # Must manually close file
# Problem: file not closed if error occurs
# MLOps use: saving configurations, logging results

# Reading a file - manual approach
f = open("example.txt", "r")  # Open file in read mode
content = f.read()            # Read entire file content
print(content)                # Display content
f.close()                     # Must manually close file
# Problem: resource leak if close() not called
# MLOps use: loading datasets, reading model parameters

# ============================================================================
# CONTEXT MANAGERS - Safe file handling (recommended)
# ============================================================================

with open("example.txt", "r") as f:
    content = f.read()  # Read file content
    print(content)      # Process content
    # File automatically closed when exiting 'with' block
    # Even if exception occurs, file is properly closed
    # MLOps use: safe file operations, guaranteed cleanup

# ============================================================================
# LINE-BY-LINE PROCESSING - Memory-efficient for large files
# ============================================================================

with open("data.log", "r") as f:
    for line in f:          # Iterate through file line by line
        print(line.strip()) # Remove newline characters
        # Memory efficient - doesn't load entire file at once
        # MLOps use: processing large log files, streaming data

# ============================================================================
# WRITING MULTIPLE LINES - Batch file operations
# ============================================================================

lines = ["first line\n", "second line\n", "third line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)  # Write list of strings to file
    # Each string should include newline character if needed
    # MLOps use: saving experiment results, writing processed data

# ============================================================================
# BINARY FILE OPERATIONS - Handle non-text data
# ============================================================================

with open("model.pkl", "wb") as f:  # 'wb' = write binary mode
    f.write(b"binary data")          # Write bytes object
    # Binary mode for non-text files (models, images, etc.)
    # MLOps use: saving trained models, serialized objects, image data


