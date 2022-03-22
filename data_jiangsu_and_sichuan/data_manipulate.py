import pandas as pd
import numpy as np


def AgeGroup(age):
    if age <= 30:
        return 'Young'
    # if age <= 60:
    #     return 'Young'
    if age <= 100 and age > 60:
        return 'Elder'
    if age > 100:
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
    metaWhole = metaRaw['Age'].apply(AgeGroup).dropna()
    print(metaWhole.head())
    metaWhole.index.rename('SampleID', inplace=True)
    metaWhole.rename('Env', inplace=True)
    abundanceWhole = abundanceRaw[set(metaWhole.index) & set(abundanceRaw.columns)]
    abundanceWhole.to_csv('abundance_whole.csv')
    metaWhole = metaWhole.loc[abundanceWhole.columns]
    metaWhole.to_csv('metadata_whole.csv')
    print(metaWhole.value_counts())
    
    # whole data with region of centenarian
    # metaRegion = metaRaw.copy()
    # metaRegion['Age'] = metaRegion['Age'].apply(AgeGroup)
    # for i in metaRegion.index:
    #     if metaRegion.loc[i, 'Age'] == 'Elder':
    #         metaRegion.loc[i, 'Age'] = metaRegion.loc[i, 'Age'] + ' ' + metaRegion.loc[i, 'Region']
    # metaRegion.rename(columns={'Age': 'Env'}, inplace=True)
    # metaRegion = metaRegion.loc[abundanceRaw.columns]
    # metaRegion['Env'].to_csv('metadata_whole_with_region.csv')
    
    
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
    
    # Only using italy elder
    # metaRaw['Env'] = metaRaw['Age'].apply(AgeGroup)
    # metaElderItaly = metaRaw[(metaRaw['Region'] == 'Italy') & (metaRaw['Env'] == 'Elder')]['Env']
    # metaOther = metaRaw[metaRaw['Env'] != 'Elder']['Env']
    # metaWhole = metaElderItaly.append(metaOther)
    # metaWhole.index.rename('SampleID', inplace=True)
    # metaWhole.rename('Env', inplace=True)
    
    # abundanceWhole = abundanceRaw[set(metaWhole.index) & set(abundanceRaw.columns)]
    # abundanceWhole.index.rename('Samples', inplace=True)
    # abundanceWhole.to_csv('abundance_italy_elder_only.csv')
    # metaWhole = metaWhole.loc[abundanceWhole.columns]
    # metaWhole.to_csv('metadata_italy_elder_only.csv')
    # print(metaWhole.value_counts())
    