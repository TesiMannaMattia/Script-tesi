# Importazione dataset -----
Singolo_materiale <- read_csv("Grafico 4/Singolo_materiale.csv")

# Sistemare il dataset -----
dati <- Singolo_materiale[,-c(1:2)]

# Tabelle di frequenza -----
percentuali=prop.table(table(dati$Materiale,dati$Sesso))*100


## Dataframe della tabelle percentuale -----
tabella_percentuale <- as.data.frame.table(percentuali)
colnames(tabella_percentuale) <- c("Materiale","Sesso","Frequenza_Percentuale") 
tabella_percentuale <- tabella_percentuale[order(-tabella_percentuale$Frequenza_Percentuale), ]



library(ggplot2)
options(repr.plot.width = 20, repr.plot.height =10)
ggplot(tabella_percentuale, aes(x = reorder(Materiale,- Frequenza_Percentuale), y=Frequenza_Percentuale, fill = factor(Sesso))) + 
  geom_bar(stat = "identity",colour="black",width = 0.5,  position=position_dodge(width =0.7)) +
  theme(axis.text.x = element_text(angle = 45,hjust = 1))+  #Ruotare i nomi dell'asse x 
  labs( y="Proporzioni (%)",x="Materiali")+ #Etichetta asse y
 # geom_text(aes(label = round(Frequenza_Percentuale,2)), position = position_dodge(.7), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  theme(panel.grid.major.y = element_line(color = "grey70",size = 0.1,linetype = 1)) + #Mettere le linee
  ggtitle("Fibre più comuni negli indumenti \n composti da unico materiale [n=2'749]") + #Impostare il titolo
  theme(plot.title = element_text(hjust = 0.5))+ #Posizione del titolo
  theme(legend.position="top")+ #Posizione legenda
  scale_fill_discrete(name = " ", labels = c("Donne", "Uomini"))+  #Etichette legenda
  scale_y_continuous(limits = c(0,40))



## Esportare il grafico -----
ggsave("/Users/mattia/Desktop/dati/Grafici/4)Indumenti_singoli.pdf", width = 20, height = 10, units = "cm")
