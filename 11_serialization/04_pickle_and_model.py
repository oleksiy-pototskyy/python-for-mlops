#!/usr/bin/python3

"""
Pickle and Model/Object Serialization for MLOps - Educational Examples

Demonstrates pickle serialization essential for MLOps:
- Binary serialization of Python objects
- Preserving complex object state
- Model persistence and deployment
- Complete object reconstruction
"""

import pickle

# ============================================================================
# BASIC PICKLE SERIALIZATION - Binary format for Python objects
# ============================================================================

data = {"experiment": "A1", "accuracy": 0.95}  # Python dictionary
# Pickle can serialize any Python object (unlike JSON/YAML)
# MLOps use: experiment results, complex data structures, custom objects

# Save object
with open("result.pkl", "wb") as f:  # 'wb' = write binary mode
    pickle.dump(data, f)  # Serialize Python object to binary format
    # Pickle preserves exact Python object structure and types
    # More efficient than text formats for complex objects

# Load object
with open("result.pkl", "rb") as f:  # 'rb' = read binary mode
    loaded = pickle.load(f)  # Deserialize binary data back to Python object
    # Reconstructs exact original object with all attributes

print(loaded)  # {'experiment': 'A1', 'accuracy': 0.95}
# MLOps use: restore experiment data, load processed datasets

# ============================================================================
# MODEL SERIALIZATION - Save trained ML models for deployment
# ============================================================================

from sklearn.ensemble import RandomForestClassifier
import pickle

# Create and train model
model = RandomForestClassifier()  # Create ML model instance
model.fit([[1, 2], [3, 4]], [0, 1])  # Train model with sample data
# Model now contains learned parameters, tree structures, etc.
# MLOps use: trained models ready for deployment

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)  # Serialize entire trained model
    # Saves all model parameters, hyperparameters, and internal state
    # MLOps use: model deployment, model versioning, backup trained models

# Load model
with open("model.pkl", "rb") as f:
    loaded_model = pickle.load(f)  # Restore complete trained model
    # Model ready for predictions without retraining
    # MLOps use: deploy models, load for inference, model serving


