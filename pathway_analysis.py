import gseapy as gp
import pandas as pd
import numpy as np

# Load gene expression data
data = pd.read_csv('gene_expression_data.csv')

# Example: DEGs in the dataset
# Assume 'gene' is the gene name, and 'log2FoldChange' and 'p_value' columns are present
deg_results = data[['gene', 'log2FoldChange', 'p_value']]

# Prepare gene list
deg_results['-log10(p_value)'] = -np.log10(deg_results['p_value'])
gene_list = deg_results.set_index('gene')['-log10(p_value)'].to_dict()

# Perform pathway enrichment analysis using KEGG pathways
enrichment_results = gp.enrichr(gene_list=gene_list, gene_sets='KEGG_2021_Human', outdir='pathway_analysis_results')

# Print top pathways
print(enrichment_results.results.head())
