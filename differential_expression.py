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
from scipy.stats import ttest_ind
from statsmodels.stats.multitest import multipletests

# Group samples based on clustering labels
normal_samples = sample_cluster_df[sample_cluster_df['Cluster'] == 0]['Sample']
disease_samples = sample_cluster_df[sample_cluster_df['Cluster'] == 1]['Sample']

# Extract expression data
normal_data = standardized_df[normal_samples]
disease_data = standardized_df[disease_samples]

# Calculate t-test p-values for each gene
p_values = []
for i in range(standardized_df.shape[0]):
    normal_expr = normal_data.iloc[i, :]
    disease_expr = disease_data.iloc[i, :]
    t_stat, p_val = ttest_ind(normal_expr, disease_expr, equal_var=False)
    p_values.append(p_val)

# Add p-values to the DataFrame
standardized_df['p_value'] = p_values

# Apply Benjamini-Hochberg correction
standardized_df['adjusted_p_value'] = multipletests(standardized_df['p_value'], method='fdr_bh')[1]

# Identify significantly differentially expressed genes
sig_genes = standardized_df[standardized_df['adjusted_p_value'] < 0.05]

# Calculate log2 fold change
epsilon = 1e-6
normal_mean = standardized_df[normal_samples].mean(axis=1) + epsilon
disease_mean = standardized_df[disease_samples].mean(axis=1) + epsilon
standardized_df['log2_fold_change'] = np.log2(normal_mean / disease_mean)
