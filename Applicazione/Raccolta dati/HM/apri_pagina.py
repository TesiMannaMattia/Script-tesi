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

from estrazione_dati import estrazionedati

#%% Funzione
def apri_pagina(link,ID_articoli_estratti):
    """
    Estrae i dati dell'articolo.
    """
    #Connessione al sito, presa e parsing HTML
    options = Options()
    options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
    options.add_experimental_option("prefs", prefs)    
    driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)

    driver.get(link)
    
    #Inizializzazione liste
    nomi=[]
    idd=[]
    prezzi=[]
    materiali=[]
    altri=[]
    colorei=[]
    sconti=[]
    #COOKIE
    try:
        time.sleep(1)
        recentList = driver.find_elements_by_xpath("//div[@id='onetrust-banner-sdk']") 
        for list in recentList :
            #time.sleep(2)
            #driver.execute_script("arguments[0].scrollIntoView();", list )
            driver.execute_script("window.scrollBy(0,150)")
            #time.sleep(2)
            bottone_cookie=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accetta tutti i cookie')]"))).click()
             
    except:
        n=1

    driver.execute_script("window.scrollBy(0,500)")    
    
    #MOLTO IMPORTANTE, da utilizzare quando non funziona get_source
    #https://stackoverflow.com/questions/39047079/cant-view-complete-page-source-in-selenium
    content = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    h=driver.page_source  
    html=BeautifulSoup(h,"html.parser")
    
    
    #colore=html.find("div",{"class":"product-colors miniatures clearfix slider-completed loaded"})
    primo_colore=html.find("h3").text
    #print("1",primo_colore,"2")
    nome, id_articolo, prezzo,sconto, materiale, altro = estrazionedati(html)
    if id_articolo not in ID_articoli_estratti:
        nomi.append(nome)
        idd.append(id_articolo)
        prezzi.append(prezzo)
        sconti.append(sconto)
        materiali.append(materiale)
        altri.append(altro)
        colorei.append(primo_colore)
        ID_articoli_estratti.append(id_articolo)
        

        
  
    #AGGIIUNTA DEL TRY perchè una volta si è bloccata senza motivo
    try:
        colori=html.find("li",{"class":"mini-slider-group"})
        colori=colori.find_all("a") 
    except:
        try:
            time.sleep(5)
            h=driver.page_source  
            html=BeautifulSoup(h,"html.parser")
            colori=html.find("li",{"class":"mini-slider-group"})
            colori=colori.find_all("a") 
        except:
            driver.quit()
            return nomi, idd, prezzi,sconti,materiali,altri,colorei,ID_articoli_estratti
            
        
    
    
    
    for i in range(0,len(colori)):
            
         try:
             nome_colore=colori[i].get("data-color")
         except:
             try:
                 nome_colore=html.find("h3").text
             
             except:
                 nome_colore="Null"
                 continue 
            
         if nome_colore == primo_colore :
             #print("Skip",nome_colore)
             continue 
                
        # print("fuori",nome_colore)   
         
         #CAMBIO COLORE
         try:
             l= driver.find_element_by_xpath("//a[@data-color='"+str(nome_colore)+"']") 
             l.click()
         except:
             try:
                 l= driver.find_element_by_xpath("//a[@data-color=' "+str(nome_colore)+" ']") 
                 l.click()
             except:
                 try:
                     l= driver.find_element_by_xpath("//a[@title='"+str(nome_colore)+"']") 
                     l.click()
                 except:
                     continue 
                     
         time.sleep(2)
         
         #NUOVA ESTRAZIONE HTML
         content_iterato = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
         h_iterato=driver.page_source  

         #AGGIUNTA DATI
         nome, id_articolo, prezzo,sconto, materiale, altro =estrazionedati(h_iterato)
         if id_articolo not in ID_articoli_estratti:
             nomi.append(nome)
             idd.append(id_articolo)
             prezzi.append(prezzo)
             sconti.append(sconto)
             materiali.append(materiale)
             altri.append(altro)
             colorei.append(nome_colore)
             ID_articoli_estratti.append(id_articolo)
             
    
    driver.quit()
    return nomi, idd, prezzi,sconti,materiali,altri,colorei,ID_articoli_estratti


#link="https://www2.hm.com/it_it/productpage.0979329019.html"
#link="https://www2.hm.com/it_it/productpage.1065284004.html"   

#link="https://www2.hm.com/it_it/productpage.1089853001.html"

#link="https://www2.hm.com/it_it/productpage.1031140002.html"

#link="https://www2.hm.com/it_it/productpage.1024982002.html"
#link="https://www2.hm.com/it_it/productpage.1067060003.html"
        
#link="https://www2.hm.com/it_it/productpage.1078054001.html"
#link="https://www2.hm.com/it_it/productpage.1096337001.html"    

#https://www2.hm.com/it_it/productpage.1096337001.html
#link="https://www2.hm.com/it_it/productpage.1059302003.html"
#link="https://www2.hm.com/it_it/productpage.1067325001.html"
#print(apri_pagina(link,["1059302002"]))
#nome, materiale, altro, prezzo, id_articolo=estrazionedati(link)
