library(ggplot2)
library(ggpubr)
library(dplyr)
library(reshape2)

inde.Data <- read.csv('independent_result/layerMelt.csv')[, c(2,3)] 
trans.Data <- read.csv('transfer_result/layerMelt.csv')[, c(2,3)]
inde.Data['mode'] <- 'independent'
trans.Data['mode'] <- 'transfer'
bind.Data <- bind_rows(inde.Data, trans.Data)

box.Plot <- ggplot(bind.Data, aes(x = Env, y = Contribution, fill=mode))+
                geom_boxplot()+
                xlim(c('Kindergarten', 'Pupils', 'Middle school', 'Youth', 'Middle age', 'Elder'))+
                ylim(c(0, 1))+
                xlab('')+
                ylab('Contribution')+
                theme_bw()+
                geom_smooth()

inde.Box.Plot = ggplot(inde.Data, aes(x=forcats::fct_relevel(Env, 'Kindergarten', 'Pupils', 'Middle school', 'Youth', 'Middle age', 'Elder'), y=Contribution))+
    geom_boxplot(fill=c('#5F9933', '#57E6D8', '#E68057', '#3E4A99', '#EBCF68', '#923299'), lwd=1)+
    theme_bw()+
    ylim(c(0,1))+
    xlab('')+ 
    ylab('Contribution')+
    labs(title='Independent result')+
    stat_compare_means(label='p.signif', comparisons=list(c('Kindergarten', 'Pupils')), method='wilcox.test', hide.ns=TRUE, label.y=0.9, size=10)+
    theme(text=element_text(size=30),
            plot.title=(element_text(hjust = 0.5)))
ggsave('independent_boxplot.jpg', height=10, width=12)

trans.Box.Plot = ggplot(trans.Data, aes(x=forcats::fct_relevel(Env, 'Kindergarten', 'Pupils', 'Middle school', 'Youth', 'Middle age', 'Elder'), y=Contribution))+
    geom_boxplot(fill=c('#5F9933', '#57E6D8', '#E68057', '#3E4A99', '#EBCF68', '#923299'), lwd=1)+
    theme_bw()+
    ylim(c(0, 1))+
    xlab('')+
    ylab('Contribution')+
    labs(title='Transfer result (DM)')+
    theme(text=element_text(size=30),
            plot.title=(element_text(hjust = 0.5)))
ggsave('transfer_boxplot.jpg', height=10, width=12)