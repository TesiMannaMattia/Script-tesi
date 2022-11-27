# -*- coding: utf-8 -*-
"""PuliziaHM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mgPR9l9D9PBZdvWN4akhrQkgVPr5mLDa

# Importazione pacchetti
"""

import pandas as pd
import re
import numpy as np
import os
import _string

"""# Importazione dati"""



df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati di prima modifica (NON MODIFICARE)/HM_rivisto.csv",
               delimiter=";")


"""## Eliminazione NA"""

df=df.dropna() 
df=df.reset_index() 


"""# Pulizia colori

### Altro
"""

#m=df["Colore"]
#a=m.drop_duplicates()
#a=a.dropna() 
#a=a.reset_index()

#a=a["Colore"].drop_duplicates()
#a=a.reset_index(drop=True)

"""## Liste colori"""



altro=['Blu acciaio scuro','VERDE E BLU NAVY', 'MARRONE-BIANCO', 'STAMPA ZEBRATA', 'BLU VIOLA CHIARO', 'MULTICOLORE A FIORI', 'BEIGE E NERO', 'Nude', 'MULTI DD', 'BLU NAVY - GRIGIO - BIANCO', 'Altro', 'MULTI', 'BLACK AND WHITE', 'NERO MARRONE CON STAMPA', 'Orange-red/Wisconsin', 'MULTICOLORE', 'BLU VIOLA', 'BIANCO - ROSSO - AZZURRO - SALVIA - NERO', 'BLU GRIGIO', 'WHITE-BLACK', 'Stampa', 'RIGHE MARRONI E ROSSE', 'NERO E ROSSO', 'NERO-BIANCO-GRIGIO', 'MULTI LOGO', 'SCOZZESE MULTI', 'Multicolor', 'BLU NAVY E BIANCO', 'MIX PRIDE', 'NERO E BORDEAUX', 'BIANCO-VERDE', 'BLU-GRIGIO-NERO', 'NERO E CORALLO', 'BLU E BIANCO', 'MIX BASIC', 'BIANCO E NERO', 'VIOLA GRIGIO', 'STAMPA MIMETICA', 'NERO - BIANCO', 'MULTI ICON', 'GRIGIO MÉLANGE E BIANCO', 'BLACK AND GREY', 'Bicolore', 'NERO E GRIGIO', 'Fantasia', 'BLACK AND GREEN', 'BIANCO - GRIGIO MÉLANGE - NEROBIANCHI CON RIGHE GRIGIE', 'STAMPA SCURA', '\tLAVAGGIO MEDIO STAMPATO', 'CHIARO', 'BIANCO - BLU NAVY - ROSSO - BORDEAUX - NERO', 'BLU NAVY-BIANCO-ROSSO', 'Verde-giallo', 'NERO E BIANCO', 'VIOLA BLU', 'ARANCIONE MARRONE', 'SCOZZESE BLU-GRIGIO', 'MULTI CREW', 'WHITE - LIGHT BLUE - GREY - RED - BLACK', 'Grigio chiaro mélange/fantasia', 'WHITE AND BLACK', 'TIE-DYE MULTICOLORE', 'Militare', 'BLACK-WHITE', 'BIANCO-GRIGIO-ROSA', 'NERO E GIALLO', 'MULTI RIGHE']
arancione=["Arancione bruciato","Arancione pallido","Arancione mélange","ARANCIONE SPEZIATO CON FIORI","CORALLO","CORALLO CON STAMPA","CORALLO ARANCIONE","ARANCIONE NEON","CORALLO CHIARO","ORANGE SPICE FLORAL","ARANCIONE BRUNITO","ARANCIONE SFUMATO","CORAL","LIGHT ORANGE","ARANCIONE A RIGHE","ARANCIONE CON MOTIVO","ARANCIONE SPEZIATO","ARANCIO","ARANCIONE CON STAMPA","ARANCIONE BRUNITO CON MOTIVO","Dark orange","Arancione ruggine","Arancione mélange","Light orange","Orange marl","Arancione fiamma","Corallo chiaro","Apricot","Corallo","Albicocca","Arancione scuro","Arancione brillante","Albicocca chiaro","Orange","Arancione chiaro","Arancione"]

beige=["Beige kaki","Beige-dye","Beige quadri","Beige marl","Beige argilla","Beige sabbia mélange","Beige mélange","Beige avena mélange","Beige chiaro mélange","Beige scuro mélange","Beige chiaro mélange","Beige scuro mélange","CAMEL","Beige Logo","BEIGE","Sabbia","Beigeélange","Beige-de-poule","Beige nocciola","Powder beige","Beige cipria","Beige avena chiaro","Beige sabbia mélange","Light beige marl","Beige chiaro","Beige scuro-de-poule","Dark beige marl","Beige chiaro-de-poule","Beige-patterned","Beige mélange","Dark beige","Beige avena mélange","Beige avena mèlange","Beige avena melange","Light beige","Beige scuro","Beige","Beige chiaro","Beige scuro mélange","Beige scuro melange","Beige scuro mèlange","Beige chiaro mélange","Beige chiaro melange","Beige chiaro mèlange"]

bianco=["Bianco/Coca-Cola","Bianco-Cola","Bianco-E","Bianco UP","Bianco/7 UP","Bianco/Coca-Cola","Bianco naturale mélange","Bianco mélange","BIANCO 6","BIANCO 1","BIANCO CON STRAPPI","BIANCO TIE-DYE","BIANCO A RIGHE DD","BIANCO DD","WHITE FLOWER PATTERN","BIANCO CON SCRITTA","WHITE TIE-DYE","OFF WHITE","BIANCO A FIORI","WHITE","Bianco Logo","Perla","Bianco Latte","Bianco Seta","PANNA","BIANCO CON ICONE","RIPPED WHITE","BIANCO DISTRUTTO","SCOZZESE BIANCO","BIANCO CON TEXTURE","BIANCO A QUADRI","BIANCO CON STAMPA","WHITE COLOR BLOCK","BIANCO FLOREALE","BIANCO WITH-TEXT","BIANCO SPORCO","BIANCO","MOTIVO BIANCO","BIANCO TESTURIZZATO","BIANCO A RIGHE","Bianco7 up","Biancoélange","Bianco","Bianco-cola","Bianco naturale mélange","Bianco mélange","White","Bianco-de-poule","Natural white","Bianco naturale","Bianco","White"]

blu=["Blu indaco chiaro","Blu Jerry","Azzurro cielo","Steel blue","Blu petrolio","Blu acciaio","Azzurro mélange","Blu mélange","SCOZZESE BLU NAVY","CHAMBRAY","BLU NAVY MÉLANGE CON LOGO BLU NAVY","LAVAGGIO BLU","LAVAGGIO BLU CHIARO","BLU NAVY A FIORI","BLU NAVY TIE-DYE","BLU NAVY A MICRO RIGHE","RIGHE BLU NAVY","BLU NAVY MELANGE","NAVY BLUE","BLUE STRIPE","LIGHT NAVY ICON","DARK TEAL ICON","NAVY PRINT","LIGHT BLUE","DARK TEAL","NAVY STRIPE","AZZURRO CON ICONE","AZZURRO A RIGHE","LIGHT BLUE PATTERN","DARK BLUE","BLUE","NAVY","Blu Navy Logo","Blu China Logo","Blu Navy Logo","Blu Logo","Blu Cina","BLU CHIARO","BLU MEDIO","Avio","Ghiaccio","AZZURO","Denim","Blu Elettrico","Acqua","Blu Cadetto","Blu Navy","Blu Notte","BLUE PRINT","MOTIVO BLU NAVY","BLU SHINE","BLU SCINTILLANTE","BLU NAVY CON STAMPA","AZZURRO CON STAMPA","SCOZZESE BLU","RINSE BLU SCURO", "BLU SCURO A FIORI","RINSE BLU","QUADRI BLU","LIGHT BLUE PRINT","BLU A FIORI","BLU A RIGHE","MOTIVO BLU","MOTIVO AZZURRO","AZZURRO A FIORI", "BLU CON STAMPA","BLU TIE-DYE","BLU","AZZURRO","BLU NAVY","BLU NAVY A RIGHE","BLU CHIARO A RIGHE","BLU SCURO","TINTURA AZZURRA","BLU NAVY FLOREALE","NAVY BLUE STRIPE","Light blue-patterned","Blue-patterned","Azzurro","Azzurroélange","Blu scuroélange","Pigeon blue","Blu denim chiarissimo","Dark denim blue","Denim blue","Pale denim blue","Blu medio","Blu notte","Light denim blue","Blu petrolio scuro","Bright blue","Blu cobalto","Azzurro mélange","Blu ghiaccio","Blu mélange","Denim blue","Blu denim pallido","Blu tortora","Navy blue","Dark blue marl","Light blue","Blue","Dark blue","Blu fiordaliso","Blu denim scuro","Azzurro","Blu denim","Blu scuro","Blu","Blu acceso","Blu navy","Blu denim chiaro"]

ciano=["Dark turquoise-dye","Light turquoise","MOTIVO TURCHESE","DARK TURQUOISE PATTERN","TURCHESE CON STAMPA","TURCHESE","Dark turquoise","Ciano","Turchese chiaro","Turchese","Turquoise","Turchese scuro"]

ecru=["Ecru chiaro"]

giallo=["Crema-Cola","Giallo-verde/fantasia","Giallo-verde","Crema/Coca-Cola","Mustard yellow","Giallo intenso","Crema/Coca-Cola","STAMPA CREMA","CREAM - CALIFORNIA","CREAM - ARIZONA","GIALLO A FIORI","CREMA - ARIZONA","CREMA - CALIFORNIA","QUADRI CREMA","YELLOW","Giallo Fluo","KAKI CHIARO","MOTIVO CREMA","ICONA CREMA","GIALLO FLOREALE","GIALLO CON MOTIVO","CREMA","CREAM","SCOZZESE CREMA","GIALLO","Crema'","Giallo neon","Giallo neon pallido","Crema","Crema-cola","Cream-patterned","Ocra","Dorato","Cream-dye","Giallo scuro","Yellow","Cream","Crema","Dark yellow","Light yellow","Giallo","Giallo senape","Giallo chiaro"]

grigio=["Silver-coloured/Glittery","Grigio-nero","Light grey marl/Portland","Grigio grafite","Grigiio","Grigio pietra","GrigioIG","Grigio acciaio","Grigio chiaro mélange/NYC","Grigio chiaro mélange/Topolino","Grigio chiaro mélange/Vermont","Grigio chiaro mélange/Disney","Grigio mélange/Coca-Cola","Grigio chiaro mélange/Malibu","Grigio chiaro mélange/Boston","Grigio mélange/Snoopy","Grigio mélange/Topolino","Grigio chiaro mélange/New York","Grigio chiaro mélange/Running","Grigio chiaro mélange/NFL","Grigio chiaro mélange/Harvard","Grigio chiaro mélange/Champs","Grigio chiaro mélange/Paris","Grigio chiaro mélange/Original","Grigio mélange/Love","Grigio chiaro mél/Lake Erie","Grigio mél/New York Jets","Grigio mélange/Harvard","Grigio scuro mélange/righe","Greige scuro mélange","Greige mélange","Grigio scuro mélange","Grigio mélange/Montana","Grigio mélange","Grigio chiaro mélange","Grigio chiaro mélange","SCOZZESE ARDESIA","MOTIVO GRIGIO CHIARO","MOTIVO ARDESIA","GRIGIO SLAVATO CON STRAPPI","GRIGIO SCURO DÉLAVÉ","GRIGIO CHIARO SLAVATO","GRIGIO SLAVATO","ARDESIA SCURO","GRIGIO MIMETICO","GRIGIO A QUADRI","GREY STRIPE","GRIGIO SCURO MÉLANGE","GRIGIO CON ICONE","GRIGIO A RIGHE","GRIGIO MÉLANGE","MED GREY FLAT","DARK GREY","HEATHER GREY","LAVAGGIO GRIGIO CON STRAPPI","Grigio Logo","Grafite","Taupe","Antracite","Tortora","Grigio Chiaro","Grigio Melange","Grigio Scuro","GRIGIO MEDIO UNIFORME","MOTIVO SCOZZESE GRIGIO SCURO","GRIGIO CON STAMPA","GRIGIO TIE-DYE","LAVAGGIO ACIDO GRIGIO CHIARO","SLATE","LAVAGGIO GRIGIO","LIGHT GREY SD/TEXTURE","GRIGIO CHIARO MÉLANGE","SCALA DI GRIGI","GRIGIO TALPA","GRIGIO","GRIGIO SCURO","GRIGIO MELANGE","GRIGIO CHIARO","GRIGIO SCURO CON TEXTURE","GREY PATTERN","Greige chiaro mélange","Grigio scuroélange","Argento","Light greige","Dark greige","Grigio scuro-de-poule","Dark denim grey","Grey","Denim grigio scuro","Denim grey","Grigio denim","Grigio denim scuro","Dark grey marl","Talpa chiaro","Grigio mélange-cola","Grigio chiaro mél","Grigio mél","Light grey-blue","Grey marl","Grigio ghiaccio","Light grey marl","Grigio antracite","Greige scuro mélange","Dark grey","Greige marl","Light grey","Greige mélange","Talpa scuro","Grigio scuro mélange","Grigio melange","Grigio mélange","Grigio mèlange","Talpa","Grigio fumo","Greige chiaro","Greige scuro","Greige","Grigio scuro","Argentato","Grigio chiaro","Grigio","Grigio chiaro melange","Grigio chiaro mélange","Grigio chiaro mèlange"]

marrone=["Marrone kaki","Marrone ruggineY","Terracotta","Marrone scuro mélange","Marrone mélange","MARRONE CHIARO MIMETICO","QUADRI MARRONI","MARRONE CHIARO SCOZZESE","MARRONE MIMETICO","BROWN SHINE","BROWN","BROWN PATTERN","DARK BROWN","TAUPE","LIGHT BROWN PLAID","DARK BROWN VEGAN LEATHER","LIGHT BROWN STRIPE","Ruggine","Cuoio","Fango","Tabacco","Testa Di Moro","Rigato","KAKI","MARRONE CON MOTIVO","MOTIVO MARRONE SCURO","MARRONE SCINTILLANTE","MARRONE CON STAMPA","MARRONE SCURO CON STAMPA","DARK BROWN FLORAL","BROWN PRINT","SCOZZESE MARRONE CHIARO","MARRONE CHIARO CON MOTIVO","SCOZZESE MARRONE SCURO","MARRONE CHIARO A RIGHE","SCOZZESE MARRONE","MARRONE SCURO A RIGHE","MARRONE CHIARO CON STAMPA","MARRONE SCURO DD","LIGHT BROWN","MARRONE SCURO","MARRONE CHIARO","CAMMELLO","RIGHE MARRONI","MARRONE","CLAY","MARRONE FLOREALE","Dark brown marl","Marrone scuroélange","Marrone scuro mélange","Rust brown","Marrrone","Marrone","Marrone quadri","Marrone ruggine","Marrone cioccolato","Light brown","Marrone mélange","Mole","Brown","Dark brown","Marrone scuro","Marrone","Marrone chiaro"]

nero=["Nero Jerry","Nero-Tang Clan","NeroYC","Nero sporco","Nero den","Nero-Cola","Nero/200 den","Nero/70 den","Nero/100 den","Nero/40 den","Nero/20 den","Nero/Coca-Cola","Nero mélange","NERO 1","NERO 3","NERO 8","NERO INALTERABILE","NERO CHE NON STINGE CON STRAPPI","NERO DÉLAVÉ CON STRAPPI","NERO CON STRAPPI E RAMMENDI","NERO SBIADITO","NERO TIE-DYE","NERO SLAVATO E DISTRUTTO","NERO CON BOTTONE MARRONE","MIMETICO NERO","NERO A RIGHE DD","NERO A RIGHE","NERO MÉLANGE","BLACK - WYOMING","BLACK - UTAH","BLACK","PERCALLE NERO","BLACK ICON","BLACK LOGO","NERO CON SCRITTA","NERO SFUMATO","NERO - UTAH","BLACK STRIPE","BLACK PATTERN","NERO A FIORI","BLACK WASH", "NERO CON BOTTONE NERO","MOTIVO NERO","PIEGATURA NERA","LAVAGGIO NERO CON STRAPPI","LAVAGGIO NERO",	"NERO SLAVATO CON STRAPPI","Nero Scuro","Nero Logo","Nero Profondo","RIPPED BLACK","NERO CON DUE BOTTONI","NERO CON STRAPPI","NERO DISTRUTTO","BLACK FLORAL","NERO CON MOTIVO","FADED BLACK","NERO SLAVATO","BLACK PLAID","NERO FLOREALE","NERO","NERO CON STAMPA","SCOZZESE NERO","NERO DÉLAVÉ","NERO DD","Nero1","Nero40 den","Nero20 den","Nero70 den","Nero100 den","Nero200 den","Denim nero","Nero-cola","Neroélange","Nero-de-poule","Nero mélange","Nero-block","Petrolio","Black-patterned","Nero","Black","Nero®"]

rosa=["PinkIG","Rosa chiaro/Très Jolie","Rosa chiaro mélange","ROSA CON MOTIVI","Rosa Cipria","Rosa Antico","ROSA SCURO CON MOTIVO","ROSA NEON","LIGHT PINK FLORAL","ROSA CON MOTIVO","ROSA CREMA","ROSA ACCESO","ROSA A RIGHE","ROSA A FIORI","ROSA FLOREALE","ROSA SCURO TIE-DYE","ROSA CON STAMPA","SCOZZESE ROSA","ROSA","ROSA SCURO","ROSA CHIARO","LIGHT PINK PRINT","PINK","Rosa nebbia chiaro","Rosa pallido","Rosa nebbia","Rosa cipria scuro","Rosa","Rosa chiaro","Rosaélange","Rosa chiaroélange","Rosa polvere","Rosa cipria chiaro","Powder pink","Rosa chiaroès jolie","Rosa pesca","Pink","Fucsia","Rosa chiaro mélange","Light pink-dye","Rosa scuro","Rosa antico scuro","Light pink","Old rose","Rosa acceso","Rosa chiaro","Rosa cipria","Rosa","Rosa antico"]

rosso=["Rossos favorite","Rosso-Cola","Rosso/Santa’s favorite","Rosso/Coca-Cola","Rosso/Coca-Cola","SCOZZESE ROSSO","ROSSO SLAVATO","RED","Rosso Logo","Borgogna","Fragola","MOTIVO ROSSO","ROSA HOT","ROSSO CON STAMPA","PAPRIKA","ROSSO DD","ROSSO","ROSSO TERRACOTTA","ROSSO PAPRIKA","Rosso's favorite","Rosso vivo","Rosso ruggine","Rosso fiammante","Cerise","Rosso scuro","Bright red","Ciliegia","Rosso","Rosso-cola","Rosso acceso","Red"]

verde=["Verde kaki","Verde scuro mélange","Sage green","Verde pistacchio chiaro","Verde kaki ch","Verde chiaro mélange","DARK OLIVE","OLIVA MELANGE","QUADRI SALVIA","LAVAGGIO SCURO VERDE OLIVA","DARK OLIVE","DARK GREEN","SALVIA CHIARO","KAKI CHIARO CON CORDONCINO NERO","KAKI SCURO","KAKI SCURO CON BOTTONE MARRONE","TWILL KAKI CHIARO","VERDE SALVIA SCURO","SALVIA A RIGHE","GREEN","OLIVE","OLIVA SCURO","GREEN","LIGHT GREEN PRINT","SAGE","OLIVA","Verde Logo","Verde acqua","Verde Chiaro","Bosco","VERDE CHIARO CON MOTIVO","MINT PATTERN","MOTIVO MINT","VERDE CHIARO SCINTILLANTE","VERDE SCINTILLANTE","VERDE CON STAMPA","MOTIVO VERDE","VERDE OLIVA SCINTILLANTE","VERDE NEON","VERDE FLOREALE","VERDE MINT","VERDE CHIARO FLOREALE","GREEN FLORAL","VERDE OLIVA DD","VERDE OLIVA MIMETICO","VERDE MENTA","VERDE OLIVA CHIARO","VERDE MINT A FIORI","NEON GREEN","VERDE CHIARO SCOZZESE","MENTA","VERDE OLIVA TIE-DYE","VERDE CHIARO CON STAMPA","VERDE CHIARO A FIORI","VERDE CHIARO","VERDE A RIGHE","VERDE","GREEN DD","VERDE LIME","VERDE SCURO","VERDE OLIVA SCURO","LIGHT GREEN","SALVIA","SCOZZESE VERDE","VERDE OLIVA FLOREALE","OLIVE GREEN","VERDE OLIVA","Verde mélange","Lime green","Light neon green","Verde kaki ch.","Bright green","Neon green","Verde mentaélange","Verde polvere chiaro","Verde nebbia","Light khaki green","Verde polvere","Verde menta chiaro","Verde chiaro pallido","Verde chiaro mélange","Verde-beige","Khaki green","Verde oliva scuro","Dark khaki green","Olive green","Verde nebbia chiaro","Verde neon chiaro","Verde muschio","Verde salvia","Verde neon","Dark green","Verde lime","Verde pistacchio","Verde-beige chiaro","Verde kaki chiaro","Verde giallognolo chiaro","Light green","Verde kaki scuro","Verde salvia chiaro","Verde salvia scuro","Verde kaki","Green","Verde chiaro","Verde acceso","Verde","Verde scuro","Verde menta","Verde oliva"]

viola=["Viola erica","Violaamicizia","Viola/Bracciali dell’amicizia","Viola scuro","Viola chiaro mélange","Viola mélange","Viola scuro/quadri","QUADRI VIOLA","SCOZZESE BORDEAUX","MOTIVO BORDEAUX","BORDEAUX MÉLANGE","MALVA SLAVATO","VIOLA SCURO","MALVA","BORDEAUX A RIGHE","MALVA CHIARO","BURGUNDY STRIPE","QUADRI BURDEAUX","PURPLE","VIOLA TIE-DYE","VIOLA CON MOTIVO","VIOLA CHIARO CON STAMPA","VIOLA","BORDEAUX","LIGHT PURPLE","BORDEAUX TIE-DYE","Plum purple","Malva","Malva chiaro","Viola'amicizia","Viola prugna scuro","Lavanda","Prugna","Viola chiaro mélange","Lilla","Erica chiaro","Purple","Light purple","Viola mélange","Viola prugna","Bordeaux scuro","Bordeaux","Viola pallido","Viola","Viola chiaro"]

da_stabilire=['LAVAGGIO MEDIO STAMPATOGREY AND WHITE', 'NAVY TO BLUE OMBRE', 'LIGHT DESTROYED WASH', 'LAVAGGIO CHIARO CON STRAPPI E RAMMENDI', 'A FIORI ARANCIONI', 'LAVAGGIO MEDIO A RIGHE', 'LAVAGGIO CHIARO ACCESO', 'CHIARO SBIADITO E FONDO SEMPLICE', 'SFUMATO DA ROSSO A NERO', 'Black-coloured', 'MEDIO DISTRUTTO', 'LAVAGGIO EXTRACHIARO CON STRAPPI', 'LAVAGGIO MEDIO', 'NERO SO CAL', 'Crema-Cola', 'LAVAGGIO CHIARO', 'DISTRUTTO SCURO', 'Blu Jerry', 'SFUMATO DA NERO A ROSA', 'LAVAGGIO MEDIO SCURO', 'LAVAGGIO CHIARO DISTRUTTO', 'LAVAGGIO SUPER CHIARO CON STRAPPI', 'NAVY WITH GREY STRIPE', 'LAVAGGIO CHIARO MEDIO', 'DARK RINSE', 'LAVAGGIO MEDIO CHIARO CON STRAPPI', 'LIGHT BROWN TO BLACK OMBRE', 'SFUMATO DA BIANCO A GRIGIO', 'DA NERO A SFUMATO VERDE CHIARO', 'LAVAGGIO MEDIO SCOLORITO', 'TEAL PATTERN', 'LAVAGGIO MEDIO ACCESO CON STRAPPI', 'BLACK TO BURGUNDY OMBRE', 'SCURO', 'LAVAGGIO MEDIO SCURO CON STRAPPI', 'LAVAGGIO CHIARO MEDIO STRAPPATO', 'SFUMATO DA NERO AD AZZURRO', 'DISTRUTTO SCURO CON FONDO SFRANGIATO', 'LAVAGGIO MEDIO ACCESO', 'LAVAGGIO MEDIO CON RAMMENDI', 'CHIARO DISTRUTTO', 'LAVAGGIO SCURO CON STRAPPI E RAMMENDI', 'LAVAGGIO MEDIO CON STRAPPI EFFETTO FLOREALE', 'LAVAGGIO MEDIO CHIARO', 'LAVAGGIO CHIARO CON STRAPPI', 'LAVAGGIO SCURO MEDIO', 'MEDIO CON RAMMENDI', 'NERO CON STRAPPI E RAMMENDI', 'GREY TO BLACK OMBRE', 'LIGHT RIPPED WASH', 'NERO SLAVATO - STEP BROTHERS', 'LAVAGGIO MEDIO CON STRAPPI SULLE GINOCCHIA', 'RINSE SCURO', 'DA AZZURRO A SFUMATO NERO', 'MEDIO', 'LAVAGGIO MEDIO CON STRAPPI SCURO', 'LAVAGGIO MEDIO STAMPATO', 'LAVAGGIO MEDIO CON STRAPPI', 'LAVAGGIO CHIARO CON VERNICE', 'CAMO', 'LAVAGGIO SCURO CON RAMMENDI', 'LAVAGGIO SCURO ACCESO', 'Silver-coloured', 'LAVAGGIO CHIARO ACCESO CON VERNICE', 'RINSE', 'SCURO CON STRAPPI', 'LAVAGGIO SCURO CON STRAPPI', 'SHREDDED DARK WASH', 'DA NERO A COLOR MENTA', 'DA NERO A BIANCO', 'LIGHT WASH WITH BLEACH', 'EFFETTO GRIGIO EFFETTO TINTURA', 'NERO SLAVATO - STEP BROTHER', 'SFUMATO DA GRIGIO SCURO A NERO', 'DARK RIPPED WASH', 'MEDIA', 'LAVAGGIO CHIARO ACCESO CON STRAPPI', 'WHITE WITH TAN STRIPE', 'EFFETTO LAVAGGIO CHIARO', 'BACCA', 'LAVAGGIO SCURO', 'SFUMATO DA NERO A BIANCO', 'BLACK TO WHITE OMBRE', 'SFUMATO DA BLU A NERO', 'DARK PINK ICON', 'RINSE LEGGERMENTE STRAPPATI', 'LAVAGGIO MEDIO DISTRUTTO', 'LAVAGGIO MEDIO CON CINTURA', 'LAVAGGIO SUPER CHIARO', 'DISTRUTTO CHIARO']
"""## Pulizia"""
n=0
assenti=[]
altroo=[]
da_stabilire=[]
n_da_stabilire=0
n_altro=0
n_da_eliminare=0
for i in range(0,len(df)):
  m=re.sub(r"/[\s è é a-zA-Z]*","",df["Colore"][i])
 
  m=re.sub(r"[^a-zA-Z  è é \- \s]*","",m)
 
  m=m.strip()

  if m in arancione:
    df["Colore"][i]="Arancione"
  elif m in beige :
    df["Colore"][i]="Beige"
  elif m in  bianco :
    df["Colore"][i]="Bianco"
  elif m in blu:
    df["Colore"][i]="Blu"
  elif m in ciano:
    df["Colore"][i]="Ciano"
  elif m in ecru:
    df["Colore"][i]="Ecru"
  elif m in giallo:
    df["Colore"][i]="Giallo"
  elif m in grigio:
    df["Colore"][i]="Grigio"
  elif m in marrone:
    df["Colore"][i]="Marrone"
  elif m in nero:
    df["Colore"][i]="Nero"
  elif m in rosa:
    df["Colore"][i]="Rosa"
  elif m in rosso:
    df["Colore"][i]="Rosso"
  elif m in verde:
    df["Colore"][i]="Verde"
  elif m in viola:
    df["Colore"][i]="Viola"
  elif m in da_stabilire:
    df["Colore"][i]="Da_stabilire"
    n_da_stabilire += 1
    da_stabilire.append(m)
  elif m in altro:
    df["Colore"][i]="Altro"
    n_altro +=1 
    altroo.append(m)
        
  else:
    #Per avere in output su formato txt i colori non inseriti in nessuna sotto categoria e decidere meglio il da farsi  
    #Questa parte verrà poi inibita nelle fasi finali.
    n_da_eliminare += 1
    if m not in assenti :
        assenti.append(m)  
        n+= 1 
        with open("/Users/mattia/Desktop/riepilogo_colori_HM.txt","a") as f:
            f.write(str(n)+"  "+"'"+str(m.strip())+"',")
            f.write("\n")
    df=df.drop(i)
    
    
with open("/Users/mattia/Desktop/riepilogo_colori_HM.txt","a") as f:
    f.write("\n\n")
    f.write("Riepilogo : \n")
    f.write("Numero di  articoli eliminati perchè con colori non identificabili:  "+str(n_da_eliminare))
    f.write("\n")
    f.write("Numero di colori da stabilire:  "+str(n_da_stabilire))
    f.write("\n")
    f.write("Articoli catalogati come altro: "+str(n_altro)) 
    for i in da_stabilire:
        f.write(str(i)+"\n")
    f.write("\n\n\n\n")
    for j in altroo:
         f.write(str(j)+"\n")




"""# Pulizia Materiali

## Settings
"""
df=df.reset_index(drop=True)      #si devono rimettere gli indici perchè alcune righe che presentano colori ambigui verranno eliminate



m=df["Materiali"]

"""## Pulizia effettiva"""

dataset = pd.DataFrame({'A' : []})
for i in range(0,len(m)):
  if m[i]=="Null":
    #print("Eliminato")
    df=df.drop(i) #eliminare le righe che non hanno materiale
    continue 

  k=re.sub("[a-zA-Z\s]*:","",m[i]) #Restituisce solo i materiali con la corrispettiva percentuale
  #n=re.sub("[0-9%]*","",k)
  ma=re.findall(r"[a-zA-Z \s]{2,}",k)

  df["Prezzo"][i]=df.loc[i].Prezzo.replace(",",".")   

  for j in range(0,len(ma)):
    ma[j]=ma[j].strip().capitalize()  #toglie spazi iniziali e finali e mette prima lettera maiuscola e resto tutto minuscolo
    ma[j]=re.sub("[\s]","_",ma[j])    #Se una parola è doppia toglie lo spazio ed unisce con un trattino le due parole
    
    if ma[j]=="Poliestere_riciclato" or ma[j]=="Fibre_di_poliestere_riciclato":
        ma[j]="Poliestere"
    
    elif ma[j]=="Cotone_biologico" or  ma[j]=="Cotton":
        ma[j]="Cotone"
    
    elif ma[j]=="Lana_riciclata" or  ma[j]=="Lana_di_yak" or ma[j]=="Yak_wool" or  ma[j]=="Wool" or  ma[j]=="Virgin_wool" or ma[j]=="Mohair_wool"or ma[j]=="Lana_di_alpaca" or ma[j]=="Lana_di_angora" or ma[j]=="Lana_mohair" or ma[j]=="Lana_rigenerata" or  ma[j]=="Lana_vergine" or	ma[j]=="Lana_merinos" or ma[j]=="Angora_wool" or ma[j]=="Alpaca_wool" or ma[j]=="Camel_wool" or ma[j]=="Lana_merinos":
        ma[j]="Lana"
 
    elif ma[j]=="Copoliestere" or ma[j]=="Polyester":
        ma[j]="Poliestere"
    
    elif ma[j]=="Poliuretano_termoplastico":
        ma[j]="Poliuretano"
        
    elif ma[j]=="Modacrilico":
        ma[j]="Modacrilica"
    
    
    elif ma[j]=="Rayon" or ma[j]=="Viscose" or ma[j]=="Modal":
        ma[j]="Viscosa"
    
    elif ma[j]=="Cachemire" or ma[j]=="Goat_hair":
        ma[j]="Cashmere"
      
    elif ma[j]=="Polyamide" or  ma[j]=="Polyimide":
        ma[j]="Poliammide"
      
    elif ma[j]=="Acrylic" or ma[j]=="Acetate":
        ma[j]="Acetato"
    

    elif ma[j]=="Seta_di_gelso" or ma[j]=="Seta_tussah" or ma[j]=="Silk":
        ma[j]="Seta"
 
    elif ma[j]=="Elastane":
        ma[j]="Elastan"
      
    elif ma[j]=="Elastomultiester":
        ma[j]="Elastomultiestere"
      
    elif ma[j]=="Cuoio" or ma[j]=="Calf" or  ma[j]=="Bovine_leather" or  ma[j]=="Goat_skin"or ma[j]=="Skin_leather" or ma[j]=="Lambskin" or ma[j]=="Pelle_di_agnello" or ma[j]=="Pelle_di_bovino":
        ma[j]="Pelle"
     
    elif ma[j]=="Linen":
        ma[j]="Lino"
        
    elif ma[j]=="Metallic_fibre" or ma[j]=="Metallica" or  ma[j]=="Fibra_metallizzata" :
        ma[j]="Fibra_di_metallo"
        
    elif ma[j]=="Piuma_d" or ma[j]=="Piumino_d" or ma[j]=="Oca" or ma[j]=="Piumino":
        ma[j]="Piuma"
        
    elif ma[j]=="Pvc":
        ma[j]="Polivinilcloruro"
    elif ma[j]=="poliuretano" or ma[j]=="Poliuretanica" or  ma[j]=="Polyurethane" or ma[j]=="Polyurethane_coated":
        ma[j]="Poliuretano"
    
    elif ma[j]=="Triacetate":
        ma[j]="Triacetato"
        
    elif ma[j]=="Other_fibres"or ma[j]=="Fibre_non_specificate":
        ma[j]="Altre_fibre"


      
  ma = list(dict.fromkeys(ma))        #Rimozione di eventuali materiali che compaiono più volte in diverse classi.

  vettore_uni=np.ones(len(ma))        #Vettori di uno per i materiali presenti 
  
  vettore_uni.astype(int)             #Togliere decimali dagli uno, nota: non sembra funzionare.
  
  riga= pd.DataFrame([vettore_uni], columns=ma)        #Crea la riga 
  
  dataset=pd.concat([dataset, riga])   



################## ################### ################### ################### ################### 
df=df.reset_index(drop=True)    #si devono rimettere gli indici perchè alcune righe che presentano colori ambigui verranno eliminate
#LAVORARE SUL DATASET PANDAS CREATO

#Sostituzione degli na con degli zeri (0).
dataset=dataset.fillna(0) 

#Rimozione colonna inutile
dataset.drop(["A"], inplace=True, axis=1)

#Aggiustamento indici
dataset=dataset.reset_index()

#ORDINARE IL DATASET PER COLONNA :
dataset = dataset.reindex(sorted(dataset.columns), axis=1)  

c=list(dataset.columns)

c.remove("index")

#Creazione della colonna che fornisce il numero di fibre presenti nel vestito.
dataset['N_Fibre_Differenti'] = dataset.sum(axis=1)
#dataset.N_Fibre_Differenti.astype(int)



#Rimozione colonna inutile
dataset.drop(["index"], inplace=True, axis=1)
dati=pd.concat([df, dataset], axis=1) #non ha senso farlo perchè il dataset in input non è corretto

#Rimozione colonna inutile
try:
    dati.drop(["Unnamed: 0","...1"], inplace=True, axis=1)
except:
    pass
try:
    dati.drop(["level_0"], inplace=True, axis=1)
except:
    pass

a=["Materiali"]
a.extend(c)
a.append("N_Fibre_Differenti")

""" # Esportazione dati"""
#dati.to_csv("/Users/mattia/desktop/pulito_HM.csv",columns=a)


#Da eseguire una volta finita tutta la ricerca di ALTRO e DA stabilire
dati.to_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_HM.csv")






