import pandas as pd
import numpy as np
from sklearn.model_selection import ShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from plotnine import*

def RandomForest(X_train, y_train, X_test):
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)
    y_pred = rfc.predict_proba(X_test)
    return pd.DataFrame(y_pred, columns = ['Senior', 'Young'], index = X_test.index)

metadata = pd.read_csv('../data_jiangsu_and_sichuan/metadata_whole.csv', index_col = 0)
abundance = pd.read_csv('../data_jiangsu_and_sichuan/abundance_whole.csv').T
region = pd.read_csv('../data_jiangsu_and_sichuan/Aged_example/mapping.txt', sep = '\t', index_col = 0)['Region']
metadata = metadata[metadata['Env'] != 'Centenarian']
abundance = abundance.loc[metadata.index]

# Bootstrap
result = pd.DataFrame(columns = ['Senior', 'Young'])
for bootstrap in range(100):
    y_train = metadata.groupby('Env').sample(n = 265)
    X_train = abundance.loc[y_train.index]
    y_test = metadata[metadata['Env'] == 'Elder'].drop(y_train[y_train['Env'] == 'Elder'].index)
    X_test = abundance.loc[y_test.index]
    result = pd.concat([result, RandomForest(X_train, y_train, X_test)])

# Deprocess
result = result.reset_index().melt(id_vars = 'index', var_name = 'Env', value_name = 'Contribution')
result.set_index('index', inplace = True)
result_region = result.merge(region, how='inner', left_index=True, right_index=True)
result_region['Contribution'] = result_region['Contribution']
result_region.to_csv('RF_result.csv')