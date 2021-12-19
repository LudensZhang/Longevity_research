import pandas as pd

if __name__ == '__main__':
    # Loading data...
    rawMeta = pd.read_csv('../../data/normal-meta.csv', index_col=0)
    rawAbundance = pd.read_csv('../../data/relative-abundance.csv', index_col=0)
    # Filtering data...
    rawMeta['Env'] = rawMeta['Age'].apply(lambda x: 'root:young' if x <= 30 else 'root:other')
    centenarienMeta = rawMeta[rawMeta['Group'] == 'Centenarians'] 
    elderMeta = rawMeta[rawMeta['Group'] == 'elder']
    # Sorting data...
    centenarienQuery = rawAbundance[centenarienMeta.index.tolist()]
    centenarienSource = rawAbundance[set(rawMeta.index.tolist()) - set(elderMeta.index.tolist()) - set(centenarienMeta.index.tolist())]
    centenarienMap = rawMeta.loc[set(rawMeta.index.tolist()) - set(elderMeta.index.tolist()) - set(centenarienMeta.index.tolist())]['Env']
    elderQuery = rawAbundance[elderMeta.index.tolist()]
    elderSource = rawAbundance[set(rawMeta.index.tolist()) - set(elderMeta.index.tolist()) - set(centenarienMeta.index.tolist())]
    elderMap = rawMeta.loc[set(rawMeta.index.tolist()) - set(elderMeta.index.tolist())- set(centenarienMeta.index.tolist())]['Env']
    # Outputting...
    centenarienQuery.to_csv('centenarien/query_abundance.tsv', sep='\t')
    centenarienSource.to_csv('centenarien/source_abundance.tsv', sep='\t')
    centenarienMap.to_csv('centenarien/metadata.csv')
    elderQuery.to_csv('elder/query_abundance.tsv', sep='\t')
    elderSource.to_csv('elder/source_abundance.tsv', sep='\t')
    elderMap.to_csv('elder/metadata.csv')