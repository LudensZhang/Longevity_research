import pandas as pd


if __name__ == '__main__':
    rawMeta = pd.read_csv('../../../data/normal-meta.csv', index_col=0)['Group']
    rawMeta.index.set_names('SampleID')
    metaData = rawMeta.apply(lambda x: f'root:{x}')
    sourceMeta = rawMeta[rawMeta != 'Centenarians'].apply(lambda x: f'root:{x}')
    queryMeta = rawMeta[rawMeta == 'Centenarians'].apply(lambda x : f'root:{x}')
    metaData.rename('Env', inplace=True)
    metaData.to_csv('metadata.csv')
    
    rawAbundance = pd.read_csv('../../../data/relative-abundance.csv', index_col=0)
    queryAbundance = rawAbundance[queryMeta.index.tolist()]
    queryAbundance.to_csv('query-abundance.tsv', sep='\t')
    sourceAbundance = rawAbundance[sourceMeta.index.tolist()]
    sourceAbundance.to_csv('source-abundance.tsv', sep='\t')
