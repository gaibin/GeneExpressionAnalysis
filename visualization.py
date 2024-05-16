import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram

# Generate the volcano plot
plt.figure(figsize=(10, 6))
plt.scatter(standardized_df['log2_fold_change'], -np.log10(standardized_df['p_value']), color='grey')
plt.scatter(sig_genes['log2_fold_change'], -np.log10(sig_genes['p_value']), color='red')
plt.xlabel('Log2 Fold Change')
plt.ylabel('-Log10 P-value')
plt.title('Volcano Plot of Differentially Expressed Genes')
plt.show()

# Perform hierarchical clustering on samples
sample_linked = linkage(standardized_data.T, method='ward')

# Plot the dendrogram for samples
plt.figure(figsize=(10, 7))
dendrogram(sample_linked, labels=large_data.columns[1:], leaf_rotation=90)
plt.title('Hierarchical Clustering Dendrogram of Samples')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

# Plot heatmap for samples and genes
sns.clustermap(standardized_data.T, row_cluster=True, col_cluster=True, figsize=(12, 8), cmap='viridis')
plt.show()
