"""
In questo script si estraggono i link delle sotto categorie da donna da EA7
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
from tqdm import tqdm 
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




df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/EA7/Uomo/LINK:HTML/link_categorie.csv")
df = df.drop('Unnamed: 0', axis=1)


new_data=pd.DataFrame(columns=["Categoria","Sotto_categoria","Link"])
for i,row in alive_it(df.iterrows(),title="Estrazione"):
   try:
       #print(row["Categoria"])
    
       #Richiesta http protocol
       response=requests.post(row["Link"],data=post_params,headers=headers)
    
       #Ottenere html corretto
       soup=BeautifulSoup(response.text,'html.parser')
    
       #Prendere il macro elemento
       pezzi=soup.find("div",{"class":"search__wrapper"})
       pezzi=pezzi.find("plp-refinements",{"class":"plp-refinements anim-hidden hidden"})
       pezzi=pezzi.find("div",{"class":"refinements"})
    
       #Accedere ai filtri
       pezzi=pezzi.find("ul")
    
    
       #Accesso alle categorie
       sotto_categorie=pezzi.find("li",{"class":"refinement refinement--category_2"})
    
       #Accesso ai value delle categorie
       #  categorie=categorie.find("div",{"class":"refinement__content anim-hidden hidden"})
       sotto_categorie=sotto_categorie.find("ul",{"class":"facets facet-category_2"})
       sotto_categorie=sotto_categorie.find_all("li",{"class":"facet"}) 
        
       
       #Iterare su tutte le sottocategorie, si fa perchè  "sotto_categorie.find_all("li",{"class":"facet"}) "
       #prendeva tutte le categorie e non quelle attive.
       for i in range(len(sotto_categorie)):
           
           #Trovare le sotto_categorie 
           #Per fare questo si ricercano le sottocategorie attive nel link corrispondente
           
           if len(sotto_categorie[i].get("class"))==1: #per capire se una sottocategoria è attiva.
               testo=sotto_categorie[i].find("label").find("span").text.strip()
              # print(testo)
         
               
               A=sotto_categorie[i].get("data-ytos-facet")
               dizionario = json.loads(A)  #convertire una stringa in un dizionario  
               
               
               #COMPOSIZIONE DEL LINK
    
    
               #Comporre la prima parte del link, parte relativa alla categoria
               a=row["SemiLink"]
               link_1=re.findall(r"([\w]*%)(.+)",a)[0][0]
               link_2=re.findall(r"([\w]*%)(.+)",a)[0][1]
               
               
               #Comporre la seconda parte del link, parte relativa alla sotto_categoria
               link_3=re.findall(r"(ads_)(.+)",dizionario["value"])[0][1]
               link_4=re.findall(r"([\w]*%)(.+)",dizionario["value"])[0][1]
           
               #UNIRE TUTTI I PEZZI 
               LINK=link_1+str(25)+link_2+"%2Cads_"+link_3+"%"+str(25)+link_4
     
    
    
               #OTTENERE IL LINK FINALE
               link_finale="https://www.armani.com/it-it/ea7/uomo/abbigliamento/?department=EU_GA_M_Clothing&departmentId=3074457345616677883&facetsvalue=" +str(LINK)+"&itemsToLoadOnNextPage=0&lazyLoadStart=4&linkdepartment=EU_GA_M_Clothing&linkdepartmentId=3074457345616677883&page=1&partialLoadedItems=6&productsPerPage=36&rsiUsed=false&suggestion=false&totalItems=6&totalPages=1&ytosQuery=true"
               
           
              # response=requests.post(link_finale,data=post_params,headers=headers)
               #print(response)
               
               df_provvisorio=pd.DataFrame({"Categoria":[row["Categoria"]],"Sotto_categoria":[testo],"Link":[link_finale]})
               
               new_data=pd.concat([new_data,df_provvisorio])
   except:
       pass

           
new_data.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/EA7/Uomo/LINK:HTML/link_sottocategorie.csv")

