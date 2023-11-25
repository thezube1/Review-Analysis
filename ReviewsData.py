import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\zubin\Dropbox\Python\MicrosoftFeedback\amazon-fine-food-reviews\Reviews.csv')
print(df.columns)

print(df.Text.head(10))
print(df.Summary.head(10))