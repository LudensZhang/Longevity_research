import pandas as pd   

if __name__ == '__main__':
    rawMeta = pd.read_csv('../../data_jiangsu_and_sichuan/metadata_italy_elder_only.csv', index_col=0)
    rawAbundance = pd.read_csv('../../data_jiangsu_and_sichuan/abundance_italy_elder_only.csv', index_col=0)

    # elderQueryMeta = rawMeta[rawMeta['Env'] == 'Elder'].sample(frac=0.3)
    # centenarianQueryMeta = rawMeta[rawMeta['Env'] == 'Centenarian']
    # sourceMeta = rawMeta.drop(elderQueryMeta.index.tolist() + centenarianQueryMeta.index.tolist())
    # sourceMeta['Env'] = sourceMeta['Env'].apply(lambda x: f'root:{x}')
    # sourceMeta.index.rename('SampleID', inplace=True)
    
    sourceMeta = rawMeta[rawMeta['Env'] == 'Young'].sample(n=60)
    sourceMeta = sourceMeta.append(rawMeta[rawMeta['Env'] == 'Elder'])
    elderMetaRaw = rawMeta[rawMeta['Env'] == 'Elder']
    elderAbundanceRaw = rawAbundance[elderMetaRaw.index]
    
    # We copied the elder metadata for small quantities
    elderMetaCp0 = elderMetaRaw.copy()
    elderMetaCp0.index = [f'{id}_cp0' for id in elderMetaRaw.index.tolist()]
    elderAbundanceCp0 = elderAbundanceRaw.copy()
    elderAbundanceCp0.columns = [f'{id}_cp0' for id in elderAbundanceRaw.columns.tolist()]
    
    elderMetaCp1 = elderMetaRaw.copy()
    elderMetaCp1.index = [f'{id}_cp1' for id in elderMetaRaw.index.tolist()]
    elderAbundanceCp1 = elderAbundanceRaw.copy()
    elderAbundanceCp1.columns = [f'{id}_cp1' for id in elderAbundanceRaw.columns.tolist()]
    
    elderMetaCopy = pd.concat([elderMetaRaw, elderMetaCp0, elderMetaCp1])
    sourceMeta = pd.concat([sourceMeta, elderMetaCp0, elderMetaCp1])
    rawAbundance = pd.concat([rawAbundance, elderAbundanceCp0, elderAbundanceCp1], axis=1)
    
    elderQueryMeta = elderMetaCopy.sample(frac=0.3)
    sourceMeta.drop(elderQueryMeta.index, inplace=True)
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