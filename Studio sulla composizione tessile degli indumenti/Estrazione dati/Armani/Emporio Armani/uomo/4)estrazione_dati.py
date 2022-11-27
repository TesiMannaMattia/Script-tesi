"""
Estrazione dati articoli da uomo da EMPORIO  ARMANI
"""
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
from tqdm import tqdm as tqdm
import math
import json
import ast


# Impostazione headers
headers={
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
,'accept-encoding': 'gzip, deflate, br',
'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'max-age=0',
'content-length': '128',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://labels.fda.gov',
'referer': 'https://labels.fda.gov/ingredientName.cfm',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}


post_params={'searchfield_required':'Please enter at least 3 characters in the Active Ingredient field.',
             'searchfield': 'fentanyl','submit': 'Submit Query'}




df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Emporio Armani/Uomo/LINK:HTML/link_articoli.csv")
df = df.drop('Unnamed: 0', axis=1)

dati=[]


for i,row in alive_it(df.iterrows(),title="Estrazione dati"):
    
    errori={}
    errore=[]
    #Richiesta http protocol
    response=requests.post(row.Link,data=post_params,headers=headers)

   
    #Ottenere html corretto
    d=BeautifulSoup(response.text,'html.parser')
    
    
    # Estrazione dati 
    ## Composizione
    try:
        composizione=d.find("div",{"class":"item-shop-panel__details"})
        composizione=composizione.find("p")
        composizione=composizione.text.strip()
    except:
        composizione="Null"
        errore.append("Composizione")
    
    
    
    
  
    ## Prezzo  
    try:
        classe=d.find("div",{"class":"itemPrice"})
        prezzo=classe.find("span",{"class":"value"}).text.strip().replace("\n","")
    
    except:
        prezzo="Null"
        errore.append("Prezzo")
    
    ## Valuta
    try:
        classe=d.find("div",{"class":"itemPrice"})
        valuta=classe.find("span",{"class":"currency"}).text.strip().replace("\n","")
    
    except:
        valuta="Null"
        errore.append("Valuta")   
    
    
    
    
    ## Codice prodotto
    try:
        codice=d.find("div",{"class":"item-shop-panel__modelfabricolor"})
        codice=codice.find("p",{"class":"attributes mfPartNumber"})
        codice=codice.find("span",{"class":"value"}).text.strip().replace("\n","")
        
    
    except:
        codice="Null"
        errore.append("codice")   
    
    
    #Colore
    try:
        colore=d.find("div",{"class":"item-shop-panel__color-selector"})
        colore=colore.find("ul")
        colore=colore.find("li",{"class":"is-selected"})
        colore=colore.find("div",{"class":"inner"}).find("label").find("span",{"class":"colorText"}).text.strip()
        
    except:
        colore="Null"
        errore.append("Colore")   
        
    # Nome articolo
    try:
        nome=d.find("span",{"class":"modelName modelName"}).text.strip()
    except:
        nome="Null"
        errore.append("Nome")   
        
    #Marca
    try:
        marca=d.find("div",{"class":"item-shop-panel__topbar"}).find("p").text.strip()
    except:
        marca="Null"
        errore.append("Marca") 
        
        
    
    diz={"Sesso":"Uomo","Categoria":row["Categoria"],"Sotto_categoria":row["Sotto_categoria"],"Marca":marca,"Articolo":nome,"Prezzo":prezzo,"Valuta":valuta,"Materiali":composizione,"Colore":colore,"Codice_prodotto":codice,"Link":row["Link"]}
    dati.append(diz)
    
    
    #Wait
    time.sleep(1)
    
    
    errore.append(row.Link)
    errori[str(i)]=errore
    
    with open("/Users/mattia/Desktop/HTML/html_"+str(i)+".txt","w+") as f :
        f.write(str(d))
    
    with open("/Users/mattia/Desktop/Errori/errori.txt","a") as f :
        f.write(str(errori))
        f.write("\n")





#Creazione dataset
dff = pd.DataFrame(dati)

dff.to_csv("/Users/mattia/Desktop/emporio_armani_data.csv") 

#Esportazione dati NON puliti in csv
#dff.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Emporio Armani/Uomo/Dataset/armani_data.csv") 








