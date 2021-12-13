import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import StandardScaler
from skbio.stats.ordination import *
from scipy.spatial.distance import pdist, squareform
from sklearn.decomposition import PCA
from plotnine import*


if __name__ == '__main__':
     # Box plot
     indResult = pd.read_csv('./independent_result/layer-2.csv')
     indResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
     indMelt = indResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
     indMelt['Env'] = indMelt['Env'].apply(lambda x: x[re.search('(root:)', x).end():] if re.search('(root:)', x) else x)
     indMelt['Env'].replace({'kindergarten': 'Kindergarten', 'mid_school': 'Middle school', 
                              'youth': 'Youth', 'mid_age': 'Middle age', 'elder': 'Elder'}, inplace=True)
     indMelt.to_csv('independent_result/layerMelt.csv', index=0)
     tfP = (ggplot(indMelt, aes(x='Env', y='Contribution'))+
          geom_boxplot()+
          xlim(['Kindergarten', 'Pupils', 'Middle school', 'Youth', 'Middle age', 'Elder'])+
          theme_bw())
     tfP.save('./independent_result/plot.jpg')
     
     tfResult = pd.read_csv('./transfer_result/layer-2.csv')
     tfResult.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
     tfMelt = tfResult.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
     tfMelt['Env'] = tfMelt['Env'].apply(lambda x: x[re.search('(root:)', x).end():] if re.search('(root:)', x) else x)
     tfMelt['Env'].replace({'kindergarten': 'Kindergarten', 'mid_school': 'Middle school', 
                              'youth': 'Youth', 'mid_age': 'Middle age', 'elder': 'Elder'}, inplace=True)
     tfMelt.to_csv('transfer_result/layerMelt.csv', index=0)
     tfP = (ggplot(tfMelt, aes(x='Env', y='Contribution'))+
          geom_boxplot()+
          xlim(['Kindergarten', 'Pupils', 'Middle school', 'Youth', 'Middle age', 'Elder'])+
          theme_bw())
     tfP.save('./transfer_result/plot.jpg')

     # PCOA plot
     groupCategory = pd.CategoricalDtype(['Kindergarten', 'Pupils', 'Middle school', 'Youth', 
                                        'Middle age', 'Elder', 'Centenarians'], ordered=True)
     metaNormal = pd.read_csv('../../data/normal-meta.csv', index_col=0)['Group']
     metaNormal.replace({'kindergarten': 'Kindergarten', 'mid_school': 'Middle school', 
                         'youth': 'Youth', 'mid_age': 'Middle age', 'elder': 'Elder'}, inplace=True)
     abundanceNormal = pd.read_csv('../../data/relative-abundance.csv', index_col=0)[metaNormal.index.tolist()].T
     jsDm = squareform(pdist(abundanceNormal, metric='jensenshannon'))
     jsPcoa = pd.DataFrame(pcoa(jsDm, number_of_dimensions=2).samples.values.tolist(), 
                              index=abundanceNormal.index, columns=['PC1', 'PC2'])
     pcoaPlot = (ggplot(jsPcoa, aes('PC1', 'PC2', color=metaNormal, fill=metaNormal))+
                    geom_point(size=2)+
                    stat_ellipse(geom = "polygon", alpha = 0.1)+
                    theme_bw()+
                    theme(axis_line = element_line(color="gray", size = 2))+
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())+
                    theme(figure_size=(10, 10))+
                    theme(legend_position = (0.8,0.8))+
                    theme(text=element_text(size=20)))
     pcoaPlot.save('pcoa_plot.jpg')
     
     # PCA plot
     pca = PCA(n_components=2)
     pcaDf = pd.DataFrame(data = pca.fit_transform(abundanceNormal), columns=['PC1', 'PC2'])
     pcaDf['Env'] = metaNormal.values
     pcaPlot = (ggplot(pcaDf, aes('PC1', 'PC2', color='Env', fill='Env'))+
                    geom_point(size=2)+
                    stat_ellipse(geom = "polygon", alpha = 0.15)+
                    theme_bw()+
                    theme(axis_line = element_line(color="gray", size = 2))+
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())+
                    theme(figure_size=(10, 10))+
                    theme(legend_position = (0.8,0.8))+
                    theme(text=element_text(size=20)))
     pcaPlot.save('pca_plot.jpg')
     
     
     