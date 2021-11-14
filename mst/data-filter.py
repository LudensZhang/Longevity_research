import pandas as pd


if __name__ == '__main__':
    rawMeta = pd.read_csv('../data/normal-meta.csv', index_col=0)['Group']
    rawMeta.index.set_names('SampleID')
    sourceMeta = rawMeta[rawMeta != 'Centenarians'].apply(lambda x: f'root:{x}')
    queryMeta = rawMeta[rawMeta == 'Centenarians'].apply(lambda x : f'root:{x}')
    sourceMeta.rename('Env', inplace=True)
    queryMeta.rename('Env', inplace=True)
    sourceMeta.to_csv('source-meta.csv')
    queryMeta.to_csv('query-meta.csv')
    
    rawAbundance = pd.read_csv('../data/abundance.csv', index_col=0)
    queryAbundance = rawAbundance[[queryMeta.index.tolist()]]
    queryAbundance.to_csv('query-abundance.csv')