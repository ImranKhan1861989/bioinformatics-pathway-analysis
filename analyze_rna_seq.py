import pandas as pd
import numpy as np
import argparse
from scipy import stats

def main(input_file, output_file):
    # Load RNA-seq data
    data = pd.read_csv(input_file)

    # Perform differential expression analysis
    data['log2FoldChange'] = np.log2(data['treatment'] + 1) - np.log2(data['control'] + 1)
    data['p_value'] = data.apply(lambda row: stats.ttest_ind(
        np.random.normal(row['control'], 1, 1000),
        np.random.normal(row['treatment'], 1, 1000)
    )[1], axis=1)

    # Adjust p-values for multiple testing
    from statsmodels.stats import multitest
    data['adjusted_p_value'] = pd.Series(multitest.multipletests(data['p_value'], method='fdr_bh')[1])

    # Filter significant DEGs
    significant_genes = data[data['adjusted_p_value'] < 0.05]

    # Save results
    significant_genes.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze RNA-seq data.')
    parser.add_argument('--input', required=True, help='Input RNA-seq data file')
    parser.add_argument('--output', required=True, help='Output file for significant genes')
    args = parser.parse_args()
    main(args.input, args.output) 
