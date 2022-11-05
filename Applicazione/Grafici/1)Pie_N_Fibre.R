
Vestiti <- read_csv("Vestiti.csv")
# Rimozione colonne inutili -----
dati <- Vestiti[,-c(1,2,3,4)]


# Classi -----
dati$N.Fibre <- dati$N.Fibre_Differenti 
dati$N.Fibre[dati$N.Fibre >= 4]=4


# Tabelle di frequenza -----
nfibre <- table(dati$N.Fibre)
percentuale_fibre <- round(prop.table(nfibre)*100,0)
percentuale_fibre 

# Grafico -----
# Dataframe per il grafico.
Product <- c("1 Fibra","2 Fibre","3 Fibre","4+ Fibre")
Value   <-  nfibre

df <- data.frame(Product,Value)

# Creazione etichetta.
df$Label <- paste(Product,"[n=",nfibre,"]\n ",percentuale_fibre,"%")

pie(nfibre,labels=df$Label,
    main="Composizione indumenti (Numero di fibre differenti)\n[Numero indumenti=10191]",
    col=c("Light Green","Pink","Light Blue","Purple")
    )




