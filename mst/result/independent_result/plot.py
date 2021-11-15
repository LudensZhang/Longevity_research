import pandas as pd
from plotnine import*


if __name__ == '__main__':
    resultDf = pd.read_csv('layer-2.csv')
    resultDf.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
    resultMelt = resultDf.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
    p = (ggplot(resultMelt, aes(x='Env', y='Contribution'))+
         geom_boxplot()+
         theme_bw())
    p.save('plot.jpg')