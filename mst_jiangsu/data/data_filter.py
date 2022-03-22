import pandas as pd   

if __name__ == '__main__':
    rawMeta = pd.read_csv('../../data_jiangsu_and_sichuan/metadata_whole.csv', index_col=0)
    rawAbundance = pd.read_csv('../../data_jiangsu_and_sichuan/abundance_whole.csv', index_col=0)

    # elderQueryMeta = rawMeta[rawMeta['Env'] == 'Elder'].sample(frac=0.3)
    # centenarianQueryMeta = rawMeta[rawMeta['Env'] == 'Centenarian']
    # sourceMeta = rawMeta.drop(elderQueryMeta.index.tolist() + centenarianQueryMeta.index.tolist())
    # sourceMeta['Env'] = sourceMeta['Env'].apply(lambda x: f'root:{x}')
    # sourceMeta.index.rename('SampleID', inplace=True)
    
    sourceMeta = rawMeta[rawMeta['Env'] != 'Centenarian'].groupby('Env').sample(n=265)
    rawElderMeta = rawMeta[rawMeta['Env'] == 'Elder']
    elderQueryMeta = rawElderMeta.drop(sourceMeta[sourceMeta['Env'] == 'Elder'].index)
    centenarianQueryMeta = rawMeta[rawMeta['Env'] == 'Centenarian']
    sourceMeta['Env'] = sourceMeta['Env'].apply(lambda x: f'root:{x}')
    sourceMeta.index.rename('SampleID', inplace=True)
    
    elderQueryAbundance = rawAbundance[elderQueryMeta.index]
    centenarianQueryAbundance = rawAbundance[centenarianQueryMeta.index]
    sourceAbundance = rawAbundance[sourceMeta.index]
    
    sourceMeta.to_csv('elder/metadata.csv')
    sourceMeta.to_csv('centenarian/metadata.csv')
    sourceAbundance.to_csv('elder/source_abundance.tsv', sep='\t')
    sourceAbundance.to_csv('centenarian/source_abundance.tsv', sep='\t')
    elderQueryAbundance.to_csv('elder/query_abundance.tsv', sep='\t')
    centenarianQueryAbundance.to_csv('centenarian/query_abundance.tsv', sep='\t')