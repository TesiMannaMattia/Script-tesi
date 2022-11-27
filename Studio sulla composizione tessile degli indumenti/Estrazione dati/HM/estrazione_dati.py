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
from estrai_attributi import *
#%% Funzione

def estrazionedati(sorgente):
    try:
        html=BeautifulSoup(sorgente,"html.parser")
        
    except:
        html=sorgente

    
    
    
    try:
        
        blocco=html.find("dl",{"class":"ProductAttributesList-module--datalist__ketGC"})
        materiale, id_articolo,altro=estrazione_attributi(blocco)
        
    except:
        materiale="Null"
        id_articolo="Null"
        altro="Null"
    
    

        
    
    #ESTRAZIONE NOME
    try:
        nome=html.find("div",{"class":"ProductName-module--container__3e-gi"})
        nome=nome.find("h1")
        nome=nome.text
        nome=nome.strip()
        nome=nome.lower()
    except:
        nome="Null"
        
    #ESTRAZIONE PREZZO
    try:
        blocco=html.find("div",{"class":"ProductPrice-module--productItemPrice__2i2Hc"})
        span=blocco.find_all("span")
        
        elementi=len(span)
        sconto="Null"
        for i in range(0,elementi):
            if elementi >1 :
                if i==0:
                    
                    sconto=span[i].text
                    #https://stackoverflow.com/questions/22019556/remove-euro-sign-from-string
                    sconto=sconto.lstrip("€").strip()
                    sconto=sconto.replace(",", ".")
                else:
                    prezzo=span[i].text
                    #https://stackoverflow.com/questions/22019556/remove-euro-sign-from-string
                    prezzo=prezzo.lstrip("€").strip()
                    prezzo=prezzo.replace(",", ".")
                    
                
            else:
                prezzo=span[i].text
                #https://stackoverflow.com/questions/22019556/remove-euro-sign-from-string
                prezzo=prezzo.lstrip("€").strip()
                prezzo=prezzo.replace(",", ".")
            
            
    except:
        prezzo="Null"
        sconto="Null"
        
    return nome, id_articolo, prezzo,sconto, materiale, altro 



