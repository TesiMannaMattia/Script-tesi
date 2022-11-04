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










#%% Parametri, headers BeautifulSoup



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




#from cambiopagina import *

#%% Funzione
def estrazione_articoli(lista):
    """
    Questa funzione estrae dalla sezione degli articoli tutti i nomi dei prodotti e i loro link alla pagina dedicata.
    Una volta estratti gli argomenti vengono inseriti in un dizionario.
    La chiave del dizionario è il nome del prodotto.
    """
    #Connessione al sito, presa e parsing HTML
    dizionario_articoli={}
    for i in range(0,len(lista)):
        
        #testo=listahtml[i]
        #print(len(testo),type(testo))
        response=requests.post(lista[i],data=post_params,headers=headers)
        soup=BeautifulSoup(response.text,'html.parser')
        

        #Estrazione 
        articoli=soup.find_all("a",{"class":"product-card__name"})

        #Creazione dizionario
        

        for j in range(0,len(articoli)):
    
            #ESTRAZIONE DEL LINK
            link_articolo=articoli[j].get('href')
            link_articolo="https://www.hollisterco.com"+link_articolo
    
            #NOME ARTICOLO
            nome_articolo=articoli[j].text
        
            #CREAZIONE DIZIONARIO DEGLI ARTICOLI
            dizionario_articoli[nome_articolo]=link_articolo
        

    

    return dizionario_articoli



