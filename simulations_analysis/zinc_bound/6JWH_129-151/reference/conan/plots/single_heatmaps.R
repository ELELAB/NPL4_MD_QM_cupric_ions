library(ggplot2)
library(viridis)
library(dplyr) # data reformatting
library(tidyr) # data reformatting
library(stringr) # string manipulation
library(tidyverse)
library(patchwork)
library(gtools)

#select the residues corresponding to NPL4 zinc finger 1 
res <- c("I129","P130","R131","Q132","K133","S134","K135","L136","C137","K138","H139",
         "G140","D141","R142","G143","M144","C145","E146","Y147","C148","S149","P150",
         "L151","Z152")
# rename residue from ConAn to the corresponding one in NPL4
seq_res <- "IPRQKSKLCKHGDRGMCEYCSPLZ"
# split string into single residue names
single_seq_res <- strsplit(seq_res, "")[[1]]
#number of the starting residue
start_res = 129
#generate list of residue numbers
num_res <- seq(start_res, 152, 1)
#load the CONAN file
prot<-read.table("../aggregate/timeline.dat",header = FALSE,fill = TRUE)
#max column of encounters to use in the plots
max_var=max(prot$V7)

################
#filter the dataset for the contacts of NPL4
#select the useful columns res1 res2 persistence
prot_df1<-prot%>%select(V1,V2,V5,V7)
colnames(prot_df1)<-c("V1","V2","persistence","num_events")
prot_df2 <- prot_df1
#filter the residues
#prot_df2<-prot_df1%>%filter(V1 %in% res_prot)
#filter the contacts with persistence 20%
#prot_df2<-prot_df2%>%filter(persistence >= 0.2)
#renumber and rename residues
prot_df2$seq2 = prot_df2$V2
prot_df2$seq1 = prot_df2$V1
prot_df2$V2 <- single_seq_res[prot_df2$V2]
prot_df2$V1 <- single_seq_res[prot_df2$V1]
prot_df2$seq2 <- num_res[prot_df2$seq2]
prot_df2$seq1 <- num_res[prot_df2$seq1]
prot_df2$x <- paste(prot_df2$V2,prot_df2$seq2, sep = "")
prot_df2$y <- paste(prot_df2$V1,prot_df2$seq1, sep = "")
prot_df3 <- prot_df2[ -c(1,2,5,6) ]
#generate final dataframe
final_prot_df <- prot_df3[, c(4, 3, 1, 2)]
colnames(final_prot_df)<-c("residue","residue","Occurrence", "Num. contact events")
#write a csv with final values
write.csv(final_prot_df, "prot_conan_contact.csv",row.names = F)

#single residue heatmaps  
colnames(final_prot_df)<-c("V1","V2","V5", "V7")
for(var in res)
{
  d = subset(final_prot_df, V1 == var)
  d2 <- d
  d2[d2 == 0] <- NA
  d3 <- d2[!is.na(d2$V5), ]
  level_order <- factor(d3$V2)
  plot1 <- ggplot(d3, aes(x = factor(V1), y = factor(V2, level_order), fill = as.numeric(V5))) + geom_tile() + scale_fill_viridis(begin =0, end =1, option = "viridis", direction = -1, limits=c(0, 1)) + theme_bw() + theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 12), axis.text.y=element_text(color="black",size=8)) + xlab("residue") + ylab("residue") + labs(fill='Occurrence')
  plot2 <- ggplot(d3, aes(x = factor(V1), y = factor(V2, level_order), fill = as.numeric(V7))) + geom_tile() + scale_fill_viridis(begin =0, end =1, option = "magma", direction = -1, limits=c(0, max_var)) + theme_bw() + theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 12), axis.text.y=element_text(color="black",size=8)) + xlab("residue") + ylab("residue") + labs(fill='Num. of contact formation')
  pdf(paste("Heatmap", var,"pdf", sep="."))
  require(gridExtra)
  #plot1 + labs(x = "residue", y = "residue", fill = "Persistence during time")
  grid.arrange(plot1, plot2, ncol=2)
  dev.off()
}
