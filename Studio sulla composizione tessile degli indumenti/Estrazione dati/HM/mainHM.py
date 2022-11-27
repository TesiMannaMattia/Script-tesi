"""
Script principale dello scraping al sito HM
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




#%% Importazione funzioni
from estrazione_categorie import * 
from estrazione_sottocategorie import *
from estrazione_articoli import *
from apri_pagina import *
from estrazione_dati import *


#%% Parametri

link_sesso=["https://www2.hm.com/it_it/donna.html","https://www2.hm.com/it_it/uomo.html"]

categorie_da_escludere=['Vedi tutto','Ultime occasioni',
 'Basic',
 'Scarpe',
 'Maglieria'
 'Accessori',
 'Sport',
 'Beauty',
 'Abbigliamento premaman',
 'Plus Size e Taglie Curvy',
 'Premium Selection',
 'Capi e accessori per cani',
 'Prodotti per la cura dei capi',
 'Visualizza tutti']

sottocategorie_da_escludere=["Multipack","Accessori","Intimo Modellante e Pratico"]

#Per evitare di estrarre un articolo già estratto
SESSO=[]                                  #Sesso
                   
MARCA=[]                                  #Marca
                       
NOME=[]                                   #Nome articolo
                   
IDD=[]                                    #id dell'articolo (proprio)

PREZZI=[]                                 #Prezzo dell'articolo
  
SCONTI=[]                                 #Sconti
                 
MATERIALI=[]                              #Materiale articolo
                   
ALTRI_MATERIALI=[]                        #Altre informazioni sui materiali
                   
COLORI=[]                                 #Colori
                   
CATEGORIA=[]                              #Categoria
                   
SOTTO_CATEGORIA=[]                        #Sottocategoria
                   
LINK=[]                                   #Link pagina dell'articolo
                   
ID_ESTRAZIONE=[]                          #ID messo da me. 

ID_articoli_estratti=[]

gruppo_articoli=0



link_gia_estratti=[]
#%% Parametri di controllo
bloccocategorie=True
iterazionicategoria=1

blocco_sotto_categorie=True
iterazioni_sotto_categorie=1

blocco_articolo=True
iterazioni_articolo=1


#Debug
debugger=False
debug=0
ripartenza=264
#%% Funzione


#ITERARE SUL SESSO
for s in range(0,len(link_sesso)):
    #Sesso
    sesso=re.findall(r'[a-zA-Z_]\w*[^/]+',link_sesso[s])
    sesso=re.findall(r'[a-zA-Z_]\w*[^.]+',sesso[3])
    sesso=sesso[0]
    print("Sesso",sesso)
    
    #Definizione link
    link=link_sesso[s]
    
    #Estrazione categorie  e sottocategorie dei prodotti
    categorie_prodotti=estrazione_categorie_prodotti(link)
   
    
   #Escludere le categorie dei prodotti non utili o categorie doppie     
    for w in categorie_da_escludere:
       categorie_prodotti.pop(w.lower(), None)
    
    try:
        categorie_prodotti["giacche e completi"]=categorie_prodotti.pop("giacche e completi")
        
    except:
        b=1 #giusto per l'except
    
    try:
        categorie_prodotti["top"]=categorie_prodotti.pop("top")
    except:
        b=1 #giusto per l'except
#---------------------------------------#---------------------------------------#---------------------------------------          
    #ITERARE SULLE CATEGORIE
    n_categorie=0   #contatore per debug
    for chiave in categorie_prodotti.keys():
        
        
        #If per debug
        if bloccocategorie==True and  iterazionicategoria==n_categorie:
            break 
       
        
        
        sotto_categorie=estrazione_sotto_categorie(categorie_prodotti[chiave]) #Estrazione sotto categorie
        
        for c in sottocategorie_da_escludere:
           sotto_categorie.pop(c.lower(), None)
        
       
        #ITERARE SULLE SOTTO CATEGORIE
        n_sottocategorie =0  #contatore per debug
        for serratura in sotto_categorie.keys():
           
            #If per debug
            if  n_sottocategorie ==  iterazioni_sotto_categorie and blocco_sotto_categorie==True:
                break 
            
            
    
            articoli,link_gia_estratti=estrazione_link_articoli(sotto_categorie[serratura],link_gia_estratti) #Estrazione link articoli
            
            titolo="Articoli C("+str(n_categorie)+"/"+str(len(categorie_prodotti)-1)+") SC("+str(n_sottocategorie)+"/"+str(len(sotto_categorie)-1)+")"
            #ITERARE SUGLI ARTICOLI
            n_articoli= 0   #contatore per debug
            for chiavistello in alive_it(articoli.keys(),title=titolo):
                
                #If per debug
                if n_articoli ==  iterazioni_articolo and blocco_articolo==True:
                    break
                
                #Per debug
                if debug <= ripartenza and debugger==True:
                    debug += 1
                    continue 
                
                nomi, idd, prezzi,sconto,materiali,altri,colorei,ID_articoli_estratti=apri_pagina(articoli[chiavistello],ID_articoli_estratti)
               
                
                #Parte in cui si differenzia la gestione dei colori.
                
                for i in range(0,len(colorei)):
                    
                    SESSO.append(s)                                            #Sesso
                    
                    MARCA.append("H&M")                                        #Marca
                        
                    NOME.append(nomi[i])                                       #Nome articolo
                    
                    IDD.append(idd[i])                                         #id dell'articolo (proprio)

                    PREZZI.append(prezzi[i])                                   #Prezzo dell'articolo
                    
                    SCONTI.append(sconto[i])                                   #Sconti
                    
                    MATERIALI.append(materiali[i])                             #Materiale articolo
                   
                    ALTRI_MATERIALI.append(altri[i])                           #Altre informazioni sui materiali
                    
                
                    COLORI.append(colorei[i])                                  #Colori
                    
                    CATEGORIA.append(chiave)                                   #Categoria
                    
                    SOTTO_CATEGORIA.append(serratura)                          #Sottocategoria
                    
                    LINK.append(articoli[chiavistello])                        #Link pagina dell'articolo
                    
                    ID_ESTRAZIONE.append(gruppo_articoli)                           #ID messo da me. 
                    
                    
                    
                gruppo_articoli += 1 
                n_articoli += 1
            n_sottocategorie += 1 
        n_categorie += 1
    
    

#Creazione dataframe pandas
dataset={"Sesso" :SESSO, "Categoria": CATEGORIA, "Sotto categoria" : SOTTO_CATEGORIA,"Marca": MARCA , "Articolo" : NOME,  "Prezzo" : PREZZI,"Prezzo scontato" :SCONTI ,"Materiali" : MATERIALI, "Colore" : COLORI, "ID" : IDD, "Gruppo" : ID_ESTRAZIONE, "Link" : LINK, "Altro": ALTRI_MATERIALI}

df = pd.DataFrame(dataset)

#Esportazione dati NON puliti in csv
df.to_csv('/Users/mattia/Desktop/id.csv') 
    
    


