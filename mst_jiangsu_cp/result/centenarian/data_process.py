import pandas as pd

if __name__ == '__main__':
    region = pd.read_csv('../../../data_jiangsu_and_sichuan/Aged_example/mapping.txt', 
                         sep='\t', index_col=0)['Region']

    indResult = pd.read_csv('./independent_result/layer-2.csv')
    indResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
    indMelt = indResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
    indMelt['Env'] = indMelt['Env'].apply(lambda x: x.split(':')[-1])
    indMelt['Env'] = indMelt['Env'].replace('Elder', 'Senior')
    indMelt.set_index('SampleID', inplace=True)
    indMeltWithReigion = indMelt.merge(region, how='inner', left_index=True, right_index=True)
    indMeltWithReigion.to_csv('independent_result/layerMelt.csv')
    
    transResult = pd.read_csv('./transfer_result/layer-2.csv')
    transResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
    transMelt = transResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
    transMelt['Env'] = transMelt['Env'].apply(lambda x: x.split(':')[-1])
    transMelt['Env'] = transMelt['Env'].replace('Elder', 'Senior')
    transMelt.set_index('SampleID', inplace=True)
    transMeltWithReigion = transMelt.merge(region, how='inner', left_index=True, right_index=True)
    transMeltWithReigion.to_csv('transfer_result/layerMelt.csv')