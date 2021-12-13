import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # Loading data
    ageMeta = pd.read_csv('../../data/normal-meta.csv', index_col=0)['Age']
    microbiomeMap = pd.DataFrame([f'root:{age}' for age in ageMeta.unique()])
    microbiomeMap.to_csv('microbiomes.txt', index=0, header=0)