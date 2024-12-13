import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    cleaned_data = data[['UserId', 'ProductId']].drop_duplicates()
    return cleaned_data
