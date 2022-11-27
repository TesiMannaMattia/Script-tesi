#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraping Gucci
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





link="https://www.gucci.com/it/it/ca/men/ready-to-wear-for-men-c-men-readytowear"

options = Options()
options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
options.add_experimental_option("prefs", prefs)    
driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)

driver.get(link)
h=driver.page_source  
driver.quit()


#Ottenere html corretto
soup=BeautifulSoup(h,'html.parser')


categorie=soup.find("div",{"class":"filter-bar-container"})

categorie=categorie.find("nav",{"class":"filter-nav"}).find("ul").find("li",{"class":"filter-dropdown filter-category-expander"}).find("ul")

with open("/Users/mattia/Desktop/html.txt","w+") as f:
    f.write(str(categorie))




categorie=categorie.find_all("li")


link_categorie=[]
nome_categorie=[]
for i in range(1,len(categorie)):
    link="https://www.gucci.com/"+categorie[i].find("a").get("href")
    link_categorie.append(link)
    
    
    nome_categoria=categorie[i].find("a").text.strip()
    nome_categoria=re.sub(r"Uomo","",nome_categoria)
    nome_categoria=re.sub(r"[\d()]*","",nome_categoria).strip()
    
    
    nome_categorie.append(nome_categoria)



#   https://www.gucci.com/it/it/ca/men/ready-to-wear-for-men/knitwear-for-men-c-men-readytowear-sweaters-cardigans
  
df=pd.DataFrame({"Categoria" :nome_categorie,"Link":link_categorie})
print(df)
df.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Scraping Gucci/1) Estrazione dati/Uomo/LINK:HTML/link_categorie.csv")













