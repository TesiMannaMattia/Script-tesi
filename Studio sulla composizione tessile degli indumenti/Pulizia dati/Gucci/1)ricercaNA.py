import pandas as pd
import re

#df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati da lavoro/gucci2.csv",delimiter=";")
#df=df.drop_duplicates(keep='last')
#df.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati da lavoro/gucci3.csv")


df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati di prima modifica (NON MODIFICARE)/gucci_rivisto.csv",
               delimiter=";")




try:      
    df = df.drop('Unnamed: 0', axis=1)
except:
    pass

try:
    df = df.drop('Unnamed: 0.1', axis=1)
except:
    pass
try:
    df = df.drop('Valuta', axis=1)
except:
    pass


#Primo for per identificare le righe con gli NA.
#Una volta identificati gli NA si andranno a ricercare singolarmente.


#Analisi duplicati:
#doppi=df.loc[df.duplicated(subset=['Codice_prodotto'],keep=False), :]
#doppi.to_csv("/Users/mattia/desktop/solo_doppi.csv")

#doppi1=df.drop_duplicates(keep='last')
#oppi1.to_csv("/Users/mattia/desktop/no_doppi.csv")


n_errori =0

for i,row in df.iterrows():
    
    errore=[]
    for j in range(0,len(row)):
        errore_presente=False
        
        try:
            if str(row[j]).lower()=="null" or  str(row[j]).lower()=="nan" or str(row[j]).lower()=="na":
                errore.append(i)
                errore.append(j)
                errore.append(row["Link"])
                errore_presente=True
                n_errori += 1
                break
        except:
            errore.append(i)
            errore.append("except")
            errore.append(row["Link"])
            errore_presente=True
            n_errori += 1
            break
            
    if errore_presente==True:
        with open("/Users/mattia/Desktop/NA_gucci.txt", "a+") as f:
            f.write(str(errore))
            f.write("\n\n\n\n")


if n_errori > 0:
    with open("/Users/mattia/Desktop/NA_gucci.txt", "r+") as f: 
        file = f.read() 
        f.seek(0, 0) 
        f.write("Numero totale di errori : "+str(n_errori)+"\n"+file) 
           
                
            
#Successivamente ho analizzato uno per uno gli n errori.
#Si è andato quindi link per link per accertare l'entità dell'errore.
#E si è modificato manualmente il dataset sull'applicazione apple : Numbers.
#Da numbers si esporta di nuovo il dataset modificato e si controlla nuovamente per eventuali errori.
#Facendo bene attenzione a specificare il delimiter ";"

    
       
    

