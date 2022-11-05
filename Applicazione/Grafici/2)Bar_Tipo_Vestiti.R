# Importare il dataset -----
Vestiti <- read_csv("Vestiti.csv")

# Sistemare il dataset -----
dati <- Vestiti[,-c(1,2,3,4)]



# Tabella di frequenza singola e doppia -----
#freq <- table(dati$Tipo)
freq <- table(dati$Categoria)
doppia_freq <- table(dati$Sotto_categoria,dati$Sesso)

#Tabella di frequenza relativa
tabella_frequenze_relativa <- prop.table(freq)
doppia_relativa_freq <- prop.table(doppia_freq)

#Tabella di frequenza percentuale 
tabella_frequenze_percentuale <- prop.table(tabella_frequenze_relativa)*100
doppia_percentuale_freq <-  prop.table(doppia_relativa_freq)*100



tabella_percentuale <- as.data.frame.table(doppia_percentuale_freq)
colnames(tabella_percentuale) <- c("Categoria","Sesso","Frequenza_Percentuale") 
rm(freq,doppia_freq,tabella_frequenze_percentuale,doppia_percentuale_freq,doppia_relativa_freq,tabella_frequenze_relativa)
tabella_percentuale <- tabella_percentuale[order(-tabella_percentuale$Frequenza_Percentuale), ]

# Grafico -----
library(ggplot2)
options(repr.plot.width = 20, repr.plot.height =10)
ggplot(tabella_percentuale, aes(x = reorder(Categoria,- Frequenza_Percentuale), y=Frequenza_Percentuale, fill = factor(Sesso))) + 
  geom_bar(stat = "identity",colour="black",width = 0.5,  position=position_dodge(width =0.7)) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1))+  #Ruotare i nomi dell'asse x 
  labs( y="Proporzioni (%)",x="")+ #Etichetta asse y
  geom_text(aes(label = round(Frequenza_Percentuale,1)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  theme(panel.grid.major.y = element_line(color = "grey70",size = 0.1,linetype = 1)) + #Mettere le linee
  ggtitle("Tipi di indumenti più comuni [n=10'191]") + #Impostare il titolo
  theme(plot.title = element_text(hjust = 0.5))+ #Posizione del titolo
  theme(legend.position="top")+ #Posizione legenda
  scale_fill_discrete(name = " ", labels = c("Donne", "Uomini"))+  #Etichette legenda
  scale_y_continuous(limits = c(0,22))


## Esportare il grafico -----
ggsave("/Users/mattia/Desktop/dati/Grafici/2A)indumenti.pdf", width = 20, height = 10, units = "cm")

