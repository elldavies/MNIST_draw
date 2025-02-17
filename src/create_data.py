from sklearn.datasets import load_diabetes
import pandas as pd
import os

# Load the diabetes dataset
diabetes = load_diabetes()

# Convert to DataFrame
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# save data to csv
# Create the data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save data to csv
df.to_csv('data/raw_data.csv', index=False)