"""
Estrazione articoli da donna da GIORGIO ARMANI
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




df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Giorgio Armani/Donna/LINK:HTML/link_sottocategorie.csv")
df = df.drop('Unnamed: 0', axis=1)


new_data=pd.DataFrame(columns=["Categoria","Sotto_categoria","Link",])

for i,row in alive_it(df.iterrows(),title="Estrazione articoli"):
    try:
        #Richiesta http protocol
        response=requests.post(row.Link,data=post_params,headers=headers)
      #  print(response,end=" Nuovo sito :")
          
       
        #Ottenere html corretto
        soup=BeautifulSoup(response.text,'html.parser')
    
        #Estrazione numero di articoli, è necessario per modificare il link ed ottenere una pagina con tutti gli articoli
        numero_articoli=soup.find("div",{"class":"plp-header__category"})   
        numero_articoli=numero_articoli.find("div",{"class":"totalResults"}).find("span").text.strip()
    
        #Nuovo link:
        pezzilink=re.findall(r"([\w\W]+&productsPerPage=)([\d]+)([\w\W]+)",row.Link)[0] #tramite regex si estraggono le parti del link e si raggruppano per richiamarle in seguito
        nuovo_link=pezzilink[0]+numero_articoli+pezzilink[2]
        
    
        #Nuova richiesta http protocol
        response=requests.post(nuovo_link,data=post_params,headers=headers)
        
        #Ottenere html corretto
        soup=BeautifulSoup(response.text,'html.parser')
       # print(response)
        
        
        catalogo_prodotti=soup.find("section",{"class": "search"})
        prodotti=catalogo_prodotti.find_all("a",{"class":"item-card__link"})
        
        for i in range(0,len(prodotti)):
            link=prodotti[i].get("href")
            
            df_provvisorio=pd.DataFrame({"Categoria":[row["Categoria"]],"Sotto_categoria":[row["Sotto_categoria"]],"Link":[link]})
            new_data=pd.concat([new_data,df_provvisorio])
    except:
        pass
    
        
new_data.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Giorgio Armani/Donna/LINK:HTML/link_articoli.csv")









