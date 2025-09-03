#!/usr/bin/python3

"""
Python Naming Conventions for MLOps - Practical Demonstration

This script demonstrates all naming conventions covered in the video lecture
with practical MLOps examples that show why good naming matters.
"""

# ============================================================================
# CONSTANTS - UPPER_CASE with underscores (module-level configuration)
# ============================================================================

# Constants use ALL_CAPS to show they shouldn't be changed during execution
DEFAULT_BATCH_SIZE = 32  # Standard batch size for training
MAX_EPOCHS = 50          # Maximum training epochs
LEARNING_RATE = 0.001    # Default learning rate

# More MLOps constants
MODEL_CHECKPOINT_DIR = "/models/checkpoints"
VALIDATION_SPLIT = 0.2
EARLY_STOPPING_PATIENCE = 10


# ============================================================================
# VARIABLES AND FUNCTIONS - snake_case (lowercase with underscores)
# ============================================================================

def load_dataset(file_path):
    """
    Functions use snake_case - lowercase with underscores between words.
    
    Good: load_dataset(), train_model(), calculate_accuracy()
    Bad: LoadDataset(), trainModel(), calcAcc()
    """
    # Variables also use snake_case
    training_data_path = file_path  # Good: descriptive and clear
    # x = file_path                 # Bad: unclear what x represents
    
    raw_data = []  # Good: specific about data state
    # data = []    # Bad: too generic, unclear what kind of data
    
    return raw_data

def preprocess_features(input_data):
    """Process and clean feature data for training."""
    clean_data = []      # Good: describes data state
    processed_samples = 0  # Good: clear counter purpose
    
    for sample in input_data:
        # Good variable names in loops
        cleaned_sample = sample.strip().lower()
        clean_data.append(cleaned_sample)
        processed_samples += 1
    
    return clean_data, processed_samples

def calculate_model_accuracy(predictions, true_labels):
    """Calculate accuracy metrics for model evaluation."""
    correct_predictions = 0
    total_samples = len(predictions)
    
    for pred, true_label in zip(predictions, true_labels):
        if pred == true_label:
            correct_predictions += 1
    
    accuracy_score = correct_predictions / total_samples
    return accuracy_score


# ============================================================================
# CLASSES - PascalCase (each word starts with capital letter)
# ============================================================================

class DataLoader:
    """
    Classes use PascalCase to separate them from functions and variables.
    
    Good: DataLoader, ModelTrainer, FeatureExtractor
    Bad: dataLoader, model_trainer, featureextractor
    """
    
    def __init__(self, data_path):
        # Instance variables use snake_case
        self.data_path = data_path
        self.batch_size = DEFAULT_BATCH_SIZE
        self.is_loaded = False
        
        # Private attributes start with underscore
        self._cache = None
        self._last_modified = None
    
    def get_batch(self, batch_index):
        """Method names use snake_case like functions."""
        return f"Batch {batch_index} from {self.data_path}"

class ModelTrainer:
    """Handles model training with proper naming conventions."""
    
    def __init__(self, model_config):
        self.model_config = model_config
        self.training_history = []
        self.current_epoch = 0
        
        # Private methods and attributes
        self._best_loss = float('inf')
        self._early_stop_counter = 0
    
    def train_epoch(self, training_data, validation_data):
        """Train model for one epoch."""
        epoch_loss = self._calculate_epoch_loss(training_data)
        validation_loss = self._validate_model(validation_data)
        
        self.current_epoch += 1
        self.training_history.append({
            'epoch': self.current_epoch,
            'train_loss': epoch_loss,
            'val_loss': validation_loss
        })
        
        return epoch_loss, validation_loss
    
    def _calculate_epoch_loss(self, data):
        """Private method - internal implementation detail."""
        # Simplified loss calculation
        return 0.5 / (self.current_epoch + 1)
    
    def _validate_model(self, validation_data):
        """Private method for model validation."""
        return 0.6 / (self.current_epoch + 1)

class FeatureExtractor:
    """Extracts and processes features from raw data."""
    pass


# ============================================================================
# PRIVATE/INTERNAL FUNCTIONS - Leading underscore
# ============================================================================

def _internal_helper(data):
    """
    Private functions start with underscore to show internal use.
    
    This convention tells other developers: "Don't use this directly,
    it's an implementation detail that might change."
    """
    processed_data = []
    for item in data:
        processed_data.append(item.upper())
    return processed_data

def _validate_config(config_dict):
    """Internal function to validate configuration."""
    required_keys = ['learning_rate', 'batch_size', 'epochs']
    return all(key in config_dict for key in required_keys)

def _sanitize_filename(filename):
    """Internal utility to clean file names."""
    return filename.replace(" ", "_").lower()


# ============================================================================
# GOOD vs BAD NAMING EXAMPLES
# ============================================================================

def demonstrate_naming_examples():
    """Shows good and bad naming practices with MLOps examples."""
    
    print("=== Good vs Bad Naming Examples ===")
    
    # GOOD: Descriptive variable names
    training_data_path = "data/train.csv"
    validation_data_path = "data/val.csv"
    model_checkpoint_path = "/models/best_model.pkl"
    
    # BAD: Unclear variable names (commented out)
    # x = "data/train.csv"        # What is x?
    # data = "data/val.csv"       # What kind of data?
    # path = "/models/best_model.pkl"  # Path to what?
    
    print(f"Training data: {training_data_path}")
    print(f"Validation data: {validation_data_path}")
    print(f"Model checkpoint: {model_checkpoint_path}")
    
    # GOOD: Specific data state names
    raw_data = ["sample1", "sample2", "sample3"]
    clean_data = [item.strip() for item in raw_data]
    processed_features = [len(item) for item in clean_data]
    
    # BAD: Generic names (commented out)
    # data = ["sample1", "sample2", "sample3"]  # Too generic
    # data2 = [item.strip() for item in data]   # What's data2?
    # result = [len(item) for item in data2]    # Result of what?
    
    print(f"Raw samples: {len(raw_data)}")
    print(f"Clean samples: {len(clean_data)}")
    print(f"Feature count: {len(processed_features)}")
    
    # GOOD: Boolean variables with clear intent
    is_training_complete = False
    has_validation_data = True
    can_save_checkpoint = True
    should_early_stop = False
    
    print(f"Training complete: {is_training_complete}")
    print(f"Has validation: {has_validation_data}")


def avoid_python_keywords():
    """Demonstrates avoiding Python built-in names."""
    
    print("\n=== Avoiding Python Keywords ===")
    
    # GOOD: Don't override built-ins
    data_list = [1, 2, 3, 4, 5]        # Good: specific name
    config_dict = {"lr": 0.01}         # Good: specific name
    sample_id = "sample_001"            # Good: specific name
    
    # BAD: Overriding built-ins (commented out - would cause problems)
    # list = [1, 2, 3, 4, 5]           # Bad: overwrites built-in list()
    # dict = {"lr": 0.01}               # Bad: overwrites built-in dict()
    # id = "sample_001"                 # Bad: overwrites built-in id()
    
    print(f"Data list length: {len(data_list)}")
    print(f"Config keys: {list(config_dict.keys())}")  # list() still works
    print(f"Sample ID: {sample_id}")


if __name__ == "__main__":
    print("=== Python Naming Conventions for MLOps ===")
    
    # Demonstrate the naming conventions
    print(f"Constants: DEFAULT_BATCH_SIZE = {DEFAULT_BATCH_SIZE}")
    print(f"Constants: MAX_EPOCHS = {MAX_EPOCHS}")
    
    # Create instances with proper class names
    loader = DataLoader("data/train.csv")
    trainer = ModelTrainer({"lr": LEARNING_RATE, "batch_size": DEFAULT_BATCH_SIZE})
    
    print(f"Created {loader.__class__.__name__} instance")
    print(f"Created {trainer.__class__.__name__} instance")
    
    # Show function naming
    sample_data = ["  Sample 1  ", "  Sample 2  "]
    processed_data, count = preprocess_features(sample_data)
    print(f"Processed {count} samples")
    
    # Demonstrate good vs bad naming
    demonstrate_naming_examples()
    avoid_python_keywords()
    
    print("\n=== Key Naming Rules ===")
    print("✓ variables, functions: snake_case")
    print("✓ CONSTANTS: UPPER_CASE")
    print("✓ Classes: PascalCase")
    print("✓ modules/files: lowercase_with_underscores.py")
    print("✓ _private: _leading_underscore")
    print("✓ Be descriptive but not too long")
    print("✓ Avoid Python keywords and built-ins")