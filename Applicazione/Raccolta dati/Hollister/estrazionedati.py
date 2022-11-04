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
def estrazione_dati(link,controllo_link):
    
    """
    Questa funzione estrae dalla pagina dell'articolo  il materiale ed il colore
    """
    #time.sleep(2)  #Tempo attesa
    
    options = Options()
    options.add_argument("--Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    prefs = {"profile.managed_default_content_settings.images": 2} #Per non caricare le immagini
    options.add_experimental_option("prefs", prefs)
    
    #Aprire Google Chrome
    driver=webdriver.Chrome("/Users/mattia/opt/chromedriver",options=options)
    driver.maximize_window()
    #APRIRE LA PAGINA
    driver.get(link)
    controllo_link.append(link)
    
    #time.sleep(1)  #Tempo attesa
    #driver.get_screenshot_as_file("screenshot.png")
    
    #Scrollare la pagina
    driver.execute_script("window.scrollBy(0,500)")

    #time.sleep(1)  #Tempo attesa


    #------------------------------------------------------------------------##------------------------------------------------------------------------# #------------------------------------------------------------------------#
    #CLICCARE SUL PULSANTE "Dettagli e materiali"
    condizione=True
    nscroll=0
    antibuggoni=0
    lista_materiali=[]
    lista_colori=[]
    lista_titoli=[]
    lista_prezzi=[]
    lista_sconti=[]
    ID=[]
    while condizione==True:
        try :
            
            #print("try")
            buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Dettagli e materiali')]") #Grazie kchomski 
         #   len(buttons)       #https://stackoverflow.com/questions/35470171/click-button-by-text-using-python-and-selenium
            for btn in buttons:
                btn.click()
                condizione=False
                break

            
            antibuggoni += 1 
            #print(antibuggoni)
            if antibuggoni == 50:
                marca="NULL"
                prezzo=["NULL"]
                materiale=["NULL"]
                colori=["NULL"]
                lista_titoli=["NULL"]
                lista_sconti=["NULL"]
                lista_prezzi.append("NULL")
                #print("NIENTE DA ESTRARRE, LINK SKIPPATO")
                driver.quit()
                return materiale, colori,controllo_link,marca, lista_prezzi,lista_sconti,lista_titoli
                
        except :
            #print("Except")
            driver.execute_script("window.scrollBy(0,200)")
            nscroll += 1
            #print("Iterazioen", nscroll, "\n")
            if (nscroll % 10 )==0 and nscroll != 0:
                driver.execute_script("window.scrollTo(0,0)")
            
            if nscroll == 50:
                marca="NULL"
               
                materiale=["NULL"]
                colori=["NULL"]
                lista_titoli=["NULL"]
                lista_sconti=["NULL"]
                lista_prezzi.append("NULL")
                #print("NIENTE DA ESTRARRE, LINK SKIPPATO")
                driver.quit()
                return materiale, colori,controllo_link,marca, lista_prezzi,lista_sconti,lista_titoli

     #------------------------------------------------------------------------# #------------------------------------------------------------------------# #------------------------------------------------------------------------#            
     #------------------------------------------------------------------------# #------------------------------------------------------------------------# #------------------------------------------------------------------------#           
     #------------------------------------------------------------------------# #------------------------------------------------------------------------#  #------------------------------------------------------------------------#

    
    #PRENDERE e PROCESSARE L'HTML DELLA PAGINA
    html=driver.page_source
    html=BeautifulSoup(html,'html.parser')
    
    #Marca e prezzo si prendono subito perchè non cambiano, anche se il prezzo di una determinato colore cambia non ci interessa.
    
    #ESTRAZIONE MARCA
    try:
        marca=html.find("div",{"class":"logo"})
        marca=marca.find("span",{"class","screen-reader-text"})
        marca=marca.text
    except:
        marca="NULL"

    
    #PREZZO
    try:
        try:

            prezzo=html.find("div",{ "class":"product-price-v2"} )
            prezzo=prezzo.find("div",{"class": "product-price-v2__inner"})
            prezzo=prezzo.get("data-high-list-price")
            
        except:
                
            try:
                prezzi=html.find("span",{"class","product-price-text-wrapper"})
                prezzi=prezzi.find("span",{"class" :"product-price js-main-price"})
                prezzi=prezzi.find_all("span",{"class":"product-price-text product-price-font-size ds-override" }).text
                for i in range(0,len(prezzi)):
                    if i == 0:
                        prezzo=prezzi[i].text
                        prezzo=re.findall(r'[\d\.]+',prezzo)
                    elif i ==1:
                        sconto=prezzi[i].text
                        sconto=re.findall(r'[\d\.]+',sconto)
                  
                
            except:
               
                prezzo=html.find("span",{"class","product-price-text-wrapper"})
                prezzo=prezzo.find("span",{"class":"product-price-text product-price-font-size ds-override" }).text
                prezzi=prezzi.find_all("span",{"class":"product-price-text product-price-font-size ds-override" }).text
                for i in range(0,len(prezzi)):
                    if i == 0:
                        prezzo=prezzi[i].text
                        prezzo=re.findall(r'[\d\.]+',prezzo)
                    elif i ==1:
                        sconto=prezzi[i].text
                        sconto=re.findall(r'[\d\.]+',sconto)
            
    
    except:
        lista_prezzi.append("NULL")
        lista_sconti.append("NULL")
        
    #------------------------------------------------------------------------# #------------------------------------------------------------------------#
    #------------------------------------------------------------------------# #------------------------------------------------------------------------#
    #ESTRARRE LE INFORMAZIONI PER OGNI ARTICOLO IN BASE AL COLORE 
    
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,-300)")  #Dal pulsante "Dettagli e materiali" torna ai pulsanti dei colori

    #Prendere le informazioni  riguardanti al primo colore dell'articolo e poi fermarsi se c'è solo un colore.
    html=driver.page_source
    html=BeautifulSoup(html,'html.parser')

   
    lista_materiali=[]
    lista_colori=[]
    lista_titoli=[]
    lista_prezzi=[]
    lista_sconti=[]
    ID=[]
    #ESTRARRE TITOLO
    try:
        titolo=html.find("h1",{"class":"product-title-component product-title-main-header" })
        lista_titoli.append(titolo.text)
    except:
        lista_titoli.append("NULL")
       
    
    #----#  
    #ESTARRE I MATERIALI 
    try:
        materiali=html.find("div",{"class":"h4 fiber-content__label"})
        materiale=materiali.text
        lista_materiali.append(materiale)
        #print("Materiale ottenuto",materiale)
    except: 
        #Questa clausola è stata inserita perchè alcuni articoli non hanno la cella materiale
        materiale="NULL"
        lista_materiali.append(materiale)
        # print("Materiale non ottenuto")
    #----#
 
    #ESTRAZIONE DEL COLORE
 
    try:
      #  print("Try1")
        try:
         #   print("Caso con più colori, con tanti radio button")#Caso con più colori, con tanti radio button
            colore=html.find("div",{"class":"product-page__swatches-attributes scope-1892"})
            colore=colore.find("h3",{"class" : "product-attrs__shown-in"})
            colore=colore.find("span")
            lista_colori.append(colore.text.upper())
        except:
            try:
             #   print("Caso un colore solo, con  un solo radio button")
                #Caso un colore solo, con  un solo radio button
                colore=html.find("h3",{"class" : "product-attrs__shown-in  single-swatch"})
                colore=colore.find("span",{"class":"selected-swatch__label  single-swatch"})
                colore=colore.text
                lista_colori.append(colore.upper())
                
            except:
               # print("n colore solo, senza radio button")
                #Un colore solo, senza radio button
                colore=html.find("h3",{"class" : "product-attrs__shown-in single-swatch"})
                colore=colore.find("span")
                colore=colore.text
                lista_colori.append(colore.upper())                
                
           
    except:
    #    print("Except")
        lista_colori.append("NULL")
                
    #ESTRARRE id 
    try:
        idd=html.find("p",{"class":"details__store-item-number text-small"})
        idd=idd.find("span",{"class":"number"}).text.strip()
        ID.append(idd)
                    
    except:
        ID.append("Null")
   
    try:
        try:
            prezzi=html.find("div",{"class":"product-price-v2"})
            prezzi=prezzi.find("div",{"class" :"js-product-price"})
            prezzi=prezzi.find("span",{"class","product-price-text-wrapper"})
            prezzi=prezzi.find_all("span",{"class":"product-price-text product-price-font-size ds-override" })
            #print(prezzi)   
            for i in range(0,len(prezzi)):
                if i == 0 and len(prezzi)>1:
                    prezzo=prezzi[i].text
                    prezzo=re.findall(r'[\d\.]+',prezzo)
                    lista_prezzi.append(prezzo[0])
                elif i==0 and len(prezzi)==1:
                    prezzo=prezzi[i].text
                    prezzo=re.findall(r'[\d\.]+',prezzo)
                    lista_prezzi.append(prezzo[0])
                    lista_sconti.append("Null")
                elif i ==1:
                    sconto=prezzi[i].text
                    sconto=re.findall(r'[\d\.]+',sconto)
                    lista_sconti.append(sconto[0])

        except:
                
            try:
                prezzo=html.find("span",{"class","product-price-text-wrapper"})
                prezzo=prezzo.find("span",{"class":"product-price-text product-price-font-size ds-override" })
                prezzi=prezzi.find_all("span",{"class":"product-price-text product-price-font-size ds-override" })
                #print("1",prezzi) 
                for i in range(0,len(prezzi)):
                    if i == 0 and len(prezzi)>1:
                        prezzo=prezzi[i].text
                        prezzo=re.findall(r'[\d\.]+',prezzo)
                        lista_prezzi.append(prezzo[0])
                    elif i==0 and len(prezzi)==1:
                        prezzo=prezzi[i].text
                        prezzo=re.findall(r'[\d\.]+',prezzo)
                        lista_prezzi.append(prezzo[0])
                        lista_sconti.append("Null")
                    elif i ==1:
                        sconto=prezzi[i].text
                        sconto=re.findall(r'[\d\.]+',sconto)
                        lista_sconti.append(sconto[0])

                
            except:
                #print("2",prezzi) 
                prezzo=html.find("div",{ "class":"product-price-v2"} )
                prezzo=prezzo.find("div",{"class": "product-price-v2__inner"})
                prezzo=prezzo.get("data-high-list-price")
                lista_prezzi.append(prezzo)
                lista_sconti.append("Null")           
    
    except:
        lista_sconti.append("Null")
        lista_prezzi.append("Null") 
        
    #----#
#.----------- fine PRIMO ARTICOLO    

    


    try:
        ul=html.find("ul",{"class":"tiles product-swatches"})
        li=ul.find_all("li")




        if len(li) >1 :
        
            for i in range(0,len(li)):
                #Ottenere la classe per la div del  radio button
                div=li[i].find("div")
                classe=div.get("class")
                classe=' '.join(classe)

                #Ottenere il contenuto dell'attributo value nella tag input
                val=li[i].find("input").get("value")


                #Grazie moltissime "undetected Selenium" per come cliccare i radio button , hanno dato molti problemi
                #https://stackoverflow.com/questions/62903056/elementclickinterceptedexception-message-element-click-intercepted-element-is
    
                if "default-swatch selected" in  classe:
                    continue 
        
                else:
                    try:
                        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='"+str(classe)+"']//input[@value='"+str(val)+"']"))))
                    except:
                        #per evitare i blocchi al colore di default
                        continue 

                #time.sleep(1)
                html_colore=driver.page_source
                html_colore=BeautifulSoup(html_colore,'html.parser')
    
        
                #ESTRARRE TITOLO
                try:        
                    titolo=html_colore.find("h1",{"class":"product-title-component product-title-main-header" })
                    lista_titoli.append(titolo.text)
                    #   print("Titolo",titolo.text)
                except:
                    lista_titoli.append("NULL")
                
                
                #ESTRARRE COLORE
                try:
                    color=html_colore.find("div",{"class":"js-product-attributes-inline"})
                    color=color.find("div",{"class":"product-page__swatches-attributes scope-1892"})
                    color=color.find("h3")    
                    colore=color.find("span").text
                    lista_colori.append(colore.upper())    
                    #  print("Colore",colore)
                except:
                    lista_colori.append("NULL")
    
                #ESTARRE I MATERIALI 
                try:
                    materiali=html_colore.find("div",{"class":"h4 fiber-content__label"})
                    materiale=materiali.text
                    lista_materiali.append(materiale)
                    #print("Materiale ottenuto",materiale)
                except: 
                    #Questa clausola è stata inserita perchè alcuni articoli non hanno la cella materiale
                    materiale="NULL"
                    lista_materiali.append(materiale)
                
                #ESTRARRE id 
                try:
                    idd=html_colore.find("p",{"class":"details__store-item-number text-small"})
                    idd=idd.find("span",{"class":"number"}).text.strip()
                    ID.append(idd)
                    
                except:
                    ID.append("Null")
                    
                    
                
                #Prezzo
                try:
                    try:
                        prezzi=html_colore.find("div",{"class":"product-price-v2"})
                        prezzi=prezzi.find("div",{"class" :"js-product-price"})
                        prezzi=prezzi.find("span",{"class","product-price-text-wrapper"})
                        prezzi=prezzi.find_all("span",{"class":"product-price-text product-price-font-size ds-override" })
                        for i in range(0,len(prezzi)):
                            if i == 0 and len(prezzi)>1:
                                prezzo=prezzi[i].text
                                prezzo=re.findall(r'[\d\.]+',prezzo)
                                lista_prezzi.append(prezzo[0])
                            elif i==0 and len(prezzi)==1:
                                prezzo=prezzi[i].text
                                prezzo=re.findall(r'[\d\.]+',prezzo)
                                lista_prezzi.append(prezzo[0])
                                lista_sconti.append("Null")
                            elif i ==1:
                                sconto=prezzi[i].text
                                sconto=re.findall(r'[\d\.]+',sconto)
                                lista_sconti.append(sconto[0])

                    except:
                            
                        try:
                            prezzo=html_colore.find("span",{"class","product-price-text-wrapper"})
                            prezzo=prezzo.find("span",{"class":"product-price-text product-price-font-size ds-override" })
                            prezzi=prezzi.find_all("span",{"class":"product-price-text product-price-font-size ds-override" })
                            for i in range(0,len(prezzi)):
                                if i == 0 and len(prezzi)>1:
                                    prezzo=prezzi[i].text
                                    prezzo=re.findall(r'[\d\.]+',prezzo)
                                    lista_prezzi.append(prezzo[0])
                                elif i==0 and len(prezzi)==1:
                                    prezzo=prezzi[i].text
                                    prezzo=re.findall(r'[\d\.]+',prezzo)
                                    lista_prezzi.append(prezzo[0])
                                    lista_sconti.append("Null")
                                elif i ==1:
                                    sconto=prezzi[i].text
                                    sconto=re.findall(r'[\d\.]+',sconto)
                                    lista_sconti.append(sconto[0])

                              
                            
                        except:
                            prezzo=html_colore.find("div",{ "class":"product-price-v2"} )
                            prezzo=prezzo.find("div",{"class": "product-price-v2__inner"})
                            prezzo=prezzo.get("data-high-list-price")
                            lista_prezzi.append(prezzo)
                            lista_sconti.append("Null")
                            
                                        
                
                except:
                    lista_sconti.append("Null")
                    lista_prezzi.append("Null") 
                    

    
           
            #  print(len(lista_materiali),len(lista_colori),len(lista_titoli ))
            # print(marca,prezzo)
    
        driver.quit()
        return lista_materiali,lista_colori, controllo_link,marca,lista_prezzi,lista_sconti, lista_titoli
    except:
        driver.quit()
        return lista_materiali,lista_colori, controllo_link,marca, lista_prezzi, lista_sconti, lista_titoli
      
      
#PER DEBUGGING

lista_prova=["a"]


#Caso un colore solo, con  un solo radio button, TEST PASSED
#link="https://www.hollisterco.com/shop/eu-it/gilly-hicks/p/gilly-hicks-scuba-hoodie-50390820-4?categoryId=85311&seq=01"

#Caso con più colori, con tanti radio button,   TEST PASSED
#link="https://www.hollisterco.com/shop/eu-it/p/t-shirt-sportiva-in-maglia-con-fondo-arrotondato-48481819?categoryId=85264&seq=04&faceout=prod1"

#Un colore solo, senza radio button, TEST PASSED
#link="https://www.hollisterco.com/shop/eu-it/gilly-hicks/p/tank-3-pack-47339819-4?categoryId=67671105&seq=01&faceout=prod1"

#Problema con estrazione del materiale,  RISOLUZIONE : mancava sul sito TEST PASSED
#link="https://www.hollisterco.com/shop/eu-it/p/jeggings-vita-alta-in-stretch-avanzato-40304487?categoryId=85306&seq=11"

#Social tourist
#link="https://www.hollisterco.com/shop/eu-it/social-tourist/p/social-tourist-double-waistband-sweatpants-48563322-4?categoryId=64790720&seq=01&faceout=prod1"

#Social tourist, più radio button 
#link="https://www.hollisterco.com/shop/eu-it/social-tourist/p/social-tourist-racer-top-49649819-4?categoryId=65014874&seq=01&faceout=prod1"


#SITO NON CHIUSO , RISOLUZIONE : driver.quit() mal indentato TEST PASSED
#link="https://www.hollisterco.com/shop/eu-it/social-tourist/p/social-tourist-shine-o-ring-bandeau-bikini-top-48032322-4?categoryId=122845&seq=01"


#SITO NON CHIUSO , RISOLUZIONE : driver.quit() mal indentato TEST PASSED
#link="https://www.hollisterco.com/shop/eu-it/p/top-bikini-a-fascia-multiposizione-allacciato-al-collo-45834319?categoryId=122845&seq=02"

#link='https://www.hollisterco.com/shop/eu-it/p/top-bikini-a-fascia-multiposizione-allacciato-al-collo-45834319?categoryId=122845&seq=02'
#link="https://www.hollisterco.com/shop/eu-it/p/logo-icon-crew-t-shirt-10-pack-47088320-4?categoryId=85359&seq=01"
#link="https://www.hollisterco.com/shop/eu-it/p/leggings-a-zampa-con-vita-ultra-alta-50691821?categoryId=166330&seq=01&faceout=prod1"

#link="https://www.hollisterco.com/shop/eu-it/p/super-skinny-chino-pants-48327337-4?categoryId=85286&seq=01"
link="https://www.hollisterco.com/shop/eu-it/p/maglietta-dad-vintage-oversize-con-stampa-50503321?categoryId=120705&seq=01"
print(estrazione_dati(link,lista_prova))










