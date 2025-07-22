import pandas as pd

# Load the dataset with the correct delimiter (tab-separated)
data = pd.read_csv('brain_stroke.csv', delimiter='\t')

# Print the column names to check if they are now separated properly
print(data.columns)
