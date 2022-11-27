#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:18:44 2022

@author: mattia
"""

import pandas as pd

df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Vestiti.csv")
try:      
    df = df.drop('Unnamed: 0', axis=1)
except:
    pass


#df.loc[0].Articolo




for i,row in df[df.Categoria=="Altro"].iterrows():
    
    
    if "pigiami" in df.loc[i].Articolo.lower() or "pigiama" in df.loc[i].Articolo.lower():
        df["Categoria"][i]="Pigiami"
        
    elif  "t-shirt" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="T-shirt"
    
    
    elif  "felpa" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="Felpe"
        
    elif  "pullover" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="Maglioni e cardigan"


        
    elif  "top" in df.loc[i].Articolo.lower() or "maglia" in df.loc[i].Articolo.lower() or "maglie" in df.loc[i].Articolo.lower() or "polo" in df.loc[i].Articolo.lower():
        df["Categoria"][i]="Magliette e top"     
        
    elif  "giacca" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="Giacche e cappotti"    
        
    elif  "camicia" in df.loc[i].Articolo.lower() or "camicetta" in df.loc[i].Articolo.lower():
        df["Categoria"][i]="Camicie"    
        
    elif  "boxer" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="Biancheria Intima"    
        
    elif  "gonna" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="Gonne"    
        
    elif  "polo" in df.loc[i].Articolo.lower() :
        df["Categoria"][i]="Gonne"    





xd
