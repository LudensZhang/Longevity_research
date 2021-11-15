import pandas as pd
import re
from plotnine import*


if __name__ == '__main__':
    resultDf = pd.read_csv('./independent_result/layer-2.csv')
    resultDf.rename(columns={'Unnamed: 0': 'SampleID'}, inplace=True)
    resultMelt = resultDf.melt(id_vars='SampleID', var_name='Env', value_name='Contribution')
    resultMelt['Env'] = resultMelt['Env'].apply(lambda x: x[re.search('(root:)', x).end():] if re.search('(root:)', x) else x)
    p = (ggplot(resultMelt, aes(x='Env', y='Contribution'))+
         geom_boxplot()+
         theme_bw())
    p.save('./independent_result/plot.jpg')