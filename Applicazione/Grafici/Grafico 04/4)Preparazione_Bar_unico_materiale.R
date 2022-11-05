# Importazione dati e costruzione dataset -----
Vestiti <- read_csv("Vestiti.csv")
dati <- Vestiti[,-c(1:4)]
rm(Vestiti)
dati <- dati[dati$N.Fibre_Differenti==1,]

# Creazione tabelle di frequenza.
## Pulizia colonne inutili -----
da_eliminare=rep(0,ncol(dati))


for (i in 1:ncol(dati[,-c(c(1:11),56)])){
  if (is.na(table(dati[,i])[2])==TRUE){
    da_eliminare[i]=i
  }
} 


dati<- dati[,-da_eliminare] #eliminazione dei materiali che non hanno prodotti associati
#probabilmente è successo in quanto alcuni prodotti sono stati esclusi dal dataset.


#Note sul da farsi : bisogna riunificare le variabili binarie.

write.csv(dati,"/Users/mattia/Desktop/dati/dati_xG3.csv", row.names = TRUE)

materiali <-dati[,-c(1:11)] 
materiali <- materiali[,-ncol(materiali)]
write.csv(materiali,"/Users/mattia/Desktop/dati/materiali.csv", row.names = TRUE)


#Questi dataset sono stati presi ed importati su python.
#Una volta su python tramite pandas sono stati a loro volta puliti e importati nuovamente.

