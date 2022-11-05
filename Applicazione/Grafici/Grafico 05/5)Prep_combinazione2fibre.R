# Importazione dati -----
Vestiti <- read_csv("Vestiti.csv")

# Sistemare dataset
dati <- Vestiti[,-c(1:4)]
rm(Vestiti)

# Estrarre solo 2 fibre:
dati <- dati[dati$N.Fibre_Differenti==2,]


da_eliminare=rep(0,ncol(dati))


for (i in 1:ncol(dati[,-c(c(1:11),56)])){
  if (is.na(table(dati[,i])[2])==TRUE){
    da_eliminare[i]=i
  }
} 


dati<- dati[,-da_eliminare]
rm(i,da_eliminare)

materiali <- dati[,c(12:40)]

#Esportare il dataset per lavorarci in pandas(python):
write.csv(dati,"/Users/mattia/Desktop/dati/grafico 4/dati.csv", row.names = TRUE)
write.csv(materiali,"/Users/mattia/Desktop/dati/grafico 4/materiali.csv", row.names = TRUE)





