library(readr)
Vestiti <- read_csv("Vestiti.csv")

# Ordinamento dataset -----
dati <- Vestiti[,-c(1,2,3,4)]
rm(Vestiti)

# Tabelle di frequenza -----
materiali <- dati[,-c(1:11)]
materiali <- materiali[,-45]

rm(dati)

#Nota: rimuovere i materiali che non hanno alcuna corrispondenza.
#Primo ciclo for per identificare i materiali che non hanno alcuna corrispondenza.
da_eliminare=rep(0,ncol(materiali))

for (i in 1:ncol(materiali)){
  if (is.na(table(materiali[,i])[2])==TRUE){
    da_eliminare[i]=i
  }
} 






materiali <- materiali[,-da_eliminare] #eliminazione dei materiali che non hanno prodotti associati
                                   #probabilmente è successo in quanto alcuni prodotti sono stati esclusi dal dataset.
rm(da_eliminare)
#Secondo ciclo for per creare la tabella di frequenza riguardante i materiali.
elenco_materiali=rep(0,ncol(materiali))
for (i in 1:ncol(materiali)){
  elenco_materiali[i]=table(materiali[,i])[2]
} 
rm(i)

## Dataframe -----
df <- materiali[1,]
df <- rbind(df,elenco_materiali)
df <- df[2,]
rm(elenco_materiali,materiali)


nomi <- colnames(df)
numeri <-as.vector(t(df[1,]))
df <- data.frame(nomi,numeri)
df<- df[order(df$numeri),]
rm(nomi,numeri)

## Table -----
#v=as.vector(t(df[1,]))
#v=as.table(v)
#rownames(v) <- colnames(df)
#barplot(v)

df$percentuale <- round(df$numeri * 100 /10191,2)


# Grafico -----

## Valori piccoli  -----
library(ggplot2)
options(repr.plot.width = 20, repr.plot.height =11)
ggplot(df[1:21,], aes(x=reorder(nomi,-percentuale), percentuale) )+
  geom_bar(stat = "identity",fill = "#FF6666",width = 0.5,  position=position_dodge(width =0.7))+ 
  scale_x_discrete("Fibre")+
  theme(axis.text.x = element_text(angle = 45,hjust=1))+
  labs( y="Proporzioni (%)",x="Materiali",title ="Tipi di fibre meno comuni [n=10'191]" )+ #Etichetta asse y
  geom_text(aes(label = round(percentuale,2)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
  theme(plot.title = element_text(hjust = 0.5,size=13))+
  scale_y_continuous(limits = c(0, 65))#+ #Impostare il titolo

## Esportare il grafico -----
ggsave("/Users/mattia/Desktop/dati/Grafici/3B)Fibre_meno_comuni.pdf", width = 20, height = 11, units = "cm")

## Valori grandi -----
options(repr.plot.width = 20, repr.plot.height =11)
ggplot(df[22:42,], aes(x=reorder(nomi,-percentuale), percentuale) )+
  geom_bar(stat = "identity",fill = "#FF6666",width = 0.5,  position=position_dodge(width =0.7))+ 
  scale_x_discrete("Fibre")+
  theme(axis.text.x = element_text(angle = 45,hjust=1))+
  labs( y="Proporzioni (%)",x="Materiali",title ="Tipi di fibre più comuni [n=10'191]" )+ #Etichetta asse y
  geom_text(aes(label = round(percentuale,1)), position = position_dodge(1), size=2.7,vjust=-0.5)+#Aggiunta scritte sulle colonne
theme(plot.title = element_text(hjust = 0.5,size=13))+ #Impostare il titolo
    scale_y_continuous(limits = c(0, 65))

ggsave("/Users/mattia/Desktop/dati/Grafici/3A)Fibre_piu_comuni.pdf", width = 20, height = 11, units = "cm")
  