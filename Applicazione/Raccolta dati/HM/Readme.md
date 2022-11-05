**In tutte le cartelle oltre i file .py sono stati inseriti anche dei file .ipynb per facilitare la comprensione.**  
# Installazione  
Per potere eseguire questi codici sul proprio computer deve essere eseguita l'installazione dei seguenti pacchetti :
- wget, https://pypi.org/project/wget/
- alive_progress, https://pypi.org/project/alive-progress/
- chrome driver, https://chromedriver.chromium.org/
- selenium, https://pypi.org/project/selenium/

# Capire il codice 
## Come è impostato?
È stata scelta una impostazione a **cicli for** annidati.  
Un altro metodo con il quale si sarebbe potuto procedere può essere trovato nella cartella **Script-tesi/Esempio-bonus**.  

### Struttura
Come già detto la struttura portante dello scraping è costituita da cicli for annidati.  
Per prima cosa si va ad iterare sul sesso.  Perciò si andranno ad estrarre prima tutte le categorie di vestiti da  donna.  
Per ogni categoria si andranno a prendere tutte le sottocategorie e per ogni sottocategoria tutti gli articoli appartenenti ad essa.  
Verrà tutto ripetuto per i vestiti da uomo.  
- Sesso
  - Categorie
     - Sottocategorie
        - Articoli
           - Registrazione dati 

#### Esempio di iterazione
- Donna 
    - T-shirt e canotte
        - Canotte  
              - Tutti gli articoli appartenenti alle canotte
