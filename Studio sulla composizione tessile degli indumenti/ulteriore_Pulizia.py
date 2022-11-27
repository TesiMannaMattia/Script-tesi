import pandas as pd
import re
import numpy as np
from tqdm import tqdm
#df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati di prima modifica (NON MODIFICARE)/Vestiti_rivisto.csv",
 #              delimiter=";",usecols=['Sesso', 'Categoria', 'Sotto_categoria', 'Marca',
  #                    'Articolo', 'Prezzo', 'Materiali', 'Colore','Link' ,'Lusso',])
df=pd.read_csv('/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Vestiti.csv',
             usecols=['Sesso', 'Categoria', 'Sotto_categoria', 'Marca',
                      'Articolo', 'Prezzo', 'Materiali', 'Colore', 'Link','Lusso'])

m=df["Materiali"]

"""## Pulizia effettiva"""



non_materiali=["Silver_pink","Moonlight_jade","Light_blue","Iron_gate","Bianco","Moldavia","Tramonto_d","Sud_africa","Spagna","Perla_fum","Italia","Imbottitura","Moldavia"]


dataset = pd.DataFrame({'A' : []})
for i in tqdm(range(0,len(m))):
  if m[i]=="Null":
    #print("Eliminato")
    df=df.drop(i) #eliminare le righe che non hanno materiale
    continue 
  m[i]= m[i].replace("Composizione","")
  k=re.sub("[a-zA-Z\s]*:","",m[i]) #Restituisce solo i materiali con la corrispettiva percentuale
  #n=re.sub("[0-9%]*","",k)
  ma=re.findall(r"[a-zA-Z \s]{2,}",k)



  rimuovere=[]
  for j in range(0,len(ma)):
    ma[j]=ma[j].strip().capitalize()  #toglie spazi iniziali e finali e mette prima lettera maiuscola e resto tutto minuscolo
    ma[j]=re.sub("[\s]","_",ma[j])    #Se una parola è doppia toglie lo spazio ed unisce con un trattino le due parole
    
    
    
    
    if ma[j]=="Poliestere_e" or  ma[j]=="Poliestere_riciclato" or ma[j]=="Fibre_di_poliestere_riciclato":
        ma[j]="Poliestere"
    
    elif ma[j]=="Cotone_biologico" or  ma[j]=="Cotton" or ma[j]=="Cotone_e":
        ma[j]="Cotone"
    
    elif ma[j]=="Lama" or  ma[j]=="Lana_e"  or ma[j]=="Alpaca" or  ma[j]=="Lana_riciclata" or  ma[j]=="Lana_di_yak" or ma[j]=="Yak_wool" or  ma[j]=="Wool" or  ma[j]=="Virgin_wool" or ma[j]=="Mohair_wool"or ma[j]=="Lana_di_alpaca" or ma[j]=="Lana_di_angora" or ma[j]=="Lana_mohair" or ma[j]=="Lana_rigenerata" or  ma[j]=="Lana_vergine" or	ma[j]=="Lana_merinos" or ma[j]=="Angora_wool" or ma[j]=="Alpaca_wool" or ma[j]=="Camel_wool" or ma[j]=="Lana_merinos":
        ma[j]="Lana"
 
    elif ma[j]=="Copoliestere" or ma[j]=="Polyester":
        
        ma[j]="Poliestere"
    
    elif ma[j]=="Poliuretano_termoplastico":
        ma[j]="Poliuretano"
        
    elif ma[j]=="Modacrilico" or ma[j]=="Modacrylic":
        ma[j]="Modacrilica"
    
    elif ma[j]=="Nylon_e":
        ma[j]="Nylon"
        
    
    
    elif ma[j]=="Rayon" or ma[j]=="Viscose" or ma[j]=="Modal":
        ma[j]="Viscosa"
    
    elif ma[j]=="Cachemire" or ma[j]=="Goat_hair":
        ma[j]="Cashmere"
      
    elif ma[j]=="Polyamide" or  ma[j]=="Polyimide":
        ma[j]="Poliammide"
      
    elif ma[j]=="Acrylic" or ma[j]=="Acrilica"  :
        ma[j]="Acrilico"
        
    elif  ma[j]=="Acetate" :
        ma[j]="Acetato"
    
    elif ma[j]=="Carta_tessile":
        ma[j]="Carta"
        
    elif ma[j]=="Mohair_e":
        ma[j]="Mohair"
        
    elif ma[j]=="Modal_e":
        ma[j]="Modal"
        
        
      
    elif ma[j]=="Seta_di_gelso" or ma[j]=="Seta_tussah" or ma[j]=="Silk" or ma[j]=="Fodera_in_seta_bordeaux":
        ma[j]="Seta"
 
    elif ma[j]=="Elastane":
        ma[j]="Elastan"
      
    elif ma[j]=="Elastomultiester":
        ma[j]="Elastomultiestere"
      
    elif ma[j]=="Mucca" or  ma[j]=="Pelle_di_capra" or  ma[j]=="Pelle_di_vitello" or  ma[j]=="Pelle_bovina" or ma[j]=="Cuoio" or ma[j]=="Calf" or  ma[j]=="Bovine_leather" or  ma[j]=="Goat_skin"or ma[j]=="Skin_leather" or ma[j]=="Lambskin" or ma[j]=="Pelle_di_agnello" or ma[j]=="Pelle_di_bovino":
        ma[j]="Pelle"
     
    elif ma[j]=="Linen":
        ma[j]="Lino"
        
    elif ma[j]=="Metallic_fibre" or ma[j]=="Metallica" or  ma[j]=="Fibra_metallizzata"  or ma[j]=="Metallo":
        ma[j]="Fibra_di_metallo"
    elif ma[j]=="Anatra" or ma[j]=="Piuma_d" or ma[j]=="Piumino_d" or ma[j]=="Oca" or ma[j]=="Piumino":
        ma[j]="Piuma"
        
    elif ma[j]=="Pvc":
        ma[j]="Polivinilcloruro"
    elif ma[j]=="poliuretano" or ma[j]=="Poliuretanica" or  ma[j]=="Polyurethane" or ma[j]=="Polyurethane_coated":
        ma[j]="Poliuretano"
    
    elif ma[j]=="Triacetate":
        ma[j]="Triacetato"
        
    elif ma[j]=="Other_fibres" or ma[j]=="Fibre_non_specificate" or ma[j]=="Fibre_sintetiche" or ma[j]=="Fibre":
        ma[j]="Altre_fibre"
        
    elif ma[j] in non_materiali:
       rimuovere.append(ma[j])

  ma=set(ma)
  ma=ma.difference(set(rimuovere))  

      
  ma = list(dict.fromkeys(ma))        #Rimozione di eventuali materiali che compaiono più volte in diverse classi.

  vettore_uni=np.ones(len(ma))        #Vettori di uno per i materiali presenti 
  
  vettore_uni.astype(int)             #Togliere decimali dagli uno, nota: non sembra funzionare.
  
  riga= pd.DataFrame([vettore_uni], columns=ma)        #Crea la riga 
  
  dataset=pd.concat([dataset, riga])   

################## ################### ################### ################### ################### 
df=df.reset_index(drop=True)    #si devono rimettere gli indici perchè alcune righe che presentano colori ambigui verranno eliminate
#LAVORARE SUL DATASET PANDAS CREATO

#Sostituzione degli na con degli zeri (0).
dataset=dataset.fillna(0) 

#Rimozione colonna inutile
dataset.drop(["A"], inplace=True, axis=1)

#Aggiustamento indici
dataset=dataset.reset_index()

#ORDINARE IL DATASET PER COLONNA :
dataset = dataset.reindex(sorted(dataset.columns), axis=1)  

#Creazione della colonna che fornisce il numero di fibre presenti nel vestito.
dataset['N_Fibre_Differenti'] = dataset.sum(axis=1)
dataset.N_Fibre_Differenti.astype(int)



#Rimozione colonna inutile
dataset.drop(["index"], inplace=True, axis=1)
dati=pd.concat([df, dataset], axis=1) #non ha senso farlo perchè il dataset in input non è corretto

#Rimozione colonna inutile
try:
    dati.drop(["Unnamed: 0","...1"], inplace=True, axis=1)
except:
    pass
try:
    dati.drop(["level_0"], inplace=True, axis=1)
except:
    pass

dati.to_csv('/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Vestiti.csv')
#dati.to_csv('/Users/mattia/desktop/Vestiti.csv')
