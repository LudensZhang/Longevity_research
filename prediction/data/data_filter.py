import pandas as pd
import numpy as np

if __name__ == '__main__':
    # Loading data
    ageMeta = pd.read_csv('../../data/normal-meta.csv', index_col=0)['Age']
    ageAbundance = pd.read_csv('../../data/relative-abundance.csv', index_col=0)
    # Creating map & metadata
    ageMeta = ageMeta.apply(lambda x: f'root:{x}')
    ageMeta.rename('Env', inplace=True)
    microbiomeMap = pd.DataFrame([ageMeta.unique()])
    microbiomeMap.to_csv('microbiomes.txt', index=0, header=0)
    ageMeta.to_csv('metadata.csv')
    # Splitting abundance
    queryLabel = ageMeta.sample(frac=0.3)
    sourceLabel = ageMeta[set(ageMeta.index) - set(queryLabel.index)]
    queryAbundance = ageAbundance[queryLabel.index.tolist()]
    sourceAbundance = ageAbundance[sourceLabel.index.tolist()]
    queryAbundance.to_csv('query_abundance.tsv', sep='\t')
    sourceAbundance.to_csv('source_abundance.tsv', sep='\t')
