
#Si importano tutti i dataset parziali:
    #HM
    #Hollister
    #Armani
#Per ovvie ragioni ogni sito ha un algoritmo di estrazione proprio.
#I dataset sono quindi stati creati separatamente facendo attenzione ad avere una struttura unica.
#Ora verranno riuniti.
#Sono escluse dall'unione le variabili:
    #Codice prodotto da ARMANI
    #Gruppo da HM e Hollister
    #N_fibre_differenti da tutti, verrà ricalcolata.
    
#Nei processi di pulizia di ogni singolo dataset è stata prestata molta attenzione all'univocità dei nomi delle
#fibre e dei colori, così da evitare che nero e Nero siano diverse. Ed anche cotone e cotton devono codificare
#per la medesima variabile binaria.

import pandas as pd

#ARMANI
#df1= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_ARMANI.csv")
#print(df1.columns)
df1= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_ARMANI.csv",
                 usecols=['Sesso', 'Categoria', 'Sotto_categoria', 'Marca',
                        'Articolo', 'Prezzo', 'Materiali', 'Colore', 'Link', 'Acetato',
                        'Acrilico', 'Altre_fibre', 'Cashmere', 'Cotone', 'Cupro', 'Elastan',
                        'Elastolefin', 'Elastomultiestere', 'Fibra_di_metallo',
                        'Fibre_sintetiche', 'Lana', 'Lino', 'Lyocell', 'Modacrilica', 'Pelle',
                        'Poliammide', 'Poliestere', 'Poliuretano', 'Polivinilcloruro', 'Seta',
                        'Shearling', 'Triacetato', 'Viscosa'])


#HM
#df2= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_HM.csv")
#print(df2.columns)
df2= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_HM.csv",
                 usecols=[ 'Sesso', 'Categoria',
                        'Sotto_categoria', 'Marca', 'Articolo', 'Prezzo', 
                        'Materiali', 'Colore',  'Link', 'Acetato', 'Acrilico',
                        'Alluminio', 'Alpaca', 'Altre_fibre', 'Canapa', 'Carta', 'Cashmere',
                        'Cotone', 'Elastan', 'Elastodiene', 'Elastomultiestere',
                        'Etilenvinilacetato', 'Fibra_di_acido_polilattico',
                        'Fibra_di_asclepiade', 'Fibra_di_metallo', 'Lana', 'Lattice', 'Lino',
                        'Lyocell', 'Modacrilica', 'Mohair', 'Paglia', 'Pelle', 'Pelo_di_yak',
                        'Piuma', 'Poliammide', 'Policarbonato', 'Poliestere', 'Polietilene',
                        'Polipropilene', 'Polistirene', 'Poliuretano', 'Seta', 'Viscosa'])


#HOLLISTER
#df3= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_Hollister.csv")
#print(df3.columns)
df3= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_Hollister.csv",
                 usecols=['Sesso', 'Categoria',
                        'Sotto_categoria', 'Marca', 'Articolo', 'Prezzo', 
                        'Materiali', 'Colore',  'Link', 'Acrilico', 'Cashmere',
                        'Cotone', 'Elastan', 'Fibra_di_metallo', 'Gomma', 'Lana', 'Lino',
                        'Lyocell', 'Modacrilica', 'Nylon', 'Poliestere', 'Poliuretano',
                        'Viscosa'])
#Gucci
#df4= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_Gucci.csv")
#print(df4.columns)
df4= pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_Gucci.csv",
                 usecols=['Sesso', 'Categoria', 'Sotto_categoria', 'Marca',
                        'Articolo', 'Prezzo', 'Materiali', 'Colore',  'Link',
                        'Acetato', 'Acrilico', 'Altre_fibre', 'Anatra', 'Canapa', 'Carta',
                        'Cashmere', 'Ceramica', 'Cotone', 'Cupro', 'Elastan',
                        'Fibra_di_metallo', 'Gomma', 'Lama', 'Lana', 'Lino', 'Lyocell',
                        'Modacrilica', 'Modal', 'Mohair', 'Nylon', 'Pelle', 'Pelo_di_cammello',
                        'Piuma', 'Plastica', 'Poliammide', 'Poliestere', 'Polietilene',
                        'Poliuretano', 'Resina', 'Seta', 'Vetro', 'Viscosa'])


dati=pd.concat([df1, df2, df3,df4])
#Sostituzione degli na con degli zeri (0).

materiali=['Ceramica',
 'Pelle',
 'Nylon',
 'Vetro',
 'Seta',
 'Shearling',
 'Lyocell',
 'Elastan',
 'Fibra_di_metallo',
 'Altre_fibre',
 'Acetato',
 'Canapa',
 'Cupro',
 'Pelo_di_yak',
 'Fibre_sintetiche',
 'Paglia',
 'Poliuretano',
 'Policarbonato',
 'Acrilico',
 'Poliestere',
 'Lino',
 'Modal',
 'Anatra',
 'Triacetato',
 'Polietilene',
 'Cotone',
 'Modacrilica',
 'Fibra_di_asclepiade',
 'Lana',
 'Polistirene',
 'Lama',
 'Piuma',
 'Gomma',
 'Mohair',
 'Resina',
 'Elastodiene',
 'Lattice',
 'Etilenvinilacetato',
 'Fibra_di_acido_polilattico',
 'Polivinilcloruro',
 'Plastica',
 'Poliammide',
 'Elastomultiestere',
 'Pelo_di_cammello',
 'Polipropilene',
 'Cashmere',
 'Alluminio',
 'Carta',
 'Viscosa',
 'Alpaca',
 'Elastolefin']



materiali=list(dict.fromkeys(materiali))    
df=dati[materiali]
df=df.fillna(0) 

df = df.reindex(sorted(df.columns), axis=1)  

df['N_Fibre_Differenti'] = df.sum(axis=1)


senza_materiali= dati.drop(materiali, axis=1)


#Creare una nuova variabile lusso.
#0 dove la marca è HM,Hollister,gillick hicks, EA7,social tourist
senza_materiali["Lusso"]=0
senza_materiali.loc[senza_materiali.Marca.isin([ 'Emporio Armani', 'Giorgio Armani',  'Gucci']),"Lusso"] =1


#Correggere un errore : sesso "donna" è codificato come 0, sesso "uomo" è codificato come 1.
senza_materiali.loc[senza_materiali.Sesso=="Donna","Sesso"] =0
senza_materiali.loc[senza_materiali.Sesso=="Uomo","Sesso"] =1

dati=pd.concat([ senza_materiali,df], axis=1) 
dati=dati.reset_index()




dati.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Vestiti.csv")
