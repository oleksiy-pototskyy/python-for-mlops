# Python Testing for MLOps

Comprehensive testing examples demonstrating essential patterns for reliable MLOps development.

## 📁 Project Structure

```
12_testing/
├── src/                    # Source code under test
│   ├── math_ops.py        # Basic functions for testing fundamentals
│   ├── net_client.py      # External dependencies (time, HTTP)
│   └── text_utils.py      # Class-based code for OOP testing
├── tests/                 # Test files
│   ├── conftest.py        # Shared pytest fixtures
│   ├── test_*.py          # Individual test modules
│   └── ...
└── README.md
```

## 🚀 Quick Start

### Install Dependencies
```bash
pip install pytest requests
```

### Run All Tests
```bash
# Run all tests with verbose output
pytest -v

# Run tests quietly
pytest -q
```

### Run Specific Tests
```bash
# Run single test file
pytest tests/test_math_ops_pytest.py

# Run unittest style directly
python -m tests.test_math_ops_unittest

# Run tests matching pattern
pytest -k "parametrize"
```

## 📚 Testing Concepts Covered

### 1. **Basic Testing Patterns**
- **Function vs Class Tests** (`test_classes_vs_functions.py`)
- **Pytest vs Unittest** (`test_math_ops_pytest.py` vs `test_math_ops_unittest.py`)
- **Simple Assertions** - Plain `assert` statements for clear, readable tests

### 2. **Advanced Testing Features**
- **Fixtures** (`test_fixtures.py`, `conftest.py`) - Reusable test setup and data
- **Parametrization** (`test_parametrize.py`) - Test multiple inputs efficiently
- **Mocking & Patching** (`test_mocks_patches.py`) - Isolate external dependencies

### 3. **Test Organization**
- **Shared Fixtures** (`conftest.py`) - Central test configuration
- **Test Discovery** - Automatic test detection by pytest
- **Failure Output** (`test_failure_output.py`) - Rich diff reporting

## 🔧 MLOps Testing Best Practices

### ✅ Do's
- **Keep tests fast** - Mock external calls (network, file I/O)
- **Test edge cases** - Use parametrization for comprehensive coverage
- **Use fixtures** - Share expensive setup (model loading, data preparation)
- **Clear assertions** - Use plain `assert` for readable test failures
- **Isolate tests** - Each test should be independent

### ❌ Don'ts
- **Avoid real external calls** - Mock APIs, databases, file systems
- **Don't test implementation details** - Focus on behavior, not internals
- **Avoid complex test logic** - Tests should be simple and obvious
- **Don't share state** - Tests should not depend on each other

## 🎯 MLOps-Specific Testing Scenarios

### Model Testing
```python
# Test model predictions
def test_model_predictions(trained_model, sample_data):
    predictions = trained_model.predict(sample_data)
    assert len(predictions) == len(sample_data)
    assert all(0 <= p <= 1 for p in predictions)  # Probability bounds
```

### Data Pipeline Testing
```python
# Test data transformations
@pytest.mark.parametrize("input_data,expected", [
    ([1, 2, 3], [0.1, 0.2, 0.3]),  # Normalization
    ([0, 0, 0], [0.0, 0.0, 0.0]),  # Edge case
])
def test_normalize_data(input_data, expected):
    result = normalize(input_data)
    assert result == expected
```

### API Testing
```python
# Mock external API calls
def test_fetch_model_metadata(mock_requests):
    mock_requests.get.return_value.json.return_value = {"version": "1.0"}
    metadata = fetch_model_metadata("model-123")
    assert metadata["version"] == "1.0"
```

## 🛠 Useful Commands

```bash
# Run tests with different verbosity levels
pytest -v                    # Verbose output
pytest -s                    # Show print statements
pytest --tb=short           # Short traceback format

# Run specific test patterns
pytest -k "test_add"         # Tests containing "test_add"
pytest tests/test_fixtures.py::test_cleaner_fixture  # Specific test

# Generate coverage report
pytest --cov=src --cov-report=html

# Run tests in parallel (with pytest-xdist)
pytest -n auto
```

## 📋 Test File Examples

| File | Purpose | Key Concepts |
|------|---------|-------------|
| `test_math_ops_pytest.py` | Basic pytest patterns | Simple assertions, fixtures |
| `test_parametrize.py` | Multiple test inputs | `@pytest.mark.parametrize` |
| `test_mocks_patches.py` | External dependencies | `unittest.mock`, `patch` |
| `test_fixtures.py` | Reusable test setup | Custom and built-in fixtures |
| `test_classes_vs_functions.py` | Test organization | Function vs class-based tests |

## 🔍 Debugging Failed Tests

1. **Run single failing test**: `pytest tests/test_file.py::test_function -v`
2. **Use pytest debugger**: `pytest --pdb`
3. **Check failure output**: Remove `@pytest.mark.skip` from `test_failure_output.py`
4. **Add print statements**: Use `pytest -s` to see output

## 📦 Dependencies

```text
pytest>=7.0.0
requests>=2.25.0
```

---

**💡 Remember**: Good tests are the foundation of reliable MLOps systems. They catch bugs early, enable confident refactoring, and serve as living documentation of your code's behavior.