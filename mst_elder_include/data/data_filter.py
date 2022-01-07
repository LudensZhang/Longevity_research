from os import replace
import pandas as pd
import numpy as np

if __name__ == '__main__':
    rawMeta = pd.read_csv('../../data/normal-meta.csv', index_col=0)['Group']
    rawAbundance = pd.read_csv('../../data/relative-abundance.csv', index_col=0)
    queryMeta = rawMeta[rawMeta == 'elder'].sample(frac=0.3, replace=False)
    sourceMeta = rawMeta[rawMeta != 'Centenarians'].drop(queryMeta.index.tolist())
    queryAbundance = rawAbundance[queryMeta.index.tolist()]
    queryAbundance.to_csv('query_abundance.tsv', sep='\t')
    sourceAbundance = rawAbundance[sourceMeta.index.tolist()]
    sourceAbundance.to_csv('source_abundance.tsv', sep='\t')
