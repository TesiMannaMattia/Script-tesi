#%%Importazione pacchetti
#Importazione pacchetti per selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import wget
import time 

#Importazione pacchetti per BeautifulSoup
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#Importazione pacchetti per esportare in csv
import pandas as pd  

#Per lavorare con le date
from datetime import date 
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



def estrazione_sottocategorie(link,chiave):
    

    #options = Options()
    #options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
   # prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
  #  options.add_experimental_option("prefs", prefs)
    
    #Aprire Google Chrome
#    driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)
 #   driver.maximize_window()
    #APRIRE LA PAGINA
   # driver.get(link)
    
    
    response=requests.post(link,data=post_params,headers=headers)
    html=BeautifulSoup(response.text,'html.parser')
    
    #PRENDERE e PROCESSARE L'HTML DELLA PAGINA
  #  html=driver.page_source
  
#    html=BeautifulSoup(html,'html.parser')

#    driver.quit()
    
    #Andare sulla griglia
    griglia=html.find("div",{"class":"grid-nav__items-wrapper"})
    ull=griglia.find("ul",{"class":"grid-nav__items-group regular hide-sm"})



    lista_link=[]
    lista_tipo=[]
    #Grazie alla pagina : https://www.geeksforgeeks.org/beautifulsoup-nextsibling/

    try:
        element = ull.li
        a=element.find("a")
    
        linketto=a.get("href")
        linketto="https://www.hollisterco.com"+str(linketto) 
        testo=a.text

        lista_tipo.append(testo.strip())
        lista_link.append(linketto)


        nextSiblings = element.find_next_siblings("li")
        for i in range(0,len(nextSiblings)):
    
            primo=nextSiblings[i]
            
            a=primo.find("a")
    
            linketto=a.get("href")
            linketto= "https://www.hollisterco.com"+str(linketto) 
    
            testo=a.text
    
    
            lista_tipo.append(testo.strip())
            lista_link.append(linketto)
    
        return lista_tipo,lista_link
    except:
        lista_tipo.append(chiave)
        lista_link.append(link)
        return lista_tipo, lista_link
     
#link="https://www.hollisterco.com/shop/eu-it/donna-coordinati"    
#link="https://www.hollisterco.com/shop/eu-it/uomo-topwear"
#link="https://www.hollisterco.com/shop/eu-it/uomo-pezzi-di-sotto" 
#link="https://www.hollisterco.com/shop/eu-it/donna-costumi-da-bagno"
#link="https://www.hollisterco.com/shop/eu-it/donna-pantaloni-da-jogging-activewear"
#print(estrazione_sottocategorie(link,"Pezzi di sotto"))
