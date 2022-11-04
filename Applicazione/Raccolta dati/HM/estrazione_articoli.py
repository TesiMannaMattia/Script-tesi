#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:47:32 2022

@author: mattia
"""

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



def estrazione_link_articoli(link,lista_link):
    #Connessione al sito, presa e parsing HTML
    options = Options()
    options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
    options.add_experimental_option("prefs", prefs)    
    driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)

    #Apertura sito
    driver.get(link)
    
    h=driver.page_source  
    html=BeautifulSoup(h,"html.parser")
    
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
        

    
    
    

        
    
    iterazione=0
    margine=None
    previous_height=driver.execute_script('return document.body.scrollHeight')
    while True :
        
        #Aspettare
        time.sleep(1)
        
        
        
        #Scrollare 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        
        #Aspettare
        time.sleep(1)
        
        #Nuova altezza pixel
        new_height=driver.execute_script('return document.body.scrollHeight')
        
            
        if new_height == previous_height :
            
            h=driver.page_source  
            html=BeautifulSoup(h,'html.parser')
            sezione=html.find("div",{"class":"load-more-products"})
            try:
                sup=sezione.find("h2").get("data-total")
                inf=sezione.find("h2").get("data-items-shown")
            except:
                driver.quit()
                dizionario_articoli={"Skip":"skipper"}
                return dizionario_articoli, lista_link 
                
            if iterazione == 0:
                margine=(int(sup) // int(inf))+ 5
                

          #  print(sup,inf,margine)
            if int(inf) == int(sup):
                break
           
            antistallo=0
            while True:
                driver.execute_script('window.scrollBy(0,-500)')
                time.sleep(1)
                try:
                    #Cliccare sul pulsante 
                  #  print("prova click")
                    #time.sleep(2)
                   # WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='event']"))).click()
                   # l=driver.find_element_by_css_selector("button[type='event']")
                   # l.click()
                    g=WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Carica altri prodotti')]"))).click()
                    
                    
                    #print("click riuscito")
                    #Attendere qualche secondo
                    time.sleep(1)
          
                    #Ristemare i parametri di altezza pixel
                    previous_height=driver.execute_script('return document.body.scrollHeight')
                    break 

                except:
                   # print("Click non riuscito",antistallo)
                    driver.execute_script('window.scrollBy(0,-50)')
                    antistallo +=1 
                    if (antistallo % 15 ) == 0 :
                        break
                            
        iterazione += 1 
        #print(margine)
       # print(iterazione)
        if margine==iterazione:
            break
        #Aggiornare altezza pixel    
        previous_height = new_height
        
    h=driver.page_source  
    html=BeautifulSoup(h,'html.parser')
    tutti=html.find("ul",{"class":"products-listing small"})
    articoli=tutti.find_all("li",{"class":"product-item"})        
    
    dizionario_articoli={}    
    for i in range(0,len(articoli)):
        
        articolo=articoli[i].find("article")
        articolo=articolo.find("div",{"class":"item-details"})
        
        articolo=articolo.find("h3",{"class":"item-heading"})
        a=articolo.find("a")
        
        link_articolo=a.get("href")
        link_articolo="https://www2.hm.com"+link_articolo
        
        
        nome_articolo=a.text
        nome_articolo=nome_articolo.strip()
        nome_articolo=nome_articolo.lower()
        if nome_articolo in dizionario_articoli.keys():
            nome_articolo=nome_articolo +" "+str(i)
            
        if link_articolo not in lista_link :
            dizionario_articoli[nome_articolo]=link_articolo
            lista_link.append(link_articolo)
        else:
            continue 
    
    driver.quit()
    return dizionario_articoli, lista_link 

#link="https://www2.hm.com/it_it/donna/acquista-per-prodotto/cardigan-e-pullover/ponchos.html"    
#link="https://www2.hm.com/it_it/donna/acquista-per-prodotto/top/maniche-corte.html"    
#link="https://www2.hm.com/it_it/donna/acquista-per-prodotto/abiti/vestiti-jeans.html"
#lista=["https://www2.hm.com/it_it/productpage.1071018001.html"]
#diz,li=estrazione_link_articoli(link,lista)
    
#print(len(diz),len(li))





    