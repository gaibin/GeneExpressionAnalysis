import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the large Excel file
file_path = 'data/dada.xlsx'
large_data = pd.read_excel(file_path)

# Fill missing values with the mean of each column
large_data.fillna(large_data.mean(), inplace=True)

# Standardize the data (excluding the Gene_ID column)
scaler = StandardScaler()
standardized_data = scaler.fit_transform(large_data.iloc[:, 1:])

# Convert standardized data back to DataFrame and add Gene_ID column
standardized_df = pd.DataFrame(standardized_data, columns=large_data.columns[1:])
standardized_df.insert(0, 'Gene_ID', large_data['Gene_ID'])
