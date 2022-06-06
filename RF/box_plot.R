library(ggplot2)
library(ggpubr)
library(dplyr)
library(reshape2)

RF_data <- read.csv('RF_result.csv')
RF_data$Env <- factor(RF_data$Env, levels = c('Young', 'Senior'))

RF_box_Plot <- ggplot(RF_data)+
                geom_boxplot(width = 0.5, aes(x = Env, y = Contribution, fill = Region), outlier.size = 0.5)+
                ylim(c(0, 1))+
                xlim(c('Young', 'Senior'))+
                xlab('')+
                ylab('Contribution')+
                scale_fill_manual(values=c('#FFBE7A', '#FA7F6F', '#82B0B2'))+
                theme_bw()+
                labs(title='RF for Senior group')+
                theme(text = element_text(size = 10),
                        plot.title = (element_text(hjust = 0.5)),
                        axis.text = element_text(size = 10, color = 'black'),
                        panel.grid.major = element_blank(), 
                        panel.grid.minor = element_blank(),
                        panel.background = element_blank(),
                        legend.title = element_blank(),
                        legend.position = (c(0.9, 0.12)),
                        legend.background = element_blank(),
                        legend.key.size = unit(0.3, 'cm'))
ggsave('RF_box_plot_elder.jpg', height = 70, width = 100, units = 'mm')