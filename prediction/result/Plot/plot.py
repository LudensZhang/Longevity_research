import pandas as pd
import numpy as np
import re
from plotnine.labels import xlab
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

if __name__ == '__main__':
    # Loading data
    rawMeta = pd.read_csv('../../../data/normal-meta.csv', index_col=0)[['Age']]
    rawMeta = rawMeta.astype('float')
    indePredMeta = pd.read_csv('../independent_result/layer-2.csv', index_col=0, header=None)
    transPredMeta = pd.read_csv('../transfer_result/layer-2.csv', index_col=0, header=None)
    # Preprocessing
    indePredMeta.iloc[0] = indePredMeta.iloc[0].apply(lambda x: int(x[re.search('root:', x).end():]))
    indePredMeta = indePredMeta.rename(columns=indePredMeta.iloc[0]).drop(indePredMeta.index[0])
    transPredMeta.iloc[0] = transPredMeta.iloc[0].apply(lambda x: int(x[re.search('root:', x).end():]))
    transPredMeta = transPredMeta.rename(columns=transPredMeta.iloc[0]).drop(transPredMeta.index[0])
    # Calculating predict age
    indePredMeta = indePredMeta.astype('float')
    indePredMeta['Predict Age'] = indePredMeta.apply(lambda x: x.idxmax(), axis=1)
    transPredMeta = transPredMeta.astype('float')
    transPredMeta['Predict Age'] = transPredMeta.apply(lambda x: x.idxmax(), axis=1)
    # Plotting density
    densityPlot = sns.distplot(rawMeta, kde=False)
    densityPlot.set(xlim=(int(rawMeta.min()), int(rawMeta.max())))
    plt.savefig('density.png')
    # Ploting regression
    rgData = pd.concat([rawMeta.loc[indePredMeta.index], indePredMeta['Predict Age'], transPredMeta['Predict Age']], axis=1)
    rgData.columns = ['Age', 'Independent', 'Transfer']
    rgData = rgData.melt(id_vars='Age', var_name='mode', value_name='Predict Age')
    rgPlot = sns.scatterplot(data=rgData, x='Age', y='Predict Age', hue='mode')
    rgPlot = sns.lmplot(data=rgData, x='Age', y='Predict Age', hue='mode')
    rgPlot.set(xlabel='Real Age', ylabel='Predict Age')
    plt.savefig('regression.png')
    