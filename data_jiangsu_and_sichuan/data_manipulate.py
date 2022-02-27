import pandas as pd
import numpy as np


def AgeGroup(age):
    if age <= 30:
        return 'Young'
    if age <= 60:
        return 'Middle age'
    if age <= 100:
        return 'Elder'
    else:
        return 'Centenarian'


if __name__ == '__main__':
    metaRaw = pd.read_csv('Aged_example/mapping.txt', sep='\t', index_col=0)
    # metaJiangsu = metaRaw[metaRaw['Region'] == 'Jiangsu']['Age']
    # metaJiangsu = metaJiangsu.apply(AgeGroup)
    # metaJiangsu.index.rename('SampleID', inplace=True)
    # metaJiangsu.rename('Env', inplace=True)
    
    abundanceRaw = pd.read_csv('Aged_example/all_otu_table_L6.txt', skiprows=1, sep='\t', index_col=0)
    # abundanceJiangsu = abundanceRaw[set(metaJiangsu.index) & set(abundanceRaw.columns)]
    # abundanceJiangsu.index.rename('Samples', inplace=True)
    # abundanceJiangsu.to_csv('abundance_jiangsu.csv')
    # metaJiangsu = metaJiangsu.loc[abundanceJiangsu.columns]
    # metaJiangsu.to_csv('metadata_jiangsu.csv')
    
    # whole data
    metaWhole = metaRaw['Age'].apply(AgeGroup)
    # metaWhole = pd.DataFrame([metaWhole, metaRaw['Region']]).T
    print(metaWhole.head())
    metaWhole.index.rename('SampleID', inplace=True)
    metaWhole.rename('Env', inplace=True)
    abundanceWhole = abundanceRaw[set(metaWhole.index) & set(abundanceRaw.columns)]
    abundanceWhole.to_csv('abundance_whole.csv')
    metaWhole = metaWhole.loc[abundanceWhole.columns]
    metaWhole.to_csv('metadata_whole.csv')
    print(metaWhole.value_counts())
    
    # Sichuan data
    # metaSichuan = metaRaw[metaRaw['Region'] == 'Sichuan']['Age']
    # metaSichuan = metaSichuan.apply(AgeGroup)
    # metaSichuan.index.rename('SampleID', inplace=True)
    # metaSichuan.rename('Env', inplace=True)
    
    # abundanceSichuan = abundanceRaw[set(metaSichuan.index) & set(abundanceRaw.columns)]
    # abundanceSichuan.index.rename('Samples', inplace=True)
    # abundanceSichuan.to_csv('abundance_sichuan.csv')
    # metaSichuan = metaSichuan.loc[abundanceSichuan.columns]
    # metaSichuan.to_csv('metadata_sichuan.csv')
    # print(metaSichuan.value_counts())
    
    # China data
    # metaChina = metaRaw[(metaRaw['Region'] == 'Jiangsu') | (metaRaw['Region'] == 'Sichuan')]['Age']
    # metaChina = metaChina.apply(AgeGroup)
    # metaChina.index.rename('SampleID', inplace=True)
    # metaChina.rename('Env', inplace=True)
    
    # abundanceChina = abundanceRaw[set(metaChina.index) & set(abundanceRaw.columns)]
    # abundanceChina.index.rename('Samples', inplace=True)
    # abundanceChina.to_csv('abundance_china.csv')
    # metaChina = metaChina.loc[abundanceChina.columns]
    # metaChina.to_csv('metadata_china.csv')
    # print(metaChina.value_counts())
    