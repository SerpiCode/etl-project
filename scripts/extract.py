import os
import pandas as pd

path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'netflix_titles.csv') # https://www.kaggle.com/datasets/shivamb/netflix-shows
df = pd.read_csv(path)

print(df.head())