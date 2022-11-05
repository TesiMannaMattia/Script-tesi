import pandas as pd
from alive_progress import alive_bar
from alive_progress.styles import showtime
from alive_progress import alive_it


# Importare dataset
df = pd.read_csv(r'/Users/mattia/desktop/dati/Grafico 5/dati.csv') #dataset completo

materiali = pd.read_csv(r'/Users/mattia/desktop/dati/Grafico 5/materiali.csv')#dataset con soli materiali


# Preparazione dataset
df.drop(['Unnamed: 0'],inplace=True,axis=1)
materiali.drop(['Unnamed: 0'],inplace=True,axis=1)



lista=[]

for i in alive_it(range(0,len(materiali)),title="Coppie"): #iterare su righe
    c=0
    stringa=""
    for name in materiali.columns: #iterare su colonne 
        if materiali[name][i] == 1:  #se si trova la binaria giusta...
            stringa =stringa +" "+ str(name)
            c +=1
        if c  == 2:
            stringa=stringa.strip()
            stringa=stringa.replace(" ","/")
            lista.append(stringa)
            break

df=df.assign(Coppie=lista)
df.to_csv("/Users/mattia/desktop/dati/Grafico 5/Coppie_fibre.csv")

