from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# K-means clustering
num_clusters = 2  # Assume we want to divide into two groups
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(standardized_data.T)
clusters = kmeans.labels_

# Create a new DataFrame with sample names and cluster labels
sample_cluster_df = pd.DataFrame({
    'Sample': large_data.columns[1:],  # Exclude the Gene_ID column
    'Cluster': clusters
})

# PCA for dimensionality reduction
pca = PCA(n_components=2)
pca_result = pca.fit_transform(standardized_data.T)

# Visualize PCA results
plt.figure(figsize=(10, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis', marker='o')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('PCA of Gene Expression Data')
plt.colorbar(label='Cluster')
plt.show()
