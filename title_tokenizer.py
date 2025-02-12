
from transformers import AutoTokenizer
import pandas as pd

# Load dataset from CSV files
train_df = pd.read_csv("data/balanced_train_data.csv")
test_df = pd.read_csv("data/balanced_test_data.csv")

# Initialize pre-trained DistilBERT tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    pretrained_model_name_or_path='distilbert-base-uncased'
)

def tokenize_data(texts, tokenizer, max_length=128):
    """
    Tokenize input texts using the specified tokenizer.

    Args:
        texts (list): List of input text strings.
        max_length (int): Maximum sequence length. Defaults to 128.

    Returns:
        dict: Dictionary containing tokenized input tensors.
    """
    # Tokenize input texts with padding and truncation
    return tokenizer(
        texts,
        padding=True,  # Add [PAD] tokens when sequences are too long
        truncation=True,  # Truncate sequences that exceed max length
        max_length=max_length,  # Set maximum sequence length
        return_tensors='pt'  # Return tensors in PyTorch format
    )

# Tokenize titles from training and testing datasets
train_title_encodings = tokenize_data(train_df['title'].tolist(), tokenizer=tokenizer)
test_title_encodings = tokenize_data(test_df['title'].tolist(), tokenizer=tokenizer)

print(f"Train encodings: {train_title_encodings}")
print(f"Test encodings: {test_title_encodings}")
