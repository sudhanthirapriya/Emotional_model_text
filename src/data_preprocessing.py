import pandas as pd
import os

def preprocess_data(input_file, output_file):
    # Load dataset
    df = pd.read_csv(input_file)

    # Clean text (lowercase, remove special characters, etc.)
    df['text'] = df['text'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

    # Map emotions to simplified categories (if needed)
    emotion_map = {'joy': 'joy', 'sadness': 'sadness', 'anger': 'anger', 'fear': 'fear'}
    df['emotion'] = df['emotion'].map(emotion_map)

    # Save the processed data
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_path = "data/raw/raw_dataset.csv"  # Adjust file name
    output_path = "data/processed/processed_dataset.csv"
    preprocess_data(input_path, output_path)
