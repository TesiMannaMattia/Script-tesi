"""
Funzione per la pulizia dei dati, prende input un dataframe pandas
"""
#%%Importazione pacchetti
#Importazione pacchetti per BeautifulSoup
import re

#Importazione pacchetti per esportare in csv
import pandas as pd  

#Per lavorare con le date
from datetime import date 

#Tempo
import time


#%% Funzione



def puliziadati(df):
    print("Inizio processo di pulizia")

    #Inizializzazione contatore tempo
    tempo_inizio=time.perf_counter()

    #Estrazione materiali
    dati=df["Materiale"]

    #Se False i print verranno inibiti
    parametri_di_controllo=False

    #------------------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------------------------------
    #PULIZIA DEI DATI


    #Inizializzazione dataframe
    dataset = pd.DataFrame({'A' : []})
    #dati=["Nero - 95% cotone, 5% elastan / Bianco - 95% cotone, 5% elastan / Corpo:95% Cotone, 5% Elastan"]

    for i in range(0,len(dati)):
        #Estrazione della stringa su cui lavorare, sarebbe la riga del dataset. 
        stringa=dati[i]
        # print(stringa,i)
        
        #In modo da risolvere gli errori in casi nei quali il materiale è NAN ovvero non c'è.
        if str(stringa).lower() == "nan" or  str(stringa).lower() == "null" or str(stringa).lower() == "na" or str(stringa)=="" or str(stringa)==" ":
            continue
    
        #In modo da risolvere gli errori in casi di tipo :  "78% Cotone, 20% Poliestere, 2% Elastan"
        if stringa[0].isdigit()==True:
            stringa= "Corpo:"+stringa
     
        #Mettere tutto in minuscolo per non avere problemi di CASE SENSITIVE
        stringa=stringa.lower()
    
        #Estrazione delle varie parte dell'articolo :Gommapiuma Imbottitura,Fodera,corpo...
        parti_articolo=re.findall(r'[a-zA-Z_]\w*[^/]+',stringa) 
   
        if parametri_di_controllo==True:#Parametro di controllo e debug
            print("Pulizia della riga numero",i)#Parametro di controllo e debug
            print("STRINGA : ",stringa,) #Parametro di controllo e debug
    
        for j in range(0,len(parti_articolo)):
        
            string=parti_articolo[j]
        
            #Estrarre numeri
            percentuali=re.findall(r'\d+',string)
        
            #Separare titolo parte dagli elementi ed identificarlo:
            titolo=re.findall(r'[a-zA-Z_]\w*[^:]+',string)[0]
        
            #Trovare i materiali
            materiali = re.sub(titolo, "", string)
            materiali=re.findall(r'[a-zA-Z_]\w*[^,]+',materiali)
        
            for k in range(0,len(materiali)):
                materiali[k]=materiali[k].strip()
        
        
        
            #-----#
            #Parametri di controllo
            if parametri_di_controllo==True:#Parametro di controllo e debug
                print("Percentuali:",percentuali) #Parametro di controllo e debug
        
            if parametri_di_controllo==True:#Parametro di controllo e debug
                print("Titolo: ",titolo) 
        
            if parametri_di_controllo==True:
                print("Materiali:",materiali) ##Parametro di controllo e debug
            #-----#
            
            try:
                #NUOVO METODO
                if titolo=="corpo":
                    #Aggiungere al dataframe
                
                    riga= pd.DataFrame([percentuali], columns=materiali)
                    dataset=pd.concat([dataset, riga])
        
            except:
                continue 
        
            if parametri_di_controllo==True:    
                print("\n\n")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                #------------------------------------------------------------------------------------------------------------------------------------------------            
                #AGGIUSTAMENTO DEL DATASET
 
    #Rimozione colonna inutile
    dataset.drop(["A"], inplace=True, axis=1)

    #Aggiustamento indici
    dataset=dataset.reset_index()

    #ORDINARE IL DATASET PER COLONNA :
    #Grazie a   BrenBarn  gcamargo link : https://stackoverflow.com/questions/11067027/sorting-columns-in-pandas-dataframe-based-on-column-name
    dataset = dataset.reindex(sorted(dataset.columns), axis=1)  

    #Aggiunta del nuovo dataset al vecchio.
    dati=pd.concat([df, dataset], axis=1)

    #Rimozione delle colonne non più utili
    colonne_da_rimuovere=["index","Materiale",]
    dati.drop(colonne_da_rimuovere, inplace=True, axis=1)

    #Rimuovere tutti gli NaN e metterci degli zeri, https://www.geeksforgeeks.org/replace-nan-values-with-zeros-in-pandas-dataframe/
    dati.fillna(0)

    #Data
    today = date.today()
    today= today.strftime("%d %b, %Y")


    #Calcolo tempo di esecuzione
    tempo_fine=time.perf_counter()
    tempo_esecuzione=int(tempo_fine - tempo_inizio)
    
    path="/Users/mattia/desktop/scraping Hollister/R/Dati/dati_sporchi1000.csv"
    print("Sono stati pulite",len(dati.index),"righe  in",tempo_esecuzione,"secondi.","\nPoi importate nel file", path,"\nFine del processo di pulizia .") 
    
    
    return dati 