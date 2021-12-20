import pandas as pd
from plotnine import *


if __name__ == '__main__':
    centenarienInde = pd.read_csv('centenarien/independent_result/layer-2.csv')
    centenarienTrans = pd.read_csv('centenarien/transfer_result/layer-2.csv')
    elderInde = pd.read_csv('elder/independent_result/layer-2.csv')
    elderTrans = pd.read_csv('elder/transfer_result/layer-2.csv')
    centenarienInde = centenarienInde.melt(id_vars='Unnamed: 0')
    centenarienTrans = centenarienTrans.melt(id_vars='Unnamed: 0')
    elderInde = elderInde.melt(id_vars='Unnamed: 0')
    elderTrans = elderTrans.melt(id_vars='Unnamed: 0')
    centenarienInde['mode'] = 'Independent'
    centenarienTrans['mode'] = 'Transfer'
    elderInde['mode'] = 'Independent'
    elderTrans['mode'] = 'Transfer'
    centenarienData = centenarienInde.append(centenarienTrans, ignore_index=True)
    elderData = elderInde.append(elderTrans, ignore_index=True)
    print(elderData)
    
    centenarienBox = (ggplot(centenarienData, aes(x='variable', y='value', fill='mode'))+
    	    	    	geom_boxplot()+
			ggtitle('MST result of centenarien')+
			xlab('Env')+
			ylab('Contibution')+
			theme(plot_title=element_text(hjust=0.5)))
    centenarienBox.save('centenarienBox.jpg')
    
