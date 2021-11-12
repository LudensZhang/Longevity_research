import pandas as pd

def if_uc(df, i, ii):
    if rawTaxa.iloc[i, ii] == 'unclassified':
        return None
    else:
        return rawTaxa.iloc[i, ii]

if __name__ == '__main__':
    rawAbundance = pd.read_csv('raw_data/clean_data.txt', sep='\t')
    rawMeta = pd.read_csv('raw_data/clean_meta.txt', sep='\t', index_col=0)
    rawTaxa = pd.read_csv('raw_data/clean_tax.txt', sep='\t').drop(['Unnamed: 0', 'quality'], axis=1)
    rawTaxa = rawTaxa[['domain', 'phylum', 'class', 'order', 'family', 'genus']]
    taxaName = []
    
    for i in rawTaxa.index:
        name = f'k__{if_uc(rawTaxa, i, 0)}:p__{if_uc(rawTaxa, i, 1)}:c__{if_uc(rawTaxa, i, 2)}:o__{if_uc(rawTaxa, i, 3)}:f__{if_uc(rawTaxa, i, 4)}:g__{if_uc(rawTaxa, i, 5)}:s__'
        taxaName.append(name)
        
    rawAbundance['Unnamed: 0'] = taxaName
    rawAbundance.rename(columns={'Unnamed: 0': 'Samples'}, inplace=True)
    rawAbundance.to_csv('abundance.csv', index=0)
    
    rawMeta.index.rename('SampleID', inplace=True)
    normalMeta = rawMeta[rawMeta['Group'] != 'young soldier']['Age']
    soldierMeta = rawMeta[rawMeta['Group'] == 'young soldier']['Age']
    normalMeta.to_csv('normal_meta.csv')
    soldierMeta.to_csv('soldier_meta.csv')