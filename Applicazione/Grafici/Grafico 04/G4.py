import pandas as pd
from alive_progress import alive_bar
from alive_progress.styles import showtime
from alive_progress import alive_it


# Importare dataset
df = pd.read_csv(r'/Users/mattia/desktop/dati/Grafico 3/dati_xG3.csv') #dataset completo

materiali = pd.read_csv(r'/Users/mattia/desktop/dati/Grafico 3/materiali.csv')#dataset con soli materiali


# Preparazione dataset
materiali.drop(['Unnamed: 0'],inplace=True,axis=1)


# Creazione nuova variabile :

lista=[]

for i in alive_it(range(0,len(materiali)),title="Accorpamento binarie"): #iterare su righe
    for name in materiali.columns: #iterare su colonne 
        if materiali[name][i] == 1:  #se si trova la binaria giusta...
            lista.append(str(name))
            break


df=df.assign(Materiale=lista)
df.to_csv("/Users/mattia/desktop/Singolo_materiale.csv")
  






#Merge data
