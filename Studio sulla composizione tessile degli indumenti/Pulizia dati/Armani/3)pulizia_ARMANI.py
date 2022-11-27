import pandas as pd
import re
import numpy as np

#df = pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati grezzi (NON MODIFICARE!)/ARMANI.csv")
df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati di prima modifica (NON MODIFICARE)/ARMANI_rivisto.csv",
               delimiter=";")



try:      
    df = df.drop('Unnamed: 0', axis=1)
except:
    pass

try:
    df = df.drop('Unnamed: 0.1', axis=1)
except:
    pass
try:
    df = df.drop('Valuta', axis=1)
except:
    pass

"""## Liste colori"""

altro=["Altro","Silver-coloured/Glittery",'VIOLA GRIGIO','VERDE E BLU NAVY','MARRONE-BIANCO','STAMPA ZEBRATA','BLU VIOLA CHIARO','MULTICOLORE A FIORI','STAMPA MIMETICA','NERO - BIANCO','BEIGE E NERO','Nude','MULTI ICON','GRIGIO MÉLANGE E BIANCO','BLACK AND GREY','MULTI DD','BLU NAVY - GRIGIO - BIANCO','MULTI','Bicolore','NERO E GRIGIO','Fantasia','BLACK AND WHITE','BLACK AND GREEN','NERO MARRONE CON STAMPA','BIANCO - GRIGIO MÉLANGE - NERO''BIANCHI CON RIGHE GRIGIE','STAMPA SCURA','\tLAVAGGIO MEDIO STAMPATO','LAVAGGIO MEDIO STAMPATO''GREY AND WHITE','MULTICOLORE','BLU VIOLA','CHIARO','BIANCO - ROSSO - AZZURRO - SALVIA - NERO','BIANCO - BLU NAVY - ROSSO - BORDEAUX - NERO','BLU NAVY-BIANCO-ROSSO','BLU GRIGIO','WHITE-BLACK','Stampa','RIGHE MARRONI E ROSSE','NERO E BIANCO','NERO E ROSSO','NERO-BIANCO-GRIGIO','VIOLA BLU','ARANCIONE MARRONE','SCOZZESE BLU-GRIGIO','MULTI CREW','WHITE - LIGHT BLUE - GREY - RED - BLACK','WHITE AND BLACK','MULTI LOGO','TIE-DYE MULTICOLORE','SCOZZESE MULTI','Militare','Multicolor','BLACK-WHITE','BLU NAVY E BIANCO','MIX PRIDE','NERO E BORDEAUX','BIANCO-VERDE','BLU-GRIGIO-NERO','BIANCO-GRIGIO-ROSA','NERO E CORALLO','BLU E BIANCO','NERO E GIALLO','MIX BASIC','BIANCO E NERO','MULTI RIGHE',"Giallo-verde"]

arancione=["ARANCIONE SPEZIATO CON FIORI","CORALLO","CORALLO CON STAMPA","CORALLO ARANCIONE","ARANCIONE NEON","CORALLO CHIARO","ORANGE SPICE FLORAL","ARANCIONE BRUNITO","ARANCIONE SFUMATO","CORAL","LIGHT ORANGE","ARANCIONE A RIGHE","ARANCIONE CON MOTIVO","ARANCIONE SPEZIATO","ARANCIO","ARANCIONE CON STAMPA","ARANCIONE BRUNITO CON MOTIVO","Dark orange","Arancione ruggine","Arancione mélange","Light orange","Orange marl","Arancione fiamma","Corallo chiaro","Apricot","Corallo","Albicocca","Arancione scuro","Arancione brillante","Albicocca chiaro","Orange","Arancione chiaro","Arancione"]

beige=["Beige chiaro mélange","Beige scuro mélange","CAMEL","Beige Logo","BEIGE","Sabbia","Beigeélange","Beige-de-poule","Beige nocciola","Powder beige","Beige cipria","Beige avena chiaro","Beige sabbia mélange","Light beige marl","Beige chiaro","Beige scuro-de-poule","Dark beige marl","Beige chiaro-de-poule","Beige-patterned","Beige mélange","Dark beige","Beige avena mélange","Beige avena mèlange","Beige avena melange","Light beige","Beige scuro","Beige","Beige chiaro","Beige scuro mélange","Beige scuro melange","Beige scuro mèlange","Beige chiaro mélange","Beige chiaro melange","Beige chiaro mèlange"]

bianco=["BIANCO 6","BIANCO 1","BIANCO CON STRAPPI","BIANCO TIE-DYE","BIANCO A RIGHE DD","BIANCO DD","WHITE FLOWER PATTERN","BIANCO CON SCRITTA","WHITE TIE-DYE","OFF WHITE","BIANCO A FIORI","WHITE","Bianco Logo","Perla","Bianco Latte","Bianco Seta","PANNA","BIANCO CON ICONE","RIPPED WHITE","BIANCO DISTRUTTO","SCOZZESE BIANCO","BIANCO CON TEXTURE","BIANCO A QUADRI","BIANCO CON STAMPA","WHITE COLOR BLOCK","BIANCO FLOREALE","BIANCO WITH-TEXT","BIANCO SPORCO","BIANCO","MOTIVO BIANCO","BIANCO TESTURIZZATO","BIANCO A RIGHE","Bianco7 up","Biancoélange","Bianco","Bianco-cola","Bianco naturale mélange","Bianco mélange","White","Bianco-de-poule","Natural white","Bianco naturale","Bianco","White"]

blu=["SCOZZESE BLU NAVY","CHAMBRAY","BLU NAVY MÉLANGE CON LOGO BLU NAVY","LAVAGGIO BLU","LAVAGGIO BLU CHIARO","BLU NAVY A FIORI","BLU NAVY TIE-DYE","BLU NAVY A MICRO RIGHE","RIGHE BLU NAVY","BLU NAVY MELANGE","NAVY BLUE","BLUE STRIPE","LIGHT NAVY ICON","DARK TEAL ICON","NAVY PRINT","LIGHT BLUE","DARK TEAL","NAVY STRIPE","AZZURRO CON ICONE","AZZURRO A RIGHE","LIGHT BLUE PATTERN","DARK BLUE","BLUE","NAVY","Blu Navy Logo","Blu China Logo","Blu Navy Logo","Blu Logo","Blu Cina","BLU CHIARO","BLU MEDIO","Avio","Ghiaccio","AZZURO","Denim","Blu Elettrico","Acqua","Blu Cadetto","Blu Navy","Blu Notte","BLUE PRINT","MOTIVO BLU NAVY","BLU SHINE","BLU SCINTILLANTE","BLU NAVY CON STAMPA","AZZURRO CON STAMPA","SCOZZESE BLU","RINSE BLU SCURO", "BLU SCURO A FIORI","RINSE BLU","QUADRI BLU","LIGHT BLUE PRINT","BLU A FIORI","BLU A RIGHE","MOTIVO BLU","MOTIVO AZZURRO","AZZURRO A FIORI", "BLU CON STAMPA","BLU TIE-DYE","BLU","AZZURRO","BLU NAVY","BLU NAVY A RIGHE","BLU CHIARO A RIGHE","BLU SCURO","TINTURA AZZURRA","BLU NAVY FLOREALE","NAVY BLUE STRIPE","Light blue-patterned","Blue-patterned","Azzurro","Azzurroélange","Blu scuroélange","Pigeon blue","Blu denim chiarissimo","Dark denim blue","Denim blue","Pale denim blue","Blu medio","Blu notte","Light denim blue","Blu petrolio scuro","Bright blue","Blu cobalto","Azzurro mélange","Blu ghiaccio","Blu mélange","Denim blue","Blu denim pallido","Blu tortora","Navy blue","Dark blue marl","Light blue","Blue","Dark blue","Blu fiordaliso","Blu denim scuro","Azzurro","Blu denim","Blu scuro","Blu","Blu acceso","Blu navy","Blu denim chiaro"]

ciano=[" MOTIVO TURCHESE","DARK TURQUOISE PATTERN","TURCHESE CON STAMPA","TURCHESE","Dark turquoise","Ciano","Turchese chiaro","Turchese","Turquoise","Turchese scuro"]

ecru=["Ecru chiaro"]

giallo=["STAMPA CREMA","CREAM - CALIFORNIA","CREAM - ARIZONA","GIALLO A FIORI","CREMA - ARIZONA","CREMA - CALIFORNIA","QUADRI CREMA","YELLOW","Giallo Fluo","KAKI CHIARO","MOTIVO CREMA","ICONA CREMA","GIALLO FLOREALE","GIALLO CON MOTIVO","CREMA","CREAM","SCOZZESE CREMA","GIALLO","Crema'","Giallo neon","Giallo neon pallido","Crema","Crema-cola","Cream-patterned","Ocra","Dorato","Cream-dye","Giallo scuro","Yellow","Cream","Crema","Dark yellow","Light yellow","Giallo","Giallo senape","Giallo chiaro"]

grigio=["Grigio chiaro mélange","SCOZZESE ARDESIA","MOTIVO GRIGIO CHIARO","MOTIVO ARDESIA","GRIGIO SLAVATO CON STRAPPI","GRIGIO SCURO DÉLAVÉ","GRIGIO CHIARO SLAVATO","GRIGIO SLAVATO","ARDESIA SCURO","GRIGIO MIMETICO","GRIGIO A QUADRI","GREY STRIPE","GRIGIO SCURO MÉLANGE","GRIGIO CON ICONE","GRIGIO A RIGHE","GRIGIO MÉLANGE","MED GREY FLAT","DARK GREY","HEATHER GREY","LAVAGGIO GRIGIO CON STRAPPI","Grigio Logo","Grafite","Taupe","Antracite","Tortora","Grigio Chiaro","Grigio Melange","Grigio Scuro","GRIGIO MEDIO UNIFORME","MOTIVO SCOZZESE GRIGIO SCURO","GRIGIO CON STAMPA","GRIGIO TIE-DYE","LAVAGGIO ACIDO GRIGIO CHIARO","SLATE","LAVAGGIO GRIGIO","LIGHT GREY SD/TEXTURE","GRIGIO CHIARO MÉLANGE","SCALA DI GRIGI","GRIGIO TALPA","GRIGIO","GRIGIO SCURO","GRIGIO MELANGE","GRIGIO CHIARO","GRIGIO SCURO CON TEXTURE","GREY PATTERN","Greige chiaro mélange","Grigio scuroélange","Argento","Light greige","Dark greige","Grigio scuro-de-poule","Dark denim grey","Grey","Denim grigio scuro","Denim grey","Grigio denim","Grigio denim scuro","Dark grey marl","Talpa chiaro","Grigio mélange-cola","Grigio chiaro mél","Grigio mél","Light grey-blue","Grey marl","Grigio ghiaccio","Light grey marl","Grigio antracite","Greige scuro mélange","Dark grey","Greige marl","Light grey","Greige mélange","Talpa scuro","Grigio scuro mélange","Grigio melange","Grigio mélange","Grigio mèlange","Talpa","Grigio fumo","Greige chiaro","Greige scuro","Greige","Grigio scuro","Argentato","Grigio chiaro","Grigio","Grigio chiaro melange","Grigio chiaro mélange","Grigio chiaro mèlange"]

marrone=["MARRONE CHIARO MIMETICO","QUADRI MARRONI","MARRONE CHIARO SCOZZESE","MARRONE MIMETICO","BROWN SHINE","BROWN","BROWN PATTERN","DARK BROWN","TAUPE","LIGHT BROWN PLAID","DARK BROWN VEGAN LEATHER","LIGHT BROWN STRIPE","Ruggine","Cuoio","Fango","Tabacco","Testa Di Moro","Rigato","KAKI","MARRONE CON MOTIVO","MOTIVO MARRONE SCURO","MARRONE SCINTILLANTE","MARRONE CON STAMPA","MARRONE SCURO CON STAMPA","DARK BROWN FLORAL","BROWN PRINT","SCOZZESE MARRONE CHIARO","MARRONE CHIARO CON MOTIVO","SCOZZESE MARRONE SCURO","MARRONE CHIARO A RIGHE","SCOZZESE MARRONE","MARRONE SCURO A RIGHE","MARRONE CHIARO CON STAMPA","MARRONE SCURO DD","LIGHT BROWN","MARRONE SCURO","MARRONE CHIARO","CAMMELLO","RIGHE MARRONI","MARRONE","CLAY","MARRONE FLOREALE","Dark brown marl","Marrone scuroélange","Marrone scuro mélange","Rust brown","Marrrone","Marrone","Marrone quadri","Marrone ruggine","Marrone cioccolato","Light brown","Marrone mélange","Mole","Brown","Dark brown","Marrone scuro","Marrone","Marrone chiaro"]

nero=["NERO 1","NERO 3","NERO 8","NERO INALTERABILE","NERO CHE NON STINGE CON STRAPPI","NERO DÉLAVÉ CON STRAPPI","NERO CON STRAPPI E RAMMENDI","NERO SBIADITO","NERO TIE-DYE","NERO SLAVATO E DISTRUTTO","NERO CON BOTTONE MARRONE","MIMETICO NERO","NERO A RIGHE DD","NERO A RIGHE","NERO MÉLANGE","BLACK - WYOMING","BLACK - UTAH","BLACK","PERCALLE NERO","BLACK ICON","BLACK LOGO","NERO CON SCRITTA","NERO SFUMATO","NERO - UTAH","BLACK STRIPE","BLACK PATTERN","NERO A FIORI","BLACK WASH", "NERO CON BOTTONE NERO","MOTIVO NERO","PIEGATURA NERA","LAVAGGIO NERO CON STRAPPI","LAVAGGIO NERO",	"NERO SLAVATO CON STRAPPI","Nero Scuro","Nero Logo","Nero Profondo","RIPPED BLACK","NERO CON DUE BOTTONI","NERO CON STRAPPI","NERO DISTRUTTO","BLACK FLORAL","NERO CON MOTIVO","FADED BLACK","NERO SLAVATO","BLACK PLAID","NERO FLOREALE","NERO","NERO CON STAMPA","SCOZZESE NERO","NERO DÉLAVÉ","NERO DD","Nero1","Nero40 den","Nero20 den","Nero70 den","Nero100 den","Nero200 den","Denim nero","Nero-cola","Neroélange","Nero-de-poule","Nero mélange","Nero-block","Petrolio","Black-patterned","Nero","Black","Nero®"]

rosa=["ROSA CON MOTIVI","Rosa Cipria","Rosa Antico","ROSA SCURO CON MOTIVO","ROSA NEON","LIGHT PINK FLORAL","ROSA CON MOTIVO","ROSA CREMA","ROSA ACCESO","ROSA A RIGHE","ROSA A FIORI","ROSA FLOREALE","ROSA SCURO TIE-DYE","ROSA CON STAMPA","SCOZZESE ROSA","ROSA","ROSA SCURO","ROSA CHIARO","LIGHT PINK PRINT","PINK","Rosa nebbia chiaro","Rosa pallido","Rosa nebbia","Rosa cipria scuro","Rosa","Rosa chiaro","Rosaélange","Rosa chiaroélange","Rosa polvere","Rosa cipria chiaro","Powder pink","Rosa chiaroès jolie","Rosa pesca","Pink","Fucsia","Rosa chiaro mélange","Light pink-dye","Rosa scuro","Rosa antico scuro","Light pink","Old rose","Rosa acceso","Rosa chiaro","Rosa cipria","Rosa","Rosa antico"]

rosso=["Rosso/Coca-Cola","SCOZZESE ROSSO","ROSSO SLAVATO","RED","Rosso Logo","Borgogna","Fragola","MOTIVO ROSSO","ROSA HOT","ROSSO CON STAMPA","PAPRIKA","ROSSO DD","ROSSO","ROSSO TERRACOTTA","ROSSO PAPRIKA","Rosso's favorite","Rosso vivo","Rosso ruggine","Rosso fiammante","Cerise","Rosso scuro","Bright red","Ciliegia","Rosso","Rosso-cola","Rosso acceso","Red"]

verde=["DARK OLIVE","OLIVA MELANGE","QUADRI SALVIA","LAVAGGIO SCURO VERDE OLIVA","DARK OLIVE","DARK GREEN","SALVIA CHIARO","KAKI CHIARO CON CORDONCINO NERO","KAKI SCURO","KAKI SCURO CON BOTTONE MARRONE","TWILL KAKI CHIARO","VERDE SALVIA SCURO","SALVIA A RIGHE","GREEN","OLIVE","OLIVA SCURO","GREEN","LIGHT GREEN PRINT","SAGE","OLIVA","Verde Logo","Verde acqua","Verde Chiaro","Bosco","VERDE CHIARO CON MOTIVO","MINT PATTERN","MOTIVO MINT","VERDE CHIARO SCINTILLANTE","VERDE SCINTILLANTE","VERDE CON STAMPA","MOTIVO VERDE","VERDE OLIVA SCINTILLANTE","VERDE NEON","VERDE FLOREALE","VERDE MINT","VERDE CHIARO FLOREALE","GREEN FLORAL","VERDE OLIVA DD","VERDE OLIVA MIMETICO","VERDE MENTA","VERDE OLIVA CHIARO","VERDE MINT A FIORI","NEON GREEN","VERDE CHIARO SCOZZESE","MENTA","VERDE OLIVA TIE-DYE","VERDE CHIARO CON STAMPA","VERDE CHIARO A FIORI","VERDE CHIARO","VERDE A RIGHE","VERDE","GREEN DD","VERDE LIME","VERDE SCURO","VERDE OLIVA SCURO","LIGHT GREEN","SALVIA","SCOZZESE VERDE","VERDE OLIVA FLOREALE","OLIVE GREEN","VERDE OLIVA","Verde mélange","Lime green","Light neon green","Verde kaki ch.","Bright green","Neon green","Verde mentaélange","Verde polvere chiaro","Verde nebbia","Light khaki green","Verde polvere","Verde menta chiaro","Verde chiaro pallido","Verde chiaro mélange","Verde-beige","Khaki green","Verde oliva scuro","Dark khaki green","Olive green","Verde nebbia chiaro","Verde neon chiaro","Verde muschio","Verde salvia","Verde neon","Dark green","Verde lime","Verde pistacchio","Verde-beige chiaro","Verde kaki chiaro","Verde giallognolo chiaro","Light green","Verde kaki scuro","Verde salvia chiaro","Verde salvia scuro","Verde kaki","Green","Verde chiaro","Verde acceso","Verde","Verde scuro","Verde menta","Verde oliva"]

viola=["QUADRI VIOLA","SCOZZESE BORDEAUX","MOTIVO BORDEAUX","BORDEAUX MÉLANGE","MALVA SLAVATO","VIOLA SCURO","MALVA","BORDEAUX A RIGHE","MALVA CHIARO","BURGUNDY STRIPE","QUADRI BURDEAUX","PURPLE","VIOLA TIE-DYE","VIOLA CON MOTIVO","VIOLA CHIARO CON STAMPA","VIOLA","BORDEAUX","LIGHT PURPLE","BORDEAUX TIE-DYE","Plum purple","Malva","Malva chiaro","Viola'amicizia","Viola prugna scuro","Lavanda","Prugna","Viola chiaro mélange","Lilla","Erica chiaro","Purple","Light purple","Viola mélange","Viola prugna","Bordeaux scuro","Bordeaux","Viola pallido","Viola","Viola chiaro"]

da_stabilire=['LAVAGGIO SCURO ACCESO','LAVAGGIO CHIARO CON STRAPPI E RAMMENDI','EFFETTO LAVAGGIO CHIARO','LAVAGGIO CHIARO ACCESO','LIGHT RIPPED WASH','LAVAGGIO CHIARO ACCESO CON STRAPPI','LAVAGGIO MEDIO ACCESO','LAVAGGIO SCURO CON STRAPPI E RAMMENDI','SHREDDED DARK WASH','LAVAGGIO SUPER CHIARO','LAVAGGIO SCURO CON RAMMENDI','LAVAGGIO CHIARO ACCESO CON VERNICE','LAVAGGIO EXTRACHIARO CON STRAPPI','LIGHT WASH WITH BLEACH','LAVAGGIO SUPER CHIARO CON STRAPPI','GREY TO BLACK OMBRE','BLACK TO BURGUNDY OMBRE','NAVY TO BLUE OMBRE','LIGHT BROWN TO BLACK OMBRE','DA NERO A BIANCO','DA NERO A COLOR MENTA','SFUMATO DA NERO AD AZZURRO','SFUMATO DA NERO A BIANCO','SFUMATO DA BLU A NERO','SFUMATO DA ROSSO A NERO','SFUMATO DA GRIGIO SCURO A NERO','DA NERO A SFUMATO VERDE CHIARO','NERO CON STRAPPI E RAMMENDI','LAVAGGIO MEDIO SCOLORITO','SFUMATO DA BIANCO A GRIGIO','DA AZZURRO A SFUMATO NERO','SFUMATO DA NERO A ROSA','NERO SO CAL','DARK PINK ICON','BLACK TO WHITE OMBRE','NAVY WITH GREY STRIPE','WHITE WITH TAN STRIPE','LAVAGGIO MEDIO CHIARO CON STRAPPI','LAVAGGIO MEDIO STAMPATO','NERO SLAVATO - STEP BROTHERS','BACCA','LAVAGGIO CHIARO CON VERNICE','LAVAGGIO MEDIO ACCESO CON STRAPPI','SCURO CON STRAPPI','LAVAGGIO CHIARO MEDIO STRAPPATO','CAMO','LAVAGGIO MEDIO CHIARO','LAVAGGIO MEDIO SCURO CON STRAPPI','DARK RINSE','LAVAGGIO MEDIO CON CINTURA','LIGHT DESTROYED WASH','LAVAGGIO CHIARO DISTRUTTO','MEDIO','LAVAGGIO MEDIO A RIGHE','LAVAGGIO MEDIO CON STRAPPI EFFETTO FLOREALE','TEAL PATTERN','DARK RIPPED WASH','LAVAGGIO MEDIO CON STRAPPI SULLE GINOCCHIA','RINSE SCURO','DISTRUTTO CHIARO','LAVAGGIO MEDIO DISTRUTTO','LAVAGGIO CHIARO MEDIO','LAVAGGIO MEDIO SCURO','RINSE LEGGERMENTE STRAPPATI','DISTRUTTO SCURO','LAVAGGIO MEDIO CON STRAPPI','CHIARO DISTRUTTO','LAVAGGIO MEDIO STAMPATO','LAVAGGIO SCURO','CHIARO SBIADITO E FONDO SEMPLICE','LAVAGGIO SCURO CON STRAPPI','LAVAGGIO MEDIO CON RAMMENDI','SCURO','DISTRUTTO SCURO CON FONDO SFRANGIATO','MEDIA','MEDIO CON RAMMENDI','LAVAGGIO MEDIO CON STRAPPI SCURO','LAVAGGIO CHIARO','MEDIO DISTRUTTO','LAVAGGIO MEDIO','LAVAGGIO SCURO MEDIO','LAVAGGIO CHIARO CON STRAPPI','RINSE','A FIORI ARANCIONI','NERO SLAVATO - STEP BROTHER','EFFETTO GRIGIO EFFETTO TINTURA','Black-coloured','Silver-coloured']

"""## Pulizia"""
n=0
assenti=[]


n_da_stabilire=0
n_altro=0
n_eliminato=0
for i in range(0,len(df)):
  m=df["Colore"][i].strip()

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
  elif m in altro:
    df["Colore"][i]="Altro"
    n_altro +=1 
      
       
  else:
    #Per avere in output su formato txt i colori non inseriti in nessuna sotto categoria e decidere meglio il da farsi  
    #Questa parte verrà poi inibita nelle fasi finali.
    n_eliminato += 1
    if df["Colore"][i] not in assenti :
        assenti.append(df["Colore"][i])  
        n+= 1 
        with open("/Users/mattia/Desktop/riepilogo_colori_ARMANI.txt","a") as f:
            f.write(str(n)+"  "+str(df["Colore"][i].strip()))
            f.write("\n")
    df=df.drop(i)
    
with open("/Users/mattia/Desktop/riepilogo_colori_ARMANI.txt","a") as f:
    f.write("\n\n")
    f.write("Riepilogo : \n")
    f.write("Numero di  articoli eliminati perchè con colori non identificabili:  "+str(n_eliminato))
    f.write("\n")
    f.write("Numero di colori da stabilire:  "+str(n_da_stabilire))
    f.write("\n")
    f.write("Articoli catalogati come altro: "+str(n_altro)) 
        
df=df.reset_index(drop=True)      #si devono rimettere gli indici perchè alcune righe che presentano colori ambigui verranno eliminate





m=df["Materiali"]

"""## Pulizia effettiva"""

dataset = pd.DataFrame({'A' : []})
for i in range(0,len(m)):
  if m[i]=="Null":
    #print("Eliminato")
    df=df.drop(i) #eliminare le righe che non hanno materiale
    continue 
  m[i]= m[i].replace("Composizione","")
  k=re.sub("[a-zA-Z\s]*:","",m[i]) #Restituisce solo i materiali con la corrispettiva percentuale
  #n=re.sub("[0-9%]*","",k)
  ma=re.findall(r"[a-zA-Z \s]{2,}",k)

  #df["Prezzo"][i]=df.loc[i].Prezzo.replace(".","")
  
  #if "Gratuito"== df.loc[i].Prezzo :
   #   df["Prezzo"][i]=490
  
  
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
        
    elif ma[j]=="Modacrilico" or ma[j]=="Modacrylic":
        ma[j]="Modacrilica"
    
    
    elif ma[j]=="Rayon" or ma[j]=="Viscose" or ma[j]=="Modal":
        ma[j]="Viscosa"
    
    elif ma[j]=="Cachemire" or ma[j]=="Goat_hair":
        ma[j]="Cashmere"
      
    elif ma[j]=="Polyamide" or  ma[j]=="Polyimide":
        ma[j]="Poliammide"
      
    elif ma[j]=="Acrylic" or ma[j]=="Acrilica"  :
        ma[j]="Acrilico"
        
    elif  ma[j]=="Acetate" :
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
        
    elif ma[j]=="Other_fibres" or ma[j]=="Fibre_non_specificate":
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

#Creazione della colonna che fornisce il numero di fibre presenti nel vestito.
dataset['N_Fibre_Differenti'] = dataset.sum(axis=1)
dataset.N_Fibre_Differenti.astype(int)



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

dati.to_csv('/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Dati puliti/pulito_ARMANI.csv')

#dati.to_csv('/Users/mattia/desktop/prova_ARMANI.csv')





