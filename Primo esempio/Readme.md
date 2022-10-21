Si prenda in considerazione un primo esempio basilare, si estraggano i primi venti txt file di dati  dal seguente sito : 
\url{http://web.mta.info/developers/turnstile.html}
I file txt da estrarre dalla pagina (Figura 5) sono contenuti nei link indicati dalla parentesi graffa, come procedere?
Per prima cosa si otterrà tramite il comando \textit{requests.get("link della pagina")} 
l'html della pagina, successivamente si andranno ad estrarre i 20 link contenuti nelle tag di tipo $<$\textbf{a}$>$.
Una volta estratti i 20 link, per ognuno di essi si andrà di nuovo tramite il comando \textit{requests.get} a richiedere e salvare l'html della pagina, tuttavvia essendo pagine in formato txt si avranno direttamente i dati voluti senza bisogno di effettuare altre operazioni.
A questo punto si salveranno i dati nel formato interessato.
