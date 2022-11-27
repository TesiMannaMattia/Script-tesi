#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estrazione link categorie
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
import re
options = Options()
options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
options.add_experimental_option("prefs", prefs)    
driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)


df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Scraping Gucci/1) Estrazione dati/Donna/LINK:HTML/link_categorie.csv")
df = df.drop('Unnamed: 0', axis=1)



for i,row in alive_it(df.iterrows(),title="progresso"):

    driver.get(row["Link"])
    h=driver.page_source  
    
    
    with open("/Users/mattia/Desktop/HTML Gucci/Sotto_categorie/"+str(row["Categoria"])+".txt","w+") as f:
        f.write(str(h))
    time.sleep(1)
driver.quit()


    

    
    
    
    
    
    


   