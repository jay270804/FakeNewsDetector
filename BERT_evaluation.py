from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from title_tokenizer import test_df, tokenize_data
from dataset import NewsDataset

# Load the saved model and tokenizer
model_save_dir = "./saved_model"
model = AutoModelForSequenceClassification.from_pretrained(model_save_dir)
tokenizer = AutoTokenizer.from_pretrained(model_save_dir)

# Tokenize the test data
test_encodings = tokenize_data(test_df['title'].tolist(), tokenizer=tokenizer)
test_dataset = NewsDataset(test_encodings, test_df['label'].tolist())

# Generate predictions
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

pred_labels = []
true_labels = []

with torch.no_grad():
    for batch in torch.utils.data.DataLoader(test_dataset, batch_size=8):
        # Exclude the 'label' key from the inputs
        inputs = {key: val.to(device) for key, val in batch.items() if key != 'label'}
        outputs = model(**inputs)
        logits = outputs.logits
        batch_preds = torch.argmax(logits, dim=-1).cpu().numpy()
        pred_labels.extend(batch_preds)
        true_labels.extend(batch['label'].cpu().numpy())

# Calculate metrics
accuracy = accuracy_score(true_labels, pred_labels)
precision = precision_score(true_labels, pred_labels)
recall = recall_score(true_labels, pred_labels)
f1 = f1_score(true_labels, pred_labels)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")