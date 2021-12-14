import pandas as pd
from pandas.io.parsers import read_csv


if __name__ == '__main__':
    rawMeta = pd.read_csv('metadata.csv', index_col=0)
    rawAbundance = pd.read_csv('../../data/relative-abundance.csv', index_col=0)
    
    queryMeta = rawMeta[rawMeta == 'root:elder']
    sourceMeta = rawMeta[rawMeta != 'root:elder']
    queryAbundancne = rawAbundance[queryMeta.index]
    sourceAbundance = rawAbundance[sourceMeta.index]
    
    queryAbundancne.to_csv('query_abundance.tsv', sep='\t')
    sourceAbundance.to_csv('source_abundance.tsv', sep='\t')