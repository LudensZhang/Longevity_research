import pandas as pd

if __name__ == '__main__':
    indResult = pd.read_csv('./independent_result/layer-2.csv')
    indResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
    indMelt = indResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
    indMelt['Env'] = indMelt['Env'].apply(lambda x: x.split(':')[-1])
    indMelt.to_csv('independent_result/layerMelt.csv', index=0)
    
    transResult = pd.read_csv('./transfer_result/layer-2.csv')
    transResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
    transMelt = transResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
    transMelt['Env'] = transMelt['Env'].apply(lambda x: x.split(':')[-1])
    transMelt.to_csv('transfer_result/layerMelt.csv', index=0)