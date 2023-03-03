from bs4 import BeautifulSoup
import requests  
url = "https://en.wikipedia.org/wiki/Alexander_the_Great"
req = requests.get(url)   
statusCode = req.status_code
# print("statusCode: ", statusCode)
if statusCode == 200:
    html = BeautifulSoup(req.text,"html.parser")

# print(html.prettify())

# print(html.title)

"""div = html.find(id='firstHeading')
print(div.text)"""

# print(html.title.string)

# ejemplo de captura de subtitulos
# print([item.get_text() for item in html.select("h2 .mw-headline")])

paragraphs = html.findAll("p")


cont = 0
for para in paragraphs:
    cont +=1
    print ()
    print ("Párrafo: ",cont)
    print ()
    print (para.text)
    # parrafo = open(  clase + "/" + archivo + str(cont),"w",encoding = "utf-8") 
    # parrafo.write(para.text)
    # parrafo.close()




