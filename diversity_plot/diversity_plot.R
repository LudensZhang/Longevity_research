library(dplyr)
library(ggplot2)
library(ggpubr)
library(vegan)
library(picante)
library(Unicode)

CalculateShannon <- function(abundance){
    abundance <- t(abundance)
    return (diversity(abundance, 'simpson'))

}

abundance_whole <- read.csv('../data_jiangsu_and_sichuan/abundance_whole.csv')
meta_whole <- read.csv('../data_jiangsu_and_sichuan/metadata_whole.csv')

meta_senior <- meta_whole %>%
                mutate(Env = replace(Env, Env == 'Elder', 'Senior')) %>%
                filter(Env == 'Senior')
abundance_senior <- abundance_whole[meta_senior$X]

meta_young <- meta_whole %>%
                filter(Env == 'Young')
abundance_young <- abundance_whole[meta_young$X]


shannon_senior <- tibble(shannon = CalculateShannon(abundance_senior))
shannon_senior$Env = 'Senior'

shannon_young <- tibble(shannon = CalculateShannon(abundance_young))
shannon_young$Env = 'Young'

shannon_result <- rbind(shannon_senior, shannon_young)
shannon_result$Env = factor(shannon_result$Env, levels = c('Young', 'Senior'))

p.val <- " = 0.026"
italic_p <- u_char_inspect(u_char_from_name("MATHEMATICAL BOLD ITALIC CAPITAL P"))["Char"]

box_plot <-ggplot(shannon_result, aes(x = Env, y = shannon, fill = Env)) +
            geom_boxplot(width = 0.5, show.legend = FALSE, outlier.size = 0.5) +
            scale_fill_manual(values=c('#B24D5E', '#4D5EB2')) +
            xlab('') +
            ylab("Simpson index") +
            ylim(c(0, 1.5)) +
            annotate(geom = "text",
                        label = paste("Wilconxon, ", italic_p, p.val, sep = ''),
                        x = 1.5,
                        y = 1.4,
                        size = 3) +
            # stat_compare_means(method = 'wilcox.test', 
            #                     label = "p.format",  
            #                     label.x = 1.4, 
            #                     label.y = 1.4,
            #                     size = 3) +
            theme_bw() +
            theme(text = element_text(size = 10),
                    axis.text = element_text(size = 10, color = 'black'),
                    panel.grid.major = element_blank(), 
                    panel.grid.minor = element_blank(),
                    panel.background = element_blank(),)
ggsave('Simpson_Diversity.png', height = 70, width = 100, units = 'mm')