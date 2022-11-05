library(readr)
# Importazione dataset -----
Singolo_materiale <- read_csv("Grafico 4/Singolo_materiale.csv")

require(tidyverse) 
require(magrittr) 
require(knitr) 
require(DT) 
require(caret)
library(readr)
library(tidyverse)
library(grid)

df <- Singolo_materiale %>% filter(Materiale %in% c("Poliestere","Cotone","Viscosa","Acrilico"))
rm(Singolo_materiale)
# TABELLE DI FREQUENZA -----
#Tabella di frequenza
doppia_freq <- table(df$Materiale,df$Colore)

#Tabella di frequenza relativa
doppia_relativa_freq <- prop.table(doppia_freq)

#Tabella di frequenza percentuale 
doppia_percentuale_freq <-  round(prop.table(doppia_relativa_freq)*100,2)
tabella_percentuale <- as.data.frame.table(doppia_percentuale_freq)
colnames(tabella_percentuale) <- c("Materiale","Colore","Frequenza_Percentuale") 
tabella_percentuale <- tabella_percentuale[order(-tabella_percentuale$Frequenza_Percentuale), ]

#Eliminare roba inutile 
rm(doppia_freq,doppia_percentuale_freq,doppia_relativa_freq)


# COTONE ----
cotone <- tabella_percentuale[tabella_percentuale$Materiale=="Cotone",]
library(ggplot2)
p1 <- ggplot(cotone, aes(x=reorder(Colore,-Frequenza_Percentuale), Frequenza_Percentuale) )+
  geom_bar(stat = "identity",fill=c("Blue","Black",
                                    "White",
                                    "#DEB887",
                                    "Green","Grey",
                                    "Yellow","Brown",
                                    "Pink","#FFFFF0",
                                    "Purple","Red",
                                    "Orange","#00FFFF"),width = 0.5,  position=position_dodge(width =0.7))+ 
  theme(axis.text.x = element_text(angle = 45,hjust=1))+
  labs( y="Proporzioni (%)",x="Cotone" )+ #Etichetta asse y
  geom_text(aes(label = round(Frequenza_Percentuale,2)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  scale_y_continuous(limits = c(0, 13))#+ #Impostare il titolo
p1
#ggsave("/Users/mattia/Desktop/6)Cotone.jpg", width = 20, height = 10, units = "cm")




# POLIESTERE ----
poliestere <- tabella_percentuale[tabella_percentuale$Materiale=="Poliestere",]
library(ggplot2)
#options(repr.plot.width = 20, repr.plot.height =11)
p2 <- ggplot(poliestere, aes(x=reorder(Colore,-Frequenza_Percentuale), Frequenza_Percentuale) )+
  geom_bar(stat = "identity",fill =c("Black","#DEB887",
                                     "Green",
                                     "Blue",
                                     "Yellow","White",
                                     "Grey","Brown",
                                     "Pink","Orange",
                                     "Purple","Red",
                                     "#00FFFF","#FFFFF0"),width = 0.5,  position=position_dodge(width =0.7))+ 
  scale_x_discrete("Poliestere")+
  theme(axis.text.y=element_blank(),axis.text.x = element_text(angle = 45,hjust=1))+ #Etichetta asse y
  geom_text(aes(label = round(Frequenza_Percentuale,2)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  scale_y_continuous(limits = c(0, 13),ylab(" "))
p2
#ggsave("/Users/mattia/Desktop/dati/Grafici/6)Poliestere.jpg", width = 20, height = 10, units = "cm")

library(ggplot2)
library(cowplot)
library(grid)
library(gridExtra)



# VISCOSA ----
viscosa <- tabella_percentuale[tabella_percentuale$Materiale=="Viscosa",]
library(ggplot2)
p3 <- ggplot(viscosa, aes(x=reorder(Colore,-Frequenza_Percentuale), Frequenza_Percentuale) )+
  geom_bar(stat = "identity",fill = c("Black","Orange",
           "Green",
           "#DEB887",
           "Red","Yellow",
           "Blue","Pink",
           "White","Brown",
           "Grey","Purple","#FFFFF0",
           "#00FFFF"),width = 0.5,  position=position_dodge(width =0.7))+ 
  labs(y="Proporzioni (%)",x="Viscosa")+
  theme(axis.text.x = element_text(angle = 45,hjust=1))+ #Etichetta asse y
  geom_text(aes(label = round(Frequenza_Percentuale,2)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  scale_y_continuous(limits = c(0, 13))
p3
#ggsave("/Users/mattia/Desktop/dati/Grafici/6)Viscosa.jpg", width = 20, height = 10, units = "cm")


# ACRILICO ----
Acrilico <- tabella_percentuale[tabella_percentuale$Materiale=="Acrilico",]
library(ggplot2)
options(repr.plot.width = 20, repr.plot.height =11)
p4 <-  ggplot(Acrilico, aes(x=reorder(Colore,-Frequenza_Percentuale), Frequenza_Percentuale) )+
  geom_bar(stat = "identity",fill =c("Black","Blue",
                                     "Yellow",
                                     "White",
                                     "Brown","Green",
                                     "Purple","Grey",
                                     "Pink","#DEB887",
                                     "Red","Orange","#FFFFF0",
                                     "#00FFFF"),width = 0.5,  position=position_dodge(width =0.7))+ 
  scale_x_discrete("Acrilico")+
  theme(axis.text.y=element_blank(),axis.text.x = element_text(angle = 45,hjust=1))+ #Etichetta asse y
  geom_text(aes(label = round(Frequenza_Percentuale,2)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  scale_y_continuous(limits = c(0, 13),ylab(""))
p4
#ggsave("/Users/mattia/Desktop/dati/Grafici/6)Acrilico.jpg", width = 20, height = 10, units = "cm")



library(ggpubr)
figure <- ggarrange(p1, p2, p3,p4,ncol = 2, nrow = 2)
figure
#ggsave("/Users/mattia/Desktop/2.pdf",figure)


png(
  filename="/Users/mattia/Desktop/VHR_C_Colori_Fibre.png",
  width=10,
  height=5,
  units="in",
  res=1000)

figure
dev.off()


