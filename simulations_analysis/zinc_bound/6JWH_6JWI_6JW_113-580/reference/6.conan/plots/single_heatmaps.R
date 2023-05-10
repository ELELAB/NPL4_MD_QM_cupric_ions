library(ggplot2)
library(viridis)
library(dplyr) # data reformatting
library(tidyr) # data reformatting
library(stringr) # string manipulation
library(tidyverse)
library(patchwork)
library(gtools)


################
#filter the dataset for the contacts of NPL4 full lenght
#select the useful columns res1 res2 persistence
seq=c("IKELAVDEELEKEDGLIPRQKSKLCKHGDRGMCEYCSPLPPWDKEYHEKNKIKHISFHSYLKKLNENANKKENGSSYISPLSEPDFRINKRCHNGHEPWPRGICSKCQPSAITLQQQEFRMVDHVEFQKSEIINEFIQAWRYTGMQRFGYMYGSYSKYDNTPLGIKAVVEAIYEPPQHDEQDGLTMDVEQVKNEMLQIDRQAQEMGLSRIGLIFTDLSDAGAGDGSVFCKRHKDSFFLSSLEVIMAARHQTRHPNVSKYSEQGFFSSKFVTCVISGNLEGEIDISSYQVSTEAEALVTADMISGSTFPSMAYINDTTDERYVPEIFYMKSNEYGITVKENAKPAFPVDYLLVTLTHGFPNTDTETNSKFVSSTGFPWSNRQAMGQSQDYQELKKYLFNVASSGDFNLLHEKISNFHLLLYINSLQILSPDEWKLLIESAVKNEWEESLLKLVSSAGWQTLVMILQESGZZ")
seq1<- as.vector(str_split_fixed(seq, pattern = "", n = nchar(seq)))
conan_num <- c(1:470)
true_num <- c(113:582) # the capping are read as residues 
renumbered<- paste(seq1,true_num, sep = "")

prot1<-read.table("../aggregate/timeline.dat",header = FALSE,fill = TRUE)
prot_df1<-prot1%>%select(V1,V2,V5,V7)
colnames(prot_df1)<-c("V1","V2","persistence","num_events")
prot_df2 <- prot_df1

prot_df2<-prot_df2[prot_df2$V1 == 469 | prot_df2$V1 == 470  ,]
prot_df2[prot_df2 == 469] <- "Z581"
prot_df2[prot_df2 == 470] <- "Z582"
prot_df2['V2'] <- renumbered
colnames(prot_df2)<-c("residue1","residue2","Occurrence", "Num. contact events")
final_prot_df <- prot_df2
final_prot_df <- filter_if(final_prot_df, is.numeric, all_vars((.) != 0))

#write a csv with final values
write.csv(final_prot_df, "prot_conan_contact.csv",row.names = F)

#single residue heatmaps  
colnames(final_prot_df)<-c("V1","V2","V5", "V7")
res <- c("Z581","Z582")
for(var in res)
{
  d = subset(final_prot_df, V1 == var)
  d2 <- d
  d2[d2 == 0] <- NA
  d3 <- d2[!is.na(d2$V5), ]
  level_order <- factor(d3$V2)
  max_var <- max(d$V7)
  plot1 <- ggplot(d3, aes(x = factor(V1), y = factor(V2, level_order), fill = as.numeric(V5))) + geom_tile() + scale_fill_viridis(begin =0, end =1, option = "viridis", direction = -1, limits=c(0, 1)) + theme_bw() + theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 12), axis.text.y=element_text(color="black",size=8)) + xlab("residue") + ylab("residue") + labs(fill='Occurrence')
  plot2 <- ggplot(d3, aes(x = factor(V1), y = factor(V2, level_order), fill = as.numeric(V7))) + geom_tile() + scale_fill_viridis(begin =0, end =1, option = "magma", direction = -1, limits=c(0, max_var)) + theme_bw() + theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 12), axis.text.y=element_text(color="black",size=8)) + xlab("residue") + ylab("residue") + labs(fill='Num. of contact formation')
  pdf(paste("Heatmap", var,"pdf", sep="."))
  require(gridExtra)
  #plot1 + labs(x = "residue", y = "residue", fill = "Persistence during time")
  grid.arrange(plot1, plot2, ncol=2)
  dev.off()
}
