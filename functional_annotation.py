# Simulated function for GO and KEGG analysis (normally you would use online tools or R/Python packages)
def perform_go_kegg_analysis(genes):
    go_results = pd.DataFrame({
        'GO_Term': ['GO:0008150', 'GO:0003674', 'GO:0005575'],
        'Description': ['biological_process', 'molecular_function', 'cellular_component'],
        'Count': [5, 3, 2],
        'p_value': [0.001, 0.005, 0.01],
        'adjusted_p_value': [0.005, 0.01, 0.02]
    })
    
    kegg_results = pd.DataFrame({
        'KEGG_Pathway': ['hsa04110', 'hsa05200'],
        'Description': ['Cell cycle', 'Pathways in cancer'],
        'Count': [3, 2],
        'p_value': [0.002, 0.006],
        'adjusted_p_value': [0.01, 0.015]
    })
    
    return go_results, kegg_results

# Simulate GO and KEGG analysis
go_results, kegg_results = perform_go_kegg_analysis(sig_genes['Gene_ID'])

# Display results
go_results, kegg_results
