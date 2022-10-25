#Importazione pacchetti per selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time 

def scrollare_tutta_la_pagina():
    #Grazie Tech Path link al canale youtube : 'https://www.youtube.com/watch?v=qhJ_gMB772U'
    previous_height=driver.execute_script('return document.body.scrollHeight')
    while True:
        time.sleep(1)
        print("Loop")
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
        new_height=driver.execute_script('return document.body.scrollHeight')
        if new_height == previous_height :
            break
        previous_height = new_height
