# -*- coding: utf-8 -*-


import pandas as pd
import re

def extract_emails(text):
    # Extracts email addresses from the given text
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

def extract_phone_numbers(text):
    # Extracts phone numbers from the given text
    return re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)

def extract_dates(text):
    # Extracts dates in the format mm/dd/yyyy from the given text
    return re.findall(r'\b\d{1,2}/\d{1,2}/\d{4}\b', text)

# Load the dataset
df = pd.read_csv('dataset.csv')

# Apply the functions to the text column
df['extracted_emails'] = df['text_column'].apply(extract_emails)
df['extracted_phone_numbers'] = df['text_column'].apply(extract_phone_numbers)
df['extracted_dates'] = df['text_column'].apply(extract_dates)

# Display the results
print(df[['text_column', 'extracted_emails', 'extracted_phone_numbers', 'extracted_dates']])