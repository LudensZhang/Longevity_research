library(dplyr)
library(ggplot2)
library(vegan)
library(ape)

abundance_whole <- read.csv('../data_jiangsu_and_sichuan/abundance_whole.csv')[ ,-1]
meta_whole <- read.csv('../data_jiangsu_and_sichuan/metadata_whole.csv')

meta_no_cent <- meta_whole %>%
                mutate(Env = replace(Env, Env =='Elder', 'Senior')) %>%
                filter(Env != 'Centenarian')

abundance_no_cent <- abundance_whole[meta_no_cent$X]

bray_dis <- vegdist(t(abundance_no_cent), method = 'bray')
pcoa_frame <- pcoa(bray_dis)
x_label<-round(pcoa_frame$values$Rel_corr_eig[1]*100,2)
y_label<-round(pcoa_frame$values$Rel_corr_eig[2]*100,2)
plot_frame <- data.frame(pcoa_frame$vectors)
meta_no_cent$Env <- factor(meta_no_cent$Env, levels = c('Young', 'Senior'))

PCoA_plot <- ggplot(plot_frame, aes(Axis.2, Axis.1, fill = meta_no_cent$Env, color = meta_no_cent$Env)) +
                geom_point(size=0.5) +
                stat_ellipse(show.legend = FALSE) +
                theme_bw() +
                scale_color_manual(values = c('#B24D5E', '#4D5EB2')) +
                xlim(-0.55, 0.65) +
                ylim(-0.55, 0.65) +
                xlab(paste0("PCoA1 ",x_label,"%")) +
                ylab(paste0("PCoA2 ",y_label,"%")) +
                theme(axis.text = element_text(size = 10, color = 'black'),
                        panel.grid.major = element_blank(), 
                        panel.grid.minor = element_blank(),
                        panel.background = element_blank(),
                        # legend.position = c(1.5, 1.5),
                        legend.key.size = unit(0.5, 'cm'),
                        legend.title = element_blank(),
                        text = element_text(size = 10))
ggsave('PCoA_plot.png', height = 70, width = 100, units = ('mm'))