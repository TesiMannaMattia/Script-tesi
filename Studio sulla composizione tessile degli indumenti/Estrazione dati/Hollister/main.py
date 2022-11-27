"""
Script principale dello scraping al sito hollister, link  : https://www.hollisterco.com/shop/eu-it
"""

#%%Importazione pacchetti

#Importazione pacchetti per selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager


#Per aprire cartelle
import os
import wget


#Importazione pacchetti per BeautifulSoup
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Importazione pacchetti per esportare in csv
import pandas as pd  

#Per lavorare con le date
from datetime import date 

#Per fare i contatori tempi
import time 
from time import sleep

#Pacchetto alive, permette di creare barre di progresso
from alive_progress import alive_bar
from alive_progress.styles import showtime
from alive_progress import alive_it
#from tqdm import tqdm as tqdm









#%% Parametri, headers BeautifulSoup
headers={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
,'accept-encoding': 'gzip, deflate, br',
'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'max-age=0',
'content-length': '128',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://labels.fda.gov',
'referer': 'https://labels.fda.gov/ingredientName.cfm',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Safari/537.36'}
post_params={'searchfield_required':'Please enter at least 3 characters in the Active Ingredient field.',
             'searchfield': 'fentanyl','submit': 'Submit Query'}











#%% Importazione funzioni
from estrazioneprodotti import *
from estrazionearticoli import *
from estrazionedati import *
#from puliziadati import *
from cambiopagina import *
from estrazione_sottocategorie import *

#%% Inizializzazione elementi e parametri

#Inizializzazione contatore tempo
tempo_inizio=time.perf_counter()

#Link delle pagine
link_sesso=["https://www.hollisterco.com/shop/eu-it/donna","https://www.hollisterco.com/shop/eu-it/uomo"]


#Data
today = date.today()
today= today.strftime("%d/%m/%Y")


#Metodo naive per la creazione di un dataset.
contaarticoli=0
ID= 1195  #funge anche da id_articolo, è una cosa mia non di hollister.
#Questo ID è stato messo per ritrovare subito in fase di elaborazione dati gli articoli uguali.
#Questa scelta è stata necessaria perchè il dataset è stato creato in modo da sdoppiare gli articoli con più colori, quindi un articolo
#che ha 3 colori viene inserito tre volte, ogni riga con un colore.
sesso=[]

Marca=[]
tipologiaprodotto=[]
tipo=[]
nomearticolo=[]

Sconto=[]
Prezzo=[]
id_articolo=[]
pagina=[]

colore=[]
materiale=[]

giorno=[]
categorie_da_escludere=['Nuovi arrivi', 'Accessori e Scarpe', 'Acqua di colonia & Cura del corpo', 'Profumi & Cura del corpo']

#%% Parametri driver
#options = Options()
#options.headless = True
#options.add_argument("--window-size=1440,7648")
#options.add_argument("--window-size=1920,1080")
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")
#options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
#prefs = {"profile.managed_default_content_settings.images": 2}
#options.add_experimental_option("prefs", prefs)




#%% Principale


#PARAMETRI DEBUGGING e PROVE

#stopperrrr="Sergio Brio"
#stopperrrr="Brio goal"


#Permettono di decidere il numero di articoli da estrarre per ogni categoria
attivare_debug=True
solo_tot_articoli= 1 #articoli per categoria

#Permette di estrarre solo le prime n categorie da uomo e donna
meno_categorie=True
ncategorie_debug=1

#Permette di estrarre solo prime n sottocategorie da uomo e donna
meno_SOTTOcategorie=True
nSOTTOcategorie=1

#Primo ciclo itera su UOMO - DONNA
for s in range(1,len(link_sesso)):
    lista_controllo_link=[]
    #crea il dizionario dei prodotti 
    tipologia_categorie=estrazione_tipo_prodotti(link_sesso[s]) 
    
    #Elimina dallo scraping determinate categorie
    for w in categorie_da_escludere:
        tipologia_categorie.pop(w, None)
        
    try:
       tipologia_categorie['Abbigliamento Notte e Capi per il Tempo Libero']=tipologia_categorie.pop('Abbigliamento Notte e Capi per il Tempo Libero')
        
    except:
        b=1 #giusto per l'except
        
    #print(tipologia_categorie)
    #----------------------------------------------------#
    #Secondo ciclo for itera sulla tipologia dei prodotti
    contatore_categorie=0   #Solo per fare dei print di controllo ed estetici
    
    for chiave in tipologia_categorie.keys():
        if chiave =="Topwear":
            continue 
        

        #PER DEBUGGIN E RUN di PROVA
        if contatore_categorie == ncategorie_debug and meno_categorie==True :
            break 
        
        #Estrazione dei nomi e dei link delle sottocategorie
        nomi_sottocategorie,link_sottocategorie=estrazione_sottocategorie(tipologia_categorie[chiave],chiave)

        conta_sottocategorie=0
        for j in range(0,len(link_sottocategorie)):
            
         
            
            
            if nSOTTOcategorie ==conta_sottocategorie and  meno_SOTTOcategorie==True:
                break
            
            #Estrarre il link di una singola sottocategoria 
            link_SOTTOCATEGORIA=link_sottocategorie[j] 

            #Prendere tutti gli html delle eventuali n pagine della sottocategoria
            listahtml=cambia_pagina(link_SOTTOCATEGORIA) 
            
            #Ottenere tutti i link delle pagine una sottocategoria 
            articoli=estrazione_articoli(listahtml) 
            
            #-------------------------------------------------------------------#
            #Quarto ciclo entrare nei singoli articoli e prenderne le informazioni
        
            debug_articoli=0
            
            titolo=str(link_sesso[s][39:])+": Articolo di tipo " +str(nomi_sottocategorie[j])+" ("+str(j)+"/"+str(len(link_sottocategorie))+")  categoria "+str(chiave)+" ("+str(contatore_categorie)+"/"+str(len(tipologia_categorie))+")\n"
            
            for nome_articolo in alive_it(articoli.keys(),title=titolo) :
            
                #PARAMETRO DI CONTROLLO E DEBUGGING
            
                if solo_tot_articoli == debug_articoli and attivare_debug==True:
                    break

                if articoli[nome_articolo] in lista_controllo_link:
                    print("Articolo skippato perchè già estratto, link articolo: ",  articoli[nome_articolo])
                    #ID += 1 
                    #debug_articoli += 1 
                    continue 
                
            
                materiale_articolo,colore_articolo,lista_controllo_link,marca,prezzo,sconto,titolii=estrazione_dati(articoli[nome_articolo],lista_controllo_link)  
                
             
                
                
                #Parte in cui si differenzia la gestione dei colori.
                if  len(colore_articolo) > 1:
                    try:
                        for i in range(0,len(colore_articolo)):
                            Prezzo.append(prezzo[i])                     #Prezzo
                        
                            sesso.append(s)                              #Aggiunta : Uomo, donna.
                        
                            colore.append(colore_articolo[i].upper())    #Aggiunta colore
                        
                            tipologiaprodotto.append(chiave)             #Aggiunta Tipologia prodotto
                    
                            Marca.append(marca)                          #Marca       
                    
                            Sconto.append(sconto[i])                     #Sconto
                    
                            tipo.append(nomi_sottocategorie[j])          #Sottocategoria
                    
                            nomearticolo.append(titolii[i])              #Aggiunta nome articolo
                        
                            materiale.append(materiale_articolo[i])      #Aggiunta materiale dell'articolo
                        
                            giorno.append(today)                         #Aggiunta data di estrazione dell'articolo
                        
                            id_articolo.append(ID)                       #Aggiunta id dell'articolo
                        
                            pagina.append(articoli[nome_articolo])       #Aggiunta link della pagina contenente l'articolo
                    except:

                        mmmm=1
                
                try:    
                    if  len(colore_articolo) <= 1:
                        #Aggiunta alle liste per lo stoccaggio dei dati
                        Prezzo.append(prezzo[0])                   #Prezzo
                    
                        sesso.append(s)                            #Aggiunta : Uomo, donna.
                    
                        colore.append(colore_articolo[0].upper())  #Aggiunta colore
                    
                        tipologiaprodotto.append(chiave)           #Aggiunta Tipologia prodotto
                    
                        Marca.append(marca)                        #Marca
                    
                        Sconto.append(sconto[0])                   #Sconto
                    
                        tipo.append(nomi_sottocategorie[j])        #Sottocategoria
                    
                        nomearticolo.append(titolii[0])            #Aggiunta nome articolo
                    
                        materiale.append(materiale_articolo[0])    #Aggiunta materiale dell'articolo
                    
                        giorno.append(today)                       #Aggiunta data di estrazione dell'articolo
                    
                        id_articolo.append(ID)                     #Aggiunta id dell'articolo
                    
                        pagina.append(articoli[nome_articolo])     #Aggiunta link della pagina contenente l'articolo
                    
                except:
                    mmmm=1
                ID += 1 
                debug_articoli += 1    #Per DEBUG
                contaarticoli +=1 
            conta_sottocategorie += 1
        contatore_categorie += 1   #Solo per fare dei print di controllo ed estetici



#Chiudere GoogleChrome       
#driver.quit()

#%% Creazione dataset NON pulito
#Creazione dataframe pandas
datasetprova={"Sesso" : sesso, "Categoria" : tipologiaprodotto,"Tipo" : tipo,"Marca": Marca,"Articolo": nomearticolo,"Prezzo" : Prezzo,"Prezzo_scontato": Sconto ,"Materiale" : materiale, "Colore" :colore,"ID_articolo" : id_articolo ,"Giorno_estrazione" : giorno,"Link" : pagina}
df = pd.DataFrame(datasetprova)

#Esportazione dati NON puliti in csv
df.to_csv('/Users/mattia/Desktop/datiHollister_UOMO.csv') 

#%% Tempi di esecuzione
#Calcolo del tempo di esecuzione
tempo_fine=time.perf_counter()
tempo_esecuzione=int(tempo_fine - tempo_inizio)
minuti=tempo_esecuzione/60
ore=minuti/60
ore=round(ore,1)
print("\n\n\n")

#Conti in secondi, utilizzato quando si fanno dei test con poche iterazioni.
#print("Sono stati estratti",contatore,"articoli  in",tempo_esecuzione,"secondi","\nFine del processo.")

#Conti in ore
print("Sono stati estratti "+str(contaarticoli )+" articoli  diversi   per un totale di righe  "+str(len(df. index))+" nel dataset.\n") #Tutto questo in  "+str(ore)+" ore")#,".\nIl numero di articoli e quello delle righe non  per forza devono corrispondere, questo perchè  un articolo con  x colori viene inserito  x volte nel dataset.\n\nFine del processo di estrazione .\n")


#%% Pulizia dati
#dati=puliziadati(df)

#%% Esportazione dati
#dati.to_csv('/Users/mattia/Desktop//989puliti.csv') 









