#!/usr/bin/python3

"""
Subprocess & Shell Commands for MLOps - Educational Examples

Demonstrates executing external commands from Python:
- Running commands and capturing output
- Direct command execution
- Handling stdout and stderr
- Error checking and exceptions
- Shell command execution
- Asynchronous process management
"""

import subprocess

# ============================================================================
# CAPTURING COMMAND OUTPUT - Run command and get results
# ============================================================================

result = subprocess.run(["echo", "Hello MLOps"], capture_output=True, text=True)
print(result.stdout)  # Print captured output
# capture_output=True: capture stdout and stderr
# text=True: return strings instead of bytes
# MLOps use: run data processing scripts, get system info, execute ML tools

# ============================================================================
# DIRECT COMMAND EXECUTION - Run command without capturing output
# ============================================================================

subprocess.run(["ls", "-l"])  # Command output goes directly to terminal
# No capture_output - output displayed immediately
# MLOps use: run training scripts, system commands, file operations

# ============================================================================
# HANDLING STDOUT AND STDERR - Separate output and error streams
# ============================================================================

result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print("Output:", result.stdout)  # Standard output
print("Errors:", result.stderr)  # Standard error (if any)
# MLOps use: check tool versions, validate installations, debug command issues

# ============================================================================
# ERROR CHECKING - Handle command failures with exceptions
# ============================================================================

subprocess.run(["false"], check=True)  # Will raise CalledProcessError
# check=True: raise exception if command returns non-zero exit code
# MLOps use: ensure critical commands succeed, fail fast on errors

# ============================================================================
# SHELL COMMAND EXECUTION - Run complex shell commands
# ============================================================================

subprocess.run("echo $HOME && pwd", shell=True)  # Execute shell command string
# shell=True: interpret command through system shell
# Allows shell features: pipes, variables, command chaining
# MLOps use: complex data pipelines, environment setup, batch operations

# ============================================================================
# ASYNCHRONOUS PROCESS MANAGEMENT - Non-blocking command execution
# ============================================================================

process = subprocess.Popen(["sleep", "5"])  # Start process without waiting
process.wait()  # Wait for process to complete
# Popen: start process asynchronously
# wait(): block until process finishes
# MLOps use: long-running training jobs, parallel processing, background tasks



