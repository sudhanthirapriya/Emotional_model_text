import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# Load your dataset
df = pd.read_csv('sampled_data_with_one_emotion.csv')

# Mapping emotions to labels
emotion_to_label = {emotion: idx for idx, emotion in enumerate(df['emotion'].unique())}
df['label'] = df['emotion'].map(emotion_to_label)

# Split data into train and validation sets
train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

# Load the tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

# Tokenize the text data
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

# Convert pandas DataFrame to Hugging Face Dataset
train_dataset = Dataset.from_pandas(train_df)
val_dataset = Dataset.from_pandas(val_df)

# Apply the tokenizer to the datasets
train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)

# Set the format of the datasets to return PyTorch tensors
train_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])
val_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])

# Load the model
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=len(emotion_to_label))

# Set up training arguments
training_args = TrainingArguments(
    output_dir='./results',          # output directory
    evaluation_strategy="epoch",     # evaluate at the end of each epoch
    learning_rate=2e-5,              # learning rate
    per_device_train_batch_size=8,   # batch size for training
    per_device_eval_batch_size=8,    # batch size for evaluation
    num_train_epochs=3,              # number of training epochs
    weight_decay=0.01,               # strength of weight decay
)

# Define the Trainer
trainer = Trainer(
    model=model,                         # the model to train
    args=training_args,                  # training arguments
    train_dataset=train_dataset,         # training dataset
    eval_dataset=val_dataset,            # evaluation dataset
    tokenizer=tokenizer,                 # tokenizer
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained('./emotion_model')
tokenizer.save_pretrained('./emotion_model')

