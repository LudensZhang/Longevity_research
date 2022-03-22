import pandas as pd
import numpy as np
import re
from skbio.stats.ordination import *
from scipy.spatial.distance import pdist, squareform
from plotnine import *

if __name__ == '__main__':
    rawMeta = pd.read_csv('../../data_jiangsu_and_sichuan/metadata_whole.csv', index_col=0)
    rawAbundance = pd.read_csv('../../data_jiangsu_and_sichuan/abundance_whole.csv', index_col=0).T
    rawMeta.sort_index(inplace=True)
    rawAbundance = rawAbundance.loc[rawMeta.index.tolist()]
    jsDm = squareform(pdist(rawAbundance, metric='jensenshannon'))
    jsPcoa = pd.DataFrame(pcoa(jsDm, number_of_dimensions=2).samples.values.tolist(), 
                            index=rawAbundance.index, columns=['PC1', 'PC2'])
    jsPcoa['Env'] = rawMeta
    
    pcoaPlot = (ggplot(jsPcoa, aes('PC1', 'PC2', color='Env', fill='Env'))+
                    geom_point(size=2)+
                    stat_ellipse()+
                    theme_bw()+
                    scale_fill_manual(['#B24D5E', '#4D5EB2', '#5EB24D'])+
                    scale_color_manual(['#B24D5E', '#4D5EB2', '#5EB24D'])+
                    xlim(-0.5, 0.5)+
                    ylim(-0.5, 0.5)+
                    theme(axis_line = element_line(color="gray", size = 2))+
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())+
                    theme(figure_size=(10, 10))+
                    theme(legend_position = (0.8,0.8))+
                    theme(text=element_text(size=20)))
    pcoaPlot.save('pcoa_plot.jpg', dpi=300)
    
    pc1BoxPlot = (ggplot(jsPcoa, aes(x='Env', y='PC1', fill='Env'))+
                    geom_boxplot()+
                    theme_bw()+
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())+
                    theme(axis_line = element_line(color="gray", size = 1), axis_text_y = element_blank())+
                    coord_flip())
    pc1BoxPlot.save('PC1_box.jpg', width=4.8, height=1)
    
    pc2BoxPlot = (ggplot(jsPcoa, aes(x='Env', y='PC2', fill='Env'))+
                    geom_boxplot()+
                    theme_bw()+ 
                    theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())+
                    theme(axis_line = element_line(color="gray", size = 1), axis_text_x = element_blank()))
    pc2BoxPlot.save('PC2_box.jpg', width=1, height=4.8)