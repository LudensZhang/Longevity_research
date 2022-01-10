import pandas as pd
import numpy as np
import re
from skbio.stats.ordination import *
from scipy.spatial.distance import pdist, squareform
from plotnine import *

if __name__ == '__main__':
    rawMeta = pd.read_csv('../../data_jiangsu_and_sichuan/metadata_jiangsu.csv', index_col=0)
    rawAbundance = pd.read_csv('../../data_jiangsu_and_sichuan/abundance_jiangsu.csv', index_col=0)[rawMeta.index.tolist()].T
    jsDm = squareform(pdist(rawAbundance, metric='jensenshannon'))
    jsPcoa = pd.DataFrame(pcoa(jsDm, number_of_dimensions=2).samples.values.tolist(), 
                            index=rawAbundance.index, columns=['PC1', 'PC2'])
    
    jsPcoa['Env'] = rawMeta
    
    pcoaPlot = (ggplot(jsPcoa, aes('PC1', 'PC2', color='Env', fill='Env'))+
                    geom_point(size=2)+
                    stat_ellipse(geom = "polygon", alpha = 0.1)+
                    theme_bw()+
                    theme(axis_line = element_line(color="gray", size = 2))+
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())+
                    theme(figure_size=(10, 10))+
                    theme(legend_position = (0.8,0.8))+
                    theme(text=element_text(size=20)))
    pcoaPlot.save('pcoa_plot.jpg')
    
    pc1BoxPlot = (ggplot(jsPcoa, aes(x='Env', y='PC1', fill='Env'))+
                    geom_boxplot()+
                    theme_bw()+ 
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank()))
    pc1BoxPlot.save('PC1_box.jpg', width=1, height=4.8)