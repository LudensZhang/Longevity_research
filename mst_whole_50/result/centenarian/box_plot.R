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
                geom_boxplot(aes(x=Env, y=Contribution, fill=Region), lwd=1)+
                ylim(c(0, 1))+
                xlim(c('Young', 'Senior'))+
                xlab('')+
                ylab('Contribution')+
                scale_fill_manual(values=c('#48de83', '#854bde', '#de854b'))+
                theme_bw()+
                labs(title='Independent Contribution for the Centenarian group')+
                theme(text=element_text(size=15),
                        plot.title=(element_text(hjust=0.5)),
                        legend.title=element_blank(),
                        legend.position=(c(0.9, 0.9)),
                        legend.key.size=unit(1, 'cm'))
ggsave('independent_box_plot_Centenarian.jpg', height=10, width=15)

trans.box.Plot <- ggplot(trans.Data)+
                geom_boxplot(aes(x=Env, y=Contribution, fill=Region), lwd=1)+
                ylim(c(0, 1))+
                xlim(c('Young', 'Senior'))+
                xlab('')+
                ylab('Contribution')+
                scale_fill_manual(values=c('#48de83', '#854bde', '#de854b'))+
                theme_bw()+
                labs(title='Transfer Contribution for the Centenarian group')+
                theme(text=element_text(size = 15),
                        plot.title=(element_text(hjust = 0.5)),
                        legend.title=element_blank(),
                        legend.position=(c(0.9, 0.9)),
                        legend.key.size=unit(1, 'cm'))
ggsave('transfer_box_plot_Centenarian.jpg', height=5, width=6)