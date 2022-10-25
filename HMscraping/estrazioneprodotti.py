"""
estrazione_tipo_prodotti
"""
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










#%% Funzione 

def estrazione_tipo_prodotti(url) :
    """
    Questa funzione estrae dal sito le categorie dei prodotti e le colloca in un dizionario.
    Delle categorie si prendono il nome ed il link alla loro pagina.
    La funzione prendere come input url della pagina di uomini o donne.
    """
    
    
    #Connessione al sito, presa e parsing HTML
    response=requests.post(url,data=post_params,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    
    #Prendere la sezione con le categorie di prodotto
    sezione_link=soup.find("ul",{"class":"grid-nav__items-group regular hide-sm"})

    #Prendere le tag contenenti nome  di categoria e link alla pagina associata
    tag_a=sezione_link.find_all("a")

    #Inizializzazione dizionario
    dizionario={}

    for i in range(0,len(tag_a)):
    
        #Estrazione nome della categoria di prodotto
        nome=tag_a[i].text
        nome=" ".join(nome.split())  #Grazie https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
    
        #Estrazione link delle categoria
        link_parziale=tag_a[i].get('href')
        link="https://www.hollisterco.com"+link_parziale
    
        #Inserimento nel dizionario
        dizionario[nome]=link
    return dizionario

#link="https://www.hollisterco.com/shop/eu-it/uomo"

#diz=estrazione_tipo_prodotti(link)
#for i in diz.keys():
 #   print(i)
    


