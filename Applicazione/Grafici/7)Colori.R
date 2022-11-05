library(readr)
Vestiti <- read_csv("Vestiti.csv")

dati <- Vestiti[,-c(1:4)]
rm(Vestiti)

# Tabelle di frequenza
percentuale <- round(prop.table(table(dati$Colore))*100,2)


df <- data.frame(percentuale)
df<- df[order(-df$Freq),]
rm(percentuale,dati)





library(ggplot2)
options(repr.plot.width = 20, repr.plot.height =15)
ggplot(df, aes(x=reorder(Var1,-Freq), Freq) )+
  geom_bar(stat = "identity",fill =c( "Black",
                                      "Blue",
                                      "#DEB887",
                                      "Green",
                                      "White",
                                      "Grey",
                                      "Yellow",
                                      "Brown",
                                      "Pink",
                                      "#FFFFF0",
                                      "Purple",
                                      "Orange",
                                      "Red",
                                      "#00FFFF",
                                      "#FAEBD7"),width = 0.5,  position=position_dodge(width =0.7))+ 
  scale_x_discrete("Colori")+
  theme(axis.text.x = element_text(angle = 45,size = 8,hjust = 1))+
  labs( y="Proporzioni (%)",x="Colori",title = "Colori più comuni [n=10'191]")+ #Etichetta asse y
  geom_text(aes(label = round(Freq,2)), position = position_dodge(.7), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  theme(plot.title = element_text(hjust = 0.5,size=13))+  
  scale_y_continuous(limits = c(0,27)) #Impostare il titolo


ggsave("/Users/mattia/Desktop/dati/Grafici/7)Colori.pdf", width = 20, height = 11, units = "cm")

