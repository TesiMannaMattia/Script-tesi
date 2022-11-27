import pandas as pd
import os
import re
datasets_list=os.listdir("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/scraping ARMANI/Dataset")


df=pd.DataFrame(columns=['Unnamed: 0', 'Sesso', 'Categoria', 'Sotto_categoria', 'Marca','Articolo', 'Prezzo', 'Valuta', 'Materiali', 'Colore', 'Codice_prodotto', 'Link'])


for i in range(0,len(datasets_list)):
    if datasets_list[i][len(datasets_list[i])-3:len(datasets_list[i])]=="csv":
        df=pd.concat([df,pd.read_csv("/Users/mattia/Desktop/Dataset/"+datasets_list[i])])



try:      
    df = df.drop('Unnamed: 0', axis=1)
except:
    pass

try:
    df = df.drop('Unnamed: 0.1', axis=1)
except:
    pass

try:
    df = df.drop('index', axis=1)
except:
    pass


df=df.reset_index(drop=True) #per risolvere il problema degli indici che non venivano resettati, in questo modo li elimina direttamente

df.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati grezzi (NON TOCCARE!)/ARMANI.csv")