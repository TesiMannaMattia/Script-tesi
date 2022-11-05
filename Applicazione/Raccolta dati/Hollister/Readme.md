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
- Uomo
    - TOPWEAR
        - T-shirt & Maglie serafino
              - Tutti gli articoli appartenenti a -shirt & Maglie serafino
              
## Analisi dei singoli script

### 1) main.py/main.ipynb
Come suggerisce il titolo questo è lo script principale.  
In questo script viene definita tutta la struttura appena descritta e vengono richiamate tutte le altre funzioni.  

### 2) estrazioneprodotti.py/estrazioneprodotti.ipynb
Estrare tutte le categorie di vestiti di un sesso.

### 3) estrazione_sottocategorie.py/estrazione_sottocategorie.ipynb
Estrare tutte le sottocategorie di una categoria.

### 4) cambiopagina.y/cambiopagina.ipynb
Prende tutti gli html delle eventuali n pagine della sottocategoria

### 5) estrazionearticoli.py/estrazionearticoli.ipynb
Estrae  i link di ogni singolo articolo dagli html trovanti nella funzione precedente.

### 6) estrazionedati.py/estrazionedati.ipynb
Estrae  dati dall'html estratto nella funzione apri_pagina.py.
