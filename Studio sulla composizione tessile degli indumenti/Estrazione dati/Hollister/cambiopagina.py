"""
Funzione per caricare tutti gli articoli. 
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






def cambia_pagina(url):
    """
    Questa funzione permette di premere i pulsanti in fondo alla pagina per caricare la nuova pagina di articoli.
    È stata fatta per venire incontro alla costruzione del sito, difatti non tutti gli articoli di 
    una categoria sono presenti in una  pagina, ma magari sono disposti in 5 6 o più pagine...
    """
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


    #BeautifulSoup ricavarsi numero di iterazioni
    response=requests.post(url,data=post_params,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')

    #Estrazione numero di iterazioni
    nav=soup.find("nav",{"id":"grid-pagination"})
    ul=nav.find("ul",{"id" : "grid-pagination-control"})
    li=ul.find_all("li")
    niterazioni=len(li)

    #Opzioni drivere selenium
    options = Options()
    options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
    options.add_experimental_option("prefs", prefs)


    #Aprire Google Chrome
    driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)


    #APRIRE LA PAGINA
    driver.get(url)


    #Grazie Tech Path link al canale youtube : 'https://www.youtube.com/watch?v=qhJ_gMB772U'
    previous_height=driver.execute_script('return document.body.scrollHeight')

    #Contatore e clausola ciclo while
    iterazione=1
    
    listalink=[url]
    #listahtml=[str(soup)]
    while iterazione < niterazioni :
    
        #Aspettare
        time.sleep(1)
    
        #Scrollare 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
        #Aspettare
        time.sleep(1)
    
        #Nuova altezza pixel
        new_height=driver.execute_script('return document.body.scrollHeight')
    
        
        if new_height == previous_height :
            
            antistallo=0
            while True:
                driver.execute_script('window.scrollBy(0,-500)')
                time.sleep(1)
                try:
                    #Cliccare sul pulsante 
                    driver.find_element_by_xpath('//*[@id="grid-pagination"]/button[3]').click() 
            
                    #Attendere qualche secondo
                    time.sleep(1)
                
                    #Prendere link pagina
                    linkete=driver.current_url
                    listalink.append(str(linkete))
                    
                
                    #Prendere l'html
                    # listahtml.append(driver.page_source)
                
                    #Scrollare tutto su
                    driver.execute_script('window.scrollTo(0,0)')   
                
                    #Ristemare i parametri di altezza pixel
                    previous_height=driver.execute_script('return document.body.scrollHeight')
                
                    #Uscita dal while
                    iterazione += 1
                    break 

                except:
                    driver.execute_script('window.scrollBy(0,-50)')
                    antistallo +=1 
                    if (antistallo % 15 ) == 0 :
                       break
                        

                    
    
        #Aggiornare altezza pixel    
        previous_height = new_height
    
    #Chiudere Chrome
    driver.quit()
    return listalink




cambia_pagina("https://www.hollisterco.com/shop/eu-it/uomo-pezzi-di-sotto")


    




