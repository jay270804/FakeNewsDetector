from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from dataset import train_dataset, test_dataset
from title_tokenizer import tokenizer

model = AutoModelForSequenceClassification.from_pretrained(
    'distilbert-base-uncased',
    num_labels=2
)

training_args = TrainingArguments(
    output_dir="./model_training_data/results",
    eval_strategy='epoch',
    save_strategy='epoch',
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    gradient_accumulation_steps = 2,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./model_training_data/logs',
    logging_steps=10,
    load_best_model_at_end=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

trainer.train()

# Save the model and tokenizer after training
model_save_dir = "./saved_model"
trainer.model.save_pretrained(model_save_dir)
tokenizer.save_pretrained(model_save_dir)

print(f"Model and tokenizer saved to {model_save_dir}")