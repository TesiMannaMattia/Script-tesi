import pandas as pd

df=pd.read_csv("/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Vestiti.csv")

try:      
    df = df.drop('Unnamed: 0', axis=1)
except:
    pass

try:      
    df = df.drop('index', axis=1)
except:
    pass

modalita=sorted(df.Categoria.unique())



"""
with open("/Users/mattia/desktop/modalita_categoria.txt","a") as f :
    for i in range(len(modalita)):
        f.write(str(i)+"  '"+str(modalita[i])+"',")
        f.write("\n")
    
    
modalita=sorted(df.Categoria.unique())    
with open("/Users/mattia/desktop/modalita_sottocategoria.txt","a") as f :
    for i in range(len(modalita)):
        f.write(str(i)+"  '"+str(modalita[i])+"',")
        f.write("\n")
      pass
  
      with open("/Users/mattia/Desktop/riepilogo_DELETEDsottocategorie.txt","a") as f:
          f.write(str(m))
          f.write("\n")        
"""    

#1
altro=[ "maniche lunghe", 'salopette','i migliori basic','cut out top','casual','Top e camicie in pelle Donna',
'Pezzi di sotto','Gonne e pantaloni in pelle Donna']
#2
biancheria_intima=["body e corsetti", 'body','sottovesti','slip','boxer corti','boxer','Slip','Boxer Attillati','Boxer','Biancheria intima']
#3
bikini=['bikini','Top bikini','Bikini']
#4
camicie=['tuniche',"camicette",'camicie in lino','camicie da notte','camicie','camicette''Maniche lunghe Uomo','Camicie Smoking','Camicie Eleganti Uomo','Camicie Eleganti','Camicie Donna','Camicie Classiche','Camicie Casual','Camicie & Bluse','Camicie','Bluse']
#5
canotte=['Canottiere','canotte','Canottiere','Canotte']
#6
calzini_calze=['fantasmini','calzini sportivi', 'calzini','Calzini','Calze']
#7
costumi=["Costumi da Bagno Donna","Pezzi di sotto bikini",'costumi interi','costumi da bagno','Slip da Mare','Costumi Interi','Boxer da Mare']
#8
felpe=['felpe stampate da uomo','felpe con o senza cappuccio per donna', 'felpe con cappuccio per donna','felpe con cappuccio','felpe','Felpe con Zip','Felpe con Cappuccio','Felpe Uomo','Felpe Donna','Felpe']
#9
giacche_e_giubotti=["Casual Jackets for Men",'smanicati','parka', 'giubbotto biker','giacche in lino','giacche impermeabili','giacche di pelle','giacche','cappotti','bomber','blazer','Trench','Soprabiti in Pelle','Smanicati','Poncho e Mantelle Donna','Piumini Smanicati','Piumini Donna','Piumini','Pelliccia sintetica','Pellicce ecologiche','Peacots for Women','Montone Donna','Mantelle','Long Pants for Women','Long Coats For Men','Jackets for Women','Giacche in Pelle','Giacche in Denim','Giacche imbottite e piumini Uomo','Giacche di Pelle Uomo','Giacche da Sera','Giacche da Sci','Giacche a Vento Uomo','Giacche a Vento','Giacche Smoking','Giacche Imbottite','Giacche Fashion','Giacche Eleganti Uomo','Giacche Eleganti','Giacche Doppiopetto','Giacche Donna','Giacche Casual','Giacche','Cappotti Uomo','Cappotti','Caban','Bomber in pelle','Bomber Uomo','Blouson']
#10
gilet=['gilet maglione','gilet','Gonne in Pelle','Gilet','Gilet Imbottiti','Gilet Uomo']
#11
gonne=['minigonne','longuette','gonne scozzesi','gonne lunghe','gonna di seta','Gonne Midi','Gonne Lunghe e Gonne Midi Donna','Gonne Lunghe','Gonne Corte Donna','Gonne Corte','Gonne']
#12
jeans=['wide leg','straight jeans', 'relaxed jeans', 'regular jeans', 'jeans straight','jeans slim','jeans shorts','jeans modellanti','jeans larghi','jeans corti','jeans boyfriend', 'jeans a zampa','Jeans Uomo','Jeans Svasati','Jeans Slim','Jeans Skinny','Jeans Regular','Jeans Larghi','Jeans Gamba Dritta','Jeans Gamba Ampia','Jeans']
#13
abbigliamento_sportivo=["Pezzi di sotto Active","Jogger",'tute lunghe','tute e joggers','tute corte','leggings','joggers','jogger shorts','cycling shorts','collant e leggings','Tute Uomo','Tute Sportive','Tute Donna','Tute','Top Sportivi','Pantaloni da jogging Donna','Pantaloni da Jogging Uomo','Pantaloni da Jogging Activewear','Leggings']
#14
magliette_e_top=['coprispalle e boleri','top corti', "top con scollo all'americana", 'top con colletto','top bralette','top a fascia','polo','manica lunga','Topwear Active','Topwear','Top in Maglia', 'Top Donna','Top','Scollo a V Uomo','Polo Uomo','Polo','Maniche corte Uomo','Maniche lunghe Uomo']
#15
maglioni_e_cardigan=['pullover','dolcevita e maglie a collo alto','dolcevita','cardigan','Turtlenecks for Women','Turtleneck for Men','Maglioni','Maglieria Donna','Girocollo Uomo','Dolcevita','Cardigan Uomo','Cardigan Donna','Cardigan']
#16
pantaloni=['5 Tasche',"Pantaloni a Gamba Dritta Donna","Pantaloni da Casa",'slim','skinny','shorts vita alta', 'pantaloni a palazzo','pantaloni a zampa','pantaloni cargo', 'pantaloni chino', 'pantaloni corti lino', 'pantaloni culotte','pantaloni di lino','pantaloni eleganti','pantaloni in lino','pantaloni in pelle','pantaloni vita alta','chinos e pantaloni','chinos','casual shorts','bermuda cargo','bermuda','Short e bermuda Uomo','Shorts Donna','Shorts','Shorts','Pantaloni in pelle','Pantaloni in Pelle','Pantaloni in Felpa','Pantaloni di Felpa','Pantaloni da Sci','Pantaloni da Casa''Pantaloni a Gamba Dritta Donna','Pantaloni Uomo','Pantaloni Palazzo', 'Pantaloni Fashion','Pantaloni Eleganti', 'Pantaloni Culotte Donna','Pantaloni Classici','Pantaloni','Pantaloni Casual']
#17
pigiami=['vestaglie',"Pezzi di Sotto Sleep",'pigiami','Pigiami','Maglie del Pigiama',"Abbigliamento notte"]
#18
reggiseni=['reggiseni','Reggiseni Sportivi','Bralette']
#19
t_shirt=[ 't-shirt', 'maniche corte', 'T-Shirt Regular Fit','T-Shirt Slim Fit','T-Shirt a Maniche Corte','T-Shirt a Maniche Lunghe','T-Shirt da Casa','T-shirt', 'T-shirt & Maglie serafino','T-shirt Donna','T-Shirt Regular Fit','T-Shirt Cropped','T-Shirt','Maniche corte Uomo']
#20, si intendono vestiti da sera, abiti eleganti.
vestiti=[ 'abiti t-shirts','vestito maniche a sbuffo', 'vestiti senza maniche','vestiti maglietta','vestiti cut-out','skater dress', 'invitata','eleganti','damigella','caftano','abiti per i party','abiti maxi', 'abiti manica lunga','abiti incrociati','abiti in pizzo', 'abiti corti','abiti al polpaccio', 'Vestiti Lunghi','Vestiti Corti','Vestiti', 'Smoking','Coordinati','Abiti da sera','Abiti Uomo','Abiti Spezzati Uomo','Abiti Slim Fit','Abiti Regular Fit','Abiti Midi','Abiti', 'Abiti Comfort Fit','Abiti Corti Donna','Abiti Lunghi e Abiti Medi Donna']

    
n_altro=0
aaa=[]
for i in range(0,len(df)):
  m=df["Sotto_categoria"][i].strip()
  
    
  if  m in altro:
      df["Categoria"][i]="Altro"
      n_altro+=1

 
    
  elif m in biancheria_intima: #2
      df["Categoria"][i]="Biancheria Intima"

  elif m in bikini:#3
      df["Categoria"][i]="Bikini"
      
  elif m in camicie:#4
      df["Categoria"][i]="Camicie"
      
  elif m in canotte:#5
      df["Categoria"][i]="Canotte"

  elif m in calzini_calze: #6
      df["Categoria"][i]="Calzini e calze"
      
  elif m in costumi:#7
      df["Categoria"][i]="Costumi"
      
  elif m in felpe:#8
      df["Categoria"][i]="Felpe"
      
  elif m in giacche_e_giubotti:#9
      df["Categoria"][i]="Giacche e cappotti"
      
  elif m in gilet:#10
      df["Categoria"][i]="Gilet"
      
  elif m in gonne:#11
      df["Categoria"][i]="Gonne"
      
  elif m in jeans:#12
      df["Categoria"][i]="Jeans"
      
  elif m in abbigliamento_sportivo:#13
      df["Categoria"][i]="Abbigliamento sportivo"      

  elif m in magliette_e_top:#14
      df["Categoria"][i]="Magliette e top"
      
  elif m in maglioni_e_cardigan:#15
      df["Categoria"][i]="Maglioni e cardigan"
      
  elif m in pantaloni:#16
      df["Categoria"][i]="Pantaloni"
      
  elif m in pigiami:#17
      df["Categoria"][i]="Pigiami"
      
  elif m in reggiseni:#18
      df["Categoria"][i]="Reggiseni"
      
  elif m in t_shirt:#19
      df["Categoria"][i]="T-shirt"
      
  elif m in vestiti: #20
      df["Categoria"][i]="Vestiti"
  else:
      df=df.drop(i)
      

      

     


with open("/Users/mattia/Desktop/riepilogo_ALTROsottocategorie.txt","a") as f:
    f.write("\n\n")

    f.write("\n")
    f.write("Articoli catalogati come altro: "+str(n_altro)) 
        
df=df.reset_index()

try:      
    df = df.drop('index', axis=1)
except:
    pass






df.to_csv('/Users/mattia/Library/Mobile Documents/com~apple~CloudDocs/Tesi/Dati/Vestiti.csv')


















