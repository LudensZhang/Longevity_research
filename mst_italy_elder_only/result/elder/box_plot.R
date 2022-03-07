library(ggplot2)
library(ggpubr)
library(dplyr)
library(reshape2)

inde.Data <- read.csv('independent_result/layerMelt.csv')[, c(2,3)] 
trans.Data <- read.csv('transfer_result/layerMelt.csv')[, c(2,3)]
inde.Data['mode'] <- 'independent'
trans.Data['mode'] <- 'transfer'
bind.Data <- bind_rows(inde.Data, trans.Data)
# bind.Data$Env <- factor(bind.Data$Env, levels=c('Young','Middle age', 'Elder'))
bind.Data$Env <- factor(bind.Data$Env, levels=c('Young', 'Elder'))

box.Plot <- ggplot(bind.Data)+
                geom_boxplot(aes(x=Env, y=Contribution, fill=mode), show.legend=FALSE)+
                geom_point(aes(x=Env, y=-1, color=mode), shape=15, size=5)+
                geom_smooth(aes(x=as.numeric(Env), y=Contribution, linetype=mode), 
                method='loess', color='black', se=FALSE)+
                ylim(c(0, 1))+
                xlab('')+
                ylab('Contribution')+
                scale_color_manual(values=c('#D67F67', '#66D6B4'))+
                scale_fill_manual(values=c('#D67F67', '#66D6B4'))+
                guides()+
                theme_bw()+
                labs(title='MST result of the Elder group')+
                theme(text=element_text(size=30),
                        plot.title=(element_text(hjust=0.5)),
                        legend.title=element_blank(),
                        legend.position=(c(0.9, 0.93)),
                        legend.key.size=unit(1, 'cm'))
ggsave('box_plot_elder.jpg', height=10, width=15)