import pandas as pd
from skbio.diversity import beta_diversity
from plotnine import*


def CalculateBcUnique(age, abundance):
    bc_dm = beta_diversity("braycurtis", abundance, abundance.index).to_data_frame()
    minBc = bc_dm.apply(lambda x: x.sort_values()[1], axis=1)
    minBc = minBc.rename('Bray-Curtis uniqueness').to_frame()
    minBc['Age'] = age
    return minBc


if __name__ =='__main__':
    rawMeta = pd.read_csv('../data_jiangsu_and_sichuan/metadata_whole.csv', index_col=0)
    rawAbundance = pd.read_csv('../data_jiangsu_and_sichuan/abundance_whole.csv', index_col=0).T
    
    # group by age
    ageGroup = ['Young', 'Elder', 'Centenarian']
    dataList = [rawAbundance.loc[rawMeta[rawMeta['Env'] == age].index] for age in ageGroup]
    
    # calculate bray curtis uniqueness
    plotFrame = pd.DataFrame(columns=['Bray-Curtis uniqueness', 'Age'])
    for age, abundance in zip(ageGroup, dataList):
        plotFrame = plotFrame.append(CalculateBcUnique(age, abundance))

    # plot box plot
    boxPlot = (ggplot(plotFrame, aes(x='Age', y='Bray-Curtis uniqueness', fill='Age'))+
                geom_boxplot()+
                xlab('')+
                xlim(['Young', 'Elder', 'Centenarian'])+
                scale_fill_manual(['#B24D5E', '#4D5EB2', '#5EB24D'])+
                theme_bw()+
                theme(legend_position = (0.8, 0.78),
                      legend_title = element_blank(),
                      legend_key_size = 10))

    boxPlot.save('bray_curtis_uniqueness.png', dpi=300)