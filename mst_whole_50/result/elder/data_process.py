import pandas as pd

if __name__ == '__main__':
    region = pd.read_csv('../../../data_jiangsu_and_sichuan/Aged_example/mapping.txt', 
                         sep='\t', index_col=0)['Region']

    whole_ind_result = pd.DataFrame([], columns = ['SampleID', 'Env', 'Region'])
    whole_trans_result = pd.DataFrame([], columns = ['SampleID', 'Env', 'Region'])

    for i in range(100):
        indResult = pd.read_csv(f'./independent_result_{i}/layer-2.csv')
        indResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
        indMelt = indResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
        indMelt['Env'] = indMelt['Env'].apply(lambda x: x.split(':')[-1])
        indMelt['Env'] = indMelt['Env'].replace('Elder', 'Senior')
        indMelt.set_index('SampleID', inplace=True)
        indMeltWithReigion = indMelt.merge(region, how='inner', left_index=True, right_index=True)
        whole_ind_result = pd.concat([whole_ind_result, indMeltWithReigion])
    
        transResult = pd.read_csv(f'./transfer_result_{i}/layer-2.csv')
        transResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
        transMelt = transResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
        transMelt['Env'] = transMelt['Env'].apply(lambda x: x.split(':')[-1])
        transMelt['Env'] = transMelt['Env'].replace('Elder', 'Senior')
        transMelt.set_index('SampleID', inplace=True)
        transMeltWithReigion = transMelt.merge(region, how='inner', left_index=True, right_index=True)
        whole_trans_result = pd.concat([whole_trans_result, transMeltWithReigion])

    whole_ind_result.to_csv('whole_independent_result.csv')
    whole_trans_result.to_csv('whole_transfer_result.csv')