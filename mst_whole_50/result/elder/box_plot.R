library(ggplot2)
library(ggpubr)
library(dplyr)
library(reshape2)

inde.Data <- read.csv('whole_independent_result.csv') 
trans.Data <- read.csv('whole_transfer_result.csv')
inde.Data['mode'] <- 'independent'
trans.Data['mode'] <- 'transfer'
bind.Data <- bind_rows(inde.Data, trans.Data)
# bind.Data$Env <- factor(bind.Data$Env, levels=c('Young','Middle age', 'Elder'))
bind.Data$Env <- factor(bind.Data$Env, levels=c('Young', 'Senior'))

inde.Data$Env <- factor(inde.Data$Env, levels=c('Young', 'Senior'))
inde.Data$Env <- factor(inde.Data$Env, levels=c('Young', 'Senior'))

inde.box.Plot <- ggplot(inde.Data)+
                geom_boxplot(aes(x=Env, y=Contribution, fill=Region), width = 0.5, outlier.size = 0.5)+
                ylim(c(0, 1))+
                xlim(c('Young', 'Senior'))+
                xlab('')+
                ylab('Contribution')+
                scale_fill_manual(values=c('#FFBE7A', '#FA7F6F', '#82B0B2'))+
                theme_bw()+
                labs(title = 'Independent Contribution for the Senior group')+
                theme(text = element_text(size = 10),
                        plot.title = (element_text(hjust = 0.5)),
                        axis.text = element_text(size = 10, color = 'black'),
                        panel.grid.major = element_blank(), 
                        panel.grid.minor = element_blank(),
                        panel.background = element_blank(),
                        legend.title = element_blank(),
                        legend.position = (c(0.9, 0.88)),
                        legend.background = element_blank(),
                        legend.key.size = unit(0.3, 'cm'))
ggsave('independent_box_plot_elder.jpg', height = 70, width = 100, units = 'mm')

trans.box.Plot <- ggplot(trans.Data)+
                geom_boxplot(width = 0.5, aes(x=Env, y=Contribution, fill=Region), outlier.size = 0.5)+
                ylim(c(0, 1))+
                xlim(c('Young', 'Senior'))+
                xlab('')+
                ylab('Contribution')+
                scale_fill_manual(values=c('#FFBE7A', '#FA7F6F', '#82B0B2'))+
                theme_bw()+
                labs(title='Transfer Contribution for the Senior group')+
                theme(text = element_text(size = 10),
                        plot.title = (element_text(hjust = 0.5)),
                        axis.text = element_text(size = 10, color = 'black'),
                        panel.grid.major = element_blank(), 
                        panel.grid.minor = element_blank(),
                        panel.background = element_blank(),
                        legend.title = element_blank(),
                        legend.position = (c(0.9, 0.88)),
                        legend.background = element_blank(),
                        legend.key.size = unit(0.3, 'cm'))
ggsave('transfer_box_plot_elder.jpg', height = 70, width = 100, units = 'mm')