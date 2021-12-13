import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statannotations.Annotator import Annotator


if __name__ == '__main__':
    indeData = pd.read_csv('independent_result/layerMelt.csv')
    transData = pd.read_csv('transfer_result/layerMelt.csv')
    
    indeBox = sns.boxplot(x='Env', y='Contribution', data=indeData)
    annotator = Annotator(indeBox, [('Kindergarten', 'Pupils')], data=indeData, x='Env', y='Contribution')
    annotator.configure(alpha=0.5, test='Mann-Whitney', text_format='star', loc='outside')
    annotator.apply_and_annotate()
    plt.show()