"""
In questo script si estraggono i link delle categorie da donna da GIORGIO ARMANI
Una volta estratte vengono allocate in un csv
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






url="https://www.armani.com/it-it/giorgio-armani/donna/abbigliamento"

#Richiesta http protocol
response=requests.post(url,data=post_params,headers=headers)





#Ottenere html corretto
soup=BeautifulSoup(response.text,'html.parser')


#Prendere il macro elemento
pezzi=soup.find("div",{"class":"search__wrapper"})
pezzi=pezzi.find("plp-refinements",{"class":"plp-refinements anim-hidden hidden"})
pezzi=pezzi.find("div",{"class":"refinements"})

#Accedere ai filtri
pezzi=pezzi.find("ul")


#Accesso alle categorie
categorie=pezzi.find("li",{"class":"refinement refinement--category_1"})

#Accesso ai value delle categorie
categorie=categorie.find("div",{"class":"refinement__content anim-hidden hidden"})
categorie=categorie.find("ul")
categorie=categorie.find_all("li")


#inizializzazione dizionario, in questo dizionario saranno messi i nomi di categoria ed il corrispettivo link
link_categorie=[]
nome_categorie=[]
semi_link=[]
for i in alive_it(range(len(categorie)),title="Estrazione Categorie"):
    
    #Estrarre nome della categoria
    testo=categorie[i].find("label").find("span").text.strip()
    nome_categorie.append(testo)
    
    #Estrarre caratteristiche della categorie
    A=categorie[i].get("data-ytos-facet")
    dizionario = json.loads(A)  #convertire una stringa in un dizionario
 
    
    #Estrarre il link della categoria
    new_link="""https://www.armani.com/it-it/giorgio-armani/donna/abbigliamento/?department=EU_GA_M_Clothing&departmentId=3074457345616677883&facetsvalue="""+dizionario["value"].strip()+"""&itemsToLoadOnNextPage=36&lazyLoadStart=4&linkdepartment=EU_GA_M_Clothing&linkdepartmentId=3074457345616677883&page=1&partialLoadedItems=36&productsPerPage=36&rsiUsed=false&suggestion=false&totalItems=728&totalPages=21&ytosQuery=true"""
    link_categorie.append(new_link)
   
    semi_link.append(dizionario["value"].strip())
   

df=pd.DataFrame({"Categoria" :nome_categorie,"Link":link_categorie,"SemiLink":semi_link})

df.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Giorgio Armani/Donna/LINK:HTML/link_categorie.csv")

