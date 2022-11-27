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

#%% Funzione
def estrazione_sotto_categorie(link):
    """
    Estrae le sotto categorie dei prodotti dal sito HM.
    """
    #Connessione al sito, presa e parsing HTML
    options = Options()
    options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
    options.add_experimental_option("prefs", prefs)
    driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)
    driver.maximize_window()    

    #Aprire la pagina web
    driver.get(link)
    
    #Prendere html della pagina web
    h=driver.page_source
 
    #Parsing dell'html
    html=BeautifulSoup(h,'html.parser')
    
    #RICERCA TAG, entrare nel blocco delle categorie ed estrarre tutte le tag
    #li contenenti i nomi ed i link delle sottocategorie.
    ul=html.find("ul",{"id":"menu-links"})
    lista_li=ul.find_all("li",{"class":"list-group"})
    for i in range(0,len(lista_li)):
        nome=lista_li[i].find("strong").text.strip()
        #print("3",nome,"1")
        #print(nome)
        if nome == "Acquista per prodotto":
            elemento=lista_li[i]
            
            break
    #    print(nome)
    #elemento=lista_li[3]
    ull=elemento.find("ul",{"class":"menu"})
    liii=ull.find("li",{"class","list-group"})
    ul=liii.find("ul",{"class" :"menu"})
    sottocategorie=ul.find_all("li")
    
    dizionario_sottocategorie={}
    for i in range(0,len(sottocategorie)):
        #Elemento iterato
        tag=sottocategorie[i]
        
        #Trovare la tag anchor contenente i link ed il nome delle categorie
        a=tag.find("a")
        
        #Estrarre il link
        link_categoria=a.get("href")
        link_categoria="https://www2.hm.com"+link_categoria
        
        #Estrarre il testo e pulirlo, pulizia testo per rendere tutto omogeneo
        testo=a.text
        
        testo=testo.strip() #rimuovere spazi
        testo=testo.lower() #tutto minuscolo
        
        #Allocare i valori nel dizionario
        dizionario_sottocategorie[testo]=link_categoria
    driver.quit()
    return dizionario_sottocategorie
#if __name__ == '__main__':
    #link="https://www2.hm.com/it_it/uomo/acquista-per-prodotto/t-shirt-e-canotte.html"
    #link="https://www2.hm.com/it_it/donna/acquista-per-prodotto/cardigan-e-pullover.html"
    #link="https://www2.hm.com/it_it/donna/acquista-per-prodotto/intimo-notte.html"
    #z=estrazione_sotto_categorie(link)
    #print(z)



