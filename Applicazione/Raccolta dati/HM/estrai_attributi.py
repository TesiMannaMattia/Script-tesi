
from bs4 import BeautifulSoup

def mini_estrattore(html):
    dd=html.find_all("dd")
    attributo=""
    for j in range(0,len(dd)):
        attributi=dd[j].text
        if len(dd) > 1 and j > 0 :
            attributo = attributo +","+  attributi
        else:
            attributo = attributi
    
    return attributo 
        




def estrazione_attributi(html):
    
    righe=html.find_all("div")
    altro="Null"
    materiale="Null"
    id_articolo="Null"
    for i in range(0,len(righe)):
    
        #Estrarre nome attributo, composizione, Ulteriori informazioni sul materiale....
        nome_attributo=righe[i].find("dt").text
    
        #Pulire il nome attributo
        nome_attributo=nome_attributo.strip().lower()
       # print(nome_attributo)
        
        if nome_attributo == "composizione"    :  
            #print(i,nome_attributo)
            materiale=mini_estrattore(righe[i])
        
        elif nome_attributo == "numero di articolo" or nome_attributo == "n. art." :
            #print(i,nome_attributo)
            id_articolo=mini_estrattore(righe[i])
        
        elif nome_attributo=="ulteriori informazioni sul materiale":
            # print(i,nome_attributo)
            altro=mini_estrattore(righe[i])
            
    return materiale, id_articolo, altro
    
            

#html="""<dl class="ProductAttributesList-module--datalist__ketGC"><div class="ProductAttributesList-module--descriptionListItem__3vUL2"><dt class="Heading-module--general__3HQET ProductAttributesList-module--title__3o6do Heading-module--xsmall__4YCtn">Taglia</dt><dd class="BodyText-module--general__32l6J ProductAttributesList-module--value__ztcpd BodyText-module--meta__34sFL">Il modello è alto 179cm/5'10" e indossa la taglia L</dd></div><div class="ProductAttributesList-module--descriptionListItem__3vUL2"><dt class="Heading-module--general__3HQET ProductAttributesList-module--title__3o6do Heading-module--xsmall__4YCtn">Modello</dt><dd class="BodyText-module--general__32l6J ProductAttributesList-module--value__ztcpd BodyText-module--meta__34sFL">Linea aderente</dd></div><div class="ProductAttributesList-module--descriptionListItem__3vUL2"><dt class="Heading-module--general__3HQET ProductAttributesList-module--title__3o6do Heading-module--xsmall__4YCtn">Composizione</dt><dd class="BodyText-module--general__32l6J ProductAttributesList-module--value__ztcpd BodyText-module--meta__34sFL">Poliammide 92%, Elastan 8%</dd></div><div class="ProductAttributesList-module--descriptionListItem__3vUL2"><dt class="Heading-module--general__3HQET ProductAttributesList-module--title__3o6do Heading-module--xsmall__4YCtn">N. art.</dt><dd class="BodyText-module--general__32l6J ProductAttributesList-module--value__ztcpd BodyText-module--meta__34sFL">1067060001</dd></div></dl>
#"""

#html=BeautifulSoup(html,"html.parser")

#print(estrazione_attributi(html))

    

