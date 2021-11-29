import pandas as pd
import numpy as np


if __name__ == '__main__':
    rltAbundance = pd.read_csv('relative-abundance.csv', index_col=0)
    for column in rltAbundance.columns:
        rltAbundance[column] = rltAbundance[column].apply(lambda x: x if x > 0.001 else 0)
    rltAbundance['SUM'] = rltAbundance.apply(lambda x: x.sum(), axis=1)
    rltAbundance = rltAbundance[rltAbundance['SUM'] > 0.2]
    rltAbundance.to_csv('rlt-updated.csv')
    
    
        
