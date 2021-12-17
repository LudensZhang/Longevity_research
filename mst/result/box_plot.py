import pandas as pd 
import numpy as np
from plotnine import *


if __name__ == '__main__':
    print('Loading data...')
    indeData = pd.read_csv('independent_result/layerMelt.csv', index_col=0)
    transData = pd.read_csv('transfer_result/layerMelt.csv', index_col=0)
    groupCategory = pd.CategoricalDtype(['Kindergarten', 'Pupils', 'Middle school', 'Youth', 'Middle age', 'Elder'], ordered=True)
    
    print('Creating Binding Data...')
    indeData['mode'] = 'Independent'
    transData['mode'] = 'Transfer'
    indeData['Env'] = indeData['Env'].astype(groupCategory)
    transData['Env'] = transData['Env'].astype(groupCategory)
    bindData = indeData.append(transData)
    
    print('Plotting...')
    bindBox = (ggplot(bindData, aes(x='Env', y='Contribution', fill='mode'))+
                        geom_boxplot()+
                        geom_smooth())
    print(bindBox)