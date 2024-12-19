import os
import pandas as pd

def load_data(file_path):
    print(f'Data read from: {file_path}')
    return pd.read_csv(file_path)

def drop_nan(df):
    print('Checking for missing data...')
    
    print(f"Columns with NULL values:\n{df.isnull().sum()}")
    df = df.dropna()
    
    print(f"Missing data removed: {len(df)} lines remaining.\n")
    
    return df

def check_duplicates(df):
    print('Checking for duplicates...')
    
    duplicates = df.duplicated().sum()
    print(f"Number of duplicates: {duplicates}")
    
    if duplicates > 0:
        df = df.drop_duplicates()
        print('Duplicates removed.')
    
    return df

def clean_data(df):
    print('Cleaning data...\n')
    df = drop_nan(df)
    df = check_duplicates(df)
    
    print('\nData cleaned.')
    return df

def save_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to path: {output_path}")

if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'netflix_titles.csv') # https://www.kaggle.com/datasets/shivamb/netflix-shows
    output_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'netflix_titles_cleaned.csv')

    df = load_data(input_path)
    df_cleaned = clean_data(df)
    save_data(df_cleaned, output_path)