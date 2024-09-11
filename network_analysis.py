import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Load PPI network data
ppi_df = pd.read_csv('ppi_network.txt', sep='\t', header=None, names=['protein1', 'protein2'])

# Create graph from PPI data
G = nx.from_pandas_edgelist(ppi_df, 'protein1', 'protein2')

# Compute centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Combine centrality measures into a DataFrame
centrality_df = pd.DataFrame({
    'protein': list(G.nodes),
    'degree_centrality': [degree_centrality[node] for node in G.nodes],
    'betweenness_centrality': [betweenness_centrality[node] for node in G.nodes],
    'closeness_centrality': [closeness_centrality[node] for node in G.nodes]
})

# Identify top targets based on centrality measures
top_targets = centrality_df.sort_values(by='degree_centrality', ascending=False).head(10)
print("Top therapeutic targets based on degree centrality:")
print(top_targets)

# Plot the network
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=50, font_size=10)
plt.title('Protein-Protein Interaction Network')
plt.show()
