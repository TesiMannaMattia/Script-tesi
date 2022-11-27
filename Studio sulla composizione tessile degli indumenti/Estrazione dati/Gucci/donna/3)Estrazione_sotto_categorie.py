#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:00:54 2022

@author: mattia
"""

import pandas as pd
from bs4 import BeautifulSoup
import re
import os 


df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Scraping Gucci/1) Estrazione dati/Donna/LINK:HTML/link_categorie.csv")
df = df.drop('Unnamed: 0', axis=1)





new_data=pd.DataFrame(columns=["Categoria","Sotto_categoria","Link"])
for i,row in df.iterrows():
    if row["Categoria"]=="Activewear" or row["Categoria"]=="Costumi da Bagno" or  row["Categoria"]=="Denim Donna" or row["Categoria"]=="Activewear Donna" or row["Categoria"]=="Abiti da cocktail e da sera Donna" or row["Categoria"]=="Costumi da Bagno Donna"or row["Categoria"]=="Completi Donna"or row["Categoria"]=="Lingerie Donna":
        df_provvisorio=pd.DataFrame({"Categoria":[row["Categoria"]],"Sotto_categoria":["Null"],"Link":[row["Link"]]})
        new_data=pd.concat([new_data,df_provvisorio])
        
        continue 
    with open("/Users/mattia/Desktop/HTML Gucci/Sotto_categorie/"+row["Categoria"]+".txt","r") as f:
        html=f.readlines()
       
    soup=BeautifulSoup(str(html),'html.parser')
    categorie=soup.find("div",{"class":"filter-bar-container"})
    categorie=categorie.find("nav",{"class":"filter-nav"}).find("ul").find("li",{"class":"filter-dropdown filter-category-expander"}).find("ul")
    categorie=categorie.find_all("li")  
        


   

    for i in range(1,len(categorie)):
        link="https://www.gucci.com/"+categorie[i].find("a").get("href")
        
        

        nome_sottocategoria=categorie[i].find("a").text.strip()
        nome_sottocategoria=re.sub("[',()\d]*","",nome_sottocategoria)
        nome_sottocategoria=nome_sottocategoria.replace("\\n","")
        nome_sottocategoria=nome_sottocategoria.strip()

        
        
        
        
        df_provvisorio=pd.DataFrame({"Categoria":[row["Categoria"]],"Sotto_categoria":[nome_sottocategoria],"Link":[link]})
        new_data=pd.concat([new_data,df_provvisorio])
    
        
new_data.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Codici/Scraping Gucci/1) Estrazione dati/Donna/LINK:HTML/link_sottocategorie.csv")






