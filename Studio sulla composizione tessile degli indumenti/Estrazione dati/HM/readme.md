
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
              
## Analisi dei singoli script

### 1) mainHM.py/mainHM.ipynb
Come suggerisce il titolo questo è lo script principale.  
In questo script viene definita tutta la struttura appena descritta e vengono richiamate tutte le altre funzioni.  

### 2) estrazione_categorie.py/estrazione_categorie.ipynb
Estrare tutte le categorie di vestiti di un sesso.
### 3) estrazione_sottocategorie.py/estrazione_sottocategorie.ipynb
Estrare tutte le sottocategorie di una categoria.
### 4) estrazione_articoli.py/estrazione_articoli.ipynb
Estrare tutti i link degli articoli di una sottocategoria. 
### 5) apri_pagina.py/apri_pagina.ipynb
Per ogni link estratto nella funzione precedente apre la pagina ad esso associata.  
Una volta aperta la pagina accetta i cookie e la scrolla per far caricare tutto l'html. 
### 6) estrazione_dati.py/estrazione_dati.ipynb
Estrae  dati dall'html estratto nella funzione precedente. 
### 7) estrai_attributi.py/estrai_attributi.ipynb
Estrae  dati dall'html estratto nella funzione apri_pagina.py.
