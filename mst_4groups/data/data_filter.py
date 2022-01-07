from os import replace
import pandas as pd


def MetaGroup(x):
    if x == 'elder':
        return 'Elder'
    if x == 'mid_age':
        return 'Middle age'
    if x == 'Centenarians':
        return 'Centenarians'
    else: 
        return 'Young'

if __name__ == '__main__':
    rawMeta = pd.read_csv('../../data/normal-meta.csv', index_col=0)['Group']
    rawAbundance = pd.read_csv('../../data/relative-abundance.csv', index_col=0)
    
    rawMeta = rawMeta.apply(MetaGroup)
    elderQueryMeta = rawMeta[rawMeta == 'Elder'].sample(frac=0.3, replace=False)
    centenariansQueryMeta = rawMeta[rawMeta == 'Centenarians']
    sourceMeta = rawMeta.drop((elderQueryMeta.index.tolist() + centenariansQueryMeta.index.tolist()))
    sourceMeta = sourceMeta.apply(lambda x: f'root:{x}').rename('Env')
    
    elderQueryAbundance = rawAbundance[elderQueryMeta.index.tolist()]
    centenariansQueryAbundance = rawAbundance[centenariansQueryMeta.index.tolist()]
    sourceAbundance = rawAbundance[sourceMeta.index.tolist()]
    
    sourceMeta.to_csv('elder/metadata.csv')
    sourceMeta.to_csv('centenarien/metadata.csv')
    sourceAbundance.to_csv('elder/source_abundance.tsv', sep='\t')
    sourceAbundance.to_csv('centenarien/source_abundance.tsv', sep='\t')
    elderQueryAbundance.to_csv('elder/query_abundance.tsv', sep='\t')
    centenariansQueryAbundance.to_csv('centenarien/query_abundance.tsv', sep='\t')
    