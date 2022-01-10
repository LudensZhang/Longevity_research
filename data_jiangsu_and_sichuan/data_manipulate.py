import pandas as pd
import numpy as np


def AgeGroup(age):
    if age <= 22:
        return 'Young'
    if age <= 50:
        return 'Middle age'
    if age <= 79:
        return 'Elder'
    else:
        return 'Centenarian'


if __name__ == '__main__':
    metaData = pd.read_csv('Aged_example/mapping.txt', sep='\t', index_col=0)
    metaJiangsu = metaData[metaData['Region'] == 'Jiangsu']['Age']
    metaJiangsu = metaJiangsu.apply(AgeGroup)
    metaJiangsu.index.rename('SampleID', inplace=True)
    metaJiangsu.rename('Env', inplace=True)
    
    abundanceWhole = pd.read_csv('Aged_example/all_otu_table_L6.txt', skiprows=1, sep='\t', index_col=0)
    abundanceJiangsu = abundanceWhole[set(metaJiangsu.index) & set(abundanceWhole.columns)]
    abundanceJiangsu.index.rename('Samples', inplace=True)
    abundanceJiangsu.to_csv('abundance_jiangsu.csv')
    metaJiangsu = metaJiangsu.loc[abundanceJiangsu.columns]
    metaJiangsu.to_csv('metadata_jiangsu.csv')
    
    