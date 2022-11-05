**Oltre i file .py sono stati inseriti anche dei file .ipynb per facilitare la comprensione.**
Capita che i  dati ottenuti tramite web scraping non siano subito utilizzabili e vadano quindi puliti.  
Altre volte capita che anche se siano stati estratti correttamente i dati non siano direttamente adatti a ciò che bisogna fare e quindi vanno comunque rivisti.  
Per pulire i dati viene utilizzata la sintassi **regex** oltre alla ovvia **pandas**.  

Per quanto riguarda i due dataset, HM ed Hollister, la pulizia è stata effettuata solo su due variabili **Materiali, Colori**.  
Per quanto riguarda i materiali i dati grezzi si presentavano in formato : Cotone 59%, Poliestere 41%.
Ciò che è stato fatto è stato creare una nuova variabile binaria per ogni materiale, 0 se era presente, 1 se non lo era.  

Per i materiali si è cercato di ricollegare tutti i colori più particolari a quelli più generici, ad esempio corallo viene codificato come arancione.  







