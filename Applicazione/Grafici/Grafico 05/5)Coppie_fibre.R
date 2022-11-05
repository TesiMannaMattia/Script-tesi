# Importazione dataset -----
Coppie_fibre <- read_csv("Grafico 5/Coppie_fibre.csv")

# Sistemare dati -----
dati <- Coppie_fibre[,-1]
rm(Coppie_fibre)

# Tabelle di frequenza
percentuale <- round(prop.table(table(dati$Coppie))*100,2)


df <- data.frame(percentuale)
df<- df[order(-df$Freq),]
rm(percentuale,dati)





library(ggplot2)
options(repr.plot.width = 20, repr.plot.height =15)
ggplot(df[1:11,], aes(x=reorder(Var1,-Freq), Freq) )+
  geom_bar(stat = "identity",fill = "#FF6666",width = 0.5,  position=position_dodge(width =0.7))+ 
  scale_x_discrete("Coppia di fibre")+
  theme(axis.text.x = element_text(angle = 45,size = 8,hjust = 1))+
  labs( y="Proporzioni (%)",x="Materiali",title = "Combinazioni di due fibre più comuni [n=4'678]")+ #Etichetta asse y
  geom_text(aes(label = round(Freq,2)), position = position_dodge(.7), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  theme(plot.title = element_text(hjust = 0.5,size=13))+  
  scale_y_continuous(limits = c(0,27)) #Impostare il titolo
 

ggsave("/Users/mattia/Desktop/dati/Grafici/5)Combinazione_2Fibre_MC.pdf", width = 20, height = 11, units = "cm")


