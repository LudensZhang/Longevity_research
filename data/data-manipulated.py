import pandas as pd

def if_uc(df, i, ii):
    if raw_TAXA.iloc[i, ii] == 'unclassified':
        return None
    else:
        return raw_TAXA.iloc[i, ii]

if __name__ == '__main__':
    raw_ABUNDANCE = pd.read_csv('raw_data/clean_data.txt', sep='\t')
    raw_META = pd.read_csv('raw_data/clean_meta.txt', sep='\t', index_col=0)
    raw_TAXA = pd.read_csv('raw_data/clean_tax.txt', sep='\t').drop(['Unnamed: 0', 'quality'], axis=1)
    raw_TAXA = raw_TAXA[['domain', 'phylum', 'class', 'order', 'family', 'genus']]
    taxa_NAME = []
    
    for i in raw_TAXA.index:
        name = f'k__{if_uc(raw_TAXA, i, 0)}:p__{if_uc(raw_TAXA, i, 1)}:c__{if_uc(raw_TAXA, i, 2)}:o__{if_uc(raw_TAXA, i, 3)}:f__{if_uc(raw_TAXA, i, 4)}:g__{if_uc(raw_TAXA, i, 5)}:s__'
        taxa_NAME.append(name)
        
    raw_ABUNDANCE['Unnamed: 0'] = taxa_NAME
    raw_ABUNDANCE.rename(columns={'Unnamed: 0': 'Samples'}, inplace=True)
    raw_ABUNDANCE.to_csv('abundance.csv', index=0)
    
    raw_META.index.rename('SampleID', inplace=True)
    age_META = raw_META['Age']
    age_META.to_csv('metadata.csv')