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


df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Scraping Gucci/1) Estrazione dati/Donna/LINK:HTML/link_sottocategorie.csv")
df = df.drop('Unnamed: 0', axis=1)


options = Options()
options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
options.add_experimental_option("prefs", prefs)    
driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)





new_data=pd.DataFrame(columns=["Categoria","Sotto_categoria","Link"])

for i,row in alive_it(df.iterrows(),title="Estrazione articoli"):
    try:
        driver.get(row.Link)
        html=driver.page_source  
        
        try:
            cookie=WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id='onetrust-accept-btn-handler']"))).click()
        except:
            pass

        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        try:
            visualizza_altro=WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='productGridLoadMoreLnk']"))).click()
        except:
            pass
        

   #Apertura pagina
        

        #Ottenere html corretto
        soup=BeautifulSoup(html,'html.parser')
        with open("/Users/mattia/desktop/HTML Gucci/Sotto_categorie/"+str(row["Categoria"])+"_"+str(row["Sotto_categoria"])+".txt","w+") as f:
            f.write(str(soup))
        try:
            articoli=soup.find("div",{"class":"product-tiles-grid"})
            lista_articoli=articoli.find_all("article")
            for j in range(len(lista_articoli)):
                
                link="https://www.gucci.com"+lista_articoli[j].find("a").get("href")
                df_provvisorio=pd.DataFrame({"Categoria":[row["Categoria"]],"Sotto_categoria":[row["Sotto_categoria"]],"Link":[link]})
                new_data=pd.concat([new_data,df_provvisorio])
                
                
        except:
            pass

    except:
        pass
    time.sleep(1)
    

        
    
    
driver.quit()
new_data.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Scraping Gucci/1) Estrazione dati/Donna/LINK:HTML/link_articoli.csv")









