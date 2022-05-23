import pandas as pd
from skbio.diversity import beta_diversity
from skbio.diversity import alpha_diversity
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import*
# from statannotations.Annotator import Annotator
plt.style.use('ggplot')


def CalculateBcUnique(age, abundance):
    bcDm = beta_diversity("braycurtis", abundance, abundance.index).to_data_frame()
    minBc = bcDm.apply(lambda x: x.sort_values()[1], axis=1)
    minBc = minBc.rename('Bray-Curtis uniqueness').to_frame()
    minBc['Age'] = age
    return minBc

def CalculateShannon(age, abundance):
    shSr = alpha_diversity('shannon', abundance, abundance.index)
    shDf = pd.DataFrame(shSr, columns=["Shannon's Diversity"])
    shDf['Age'] = age
    return shDf



if __name__ =='__main__':
    rawMeta = pd.read_csv('../data_jiangsu_and_sichuan/metadata_whole.csv', index_col=0)
    rawAbundance = pd.read_csv('../data_jiangsu_and_sichuan/abundance_whole.csv', index_col=0).T
    rawMeta['Env'].replace('Elder', 'Senior', inplace=True)
    
    # group by age
    ageGroup = ['Young', 'Senior', 'Centenarian']
    dataList = [rawAbundance.loc[rawMeta[rawMeta['Env'] == age].index] for age in ageGroup]
    
    # calculate bray curtis uniqueness
    bcPlotFrame = pd.DataFrame(columns=['Bray-Curtis Uniqueness', 'Age'])
    for age, abundance in zip(ageGroup, dataList):
        bcPlotFrame = bcPlotFrame.append(CalculateBcUnique(age, abundance))
    bcPlotFrame = bcPlotFrame[bcPlotFrame['Age'] != 'Centenarian']
    
    # calculate shannon
    shPlotFrame = pd.DataFrame(columns=["Shannon's Diversity", 'Age'])
    for age, abundance in zip(ageGroup, dataList):
        shPlotFrame = shPlotFrame.append(CalculateShannon(age, abundance))

    # plot box plot
    bcBoxPlot = (ggplot(bcPlotFrame, aes(x='Age', y='Bray-Curtis uniqueness', fill='Age'))+
                geom_boxplot()+
                xlab('')+
                xlim(['Young', 'Senior'])+
                scale_fill_manual(['#B24D5E', '#4D5EB2'])+
                theme_bw()+
                theme(legend_position = (0.8, 0.78),
                      legend_title = element_blank(),
                      legend_key_size = 10))
    bcBoxPlot.save('bray_curtis_uniqueness.png', dpi=300)

    # shBoxPlot = (ggplot(shPlotFrame, aes(x='Age', y="Shannon's Diversity", fill='Age'))+
    #             geom_boxplot()+
    #             xlab('')+
    #             xlim(['Young', 'Elder', 'Centenarian'])+
    #             scale_fill_manual(['#B24D5E', '#4D5EB2', '#5EB24D'])+
    #             theme_bw()+
    #             theme(legend_position = (0.8, 0.2),
    #                   legend_title = element_blank(),
    #                   legend_key_size = 10))

    # shBoxPlot = sns.boxplot(data=shPlotFrame, x='Age', y="Shannon's Diversity")
    
    # pairs = [('Young', 'Senior'),
    #          ('Young', 'Centenarian'),
    #          ('Centenarian', 'Senior')]
    
    # shBoxPlot = Annotator(shBoxPlot, data=shPlotFrame, x='Age', y="Shannon's Diversity", pairs=pairs)
    # shBoxPlot.configure(test='Mann-Whitney')
    # shBoxPlot.apply_test()
    # shBoxPlot.annotate()
    # plt.savefig('Shannon_Diversity.png', dpi=300)