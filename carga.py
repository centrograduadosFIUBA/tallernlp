from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# Lee el archivo de Excel con pandas
df = pd.read_excel("DataSetTemas.xlsx")

for index, row in df.iterrows():

    # Obtiene los datos de cada fila
    url = row["URL"]
    nombre_archivo = row["Nombre_archivo"]
    clase = row["Clase"]
    codigo = row["Código"]
       
    # Crear la carpeta si no existe
    if not os.path.exists("textos/" + clase):
        os.makedirs("textos/" + clase)
    
    # Obtener el contenido HTML de la página
    req = requests.get(url)
    if req.status_code == 200:
        html = BeautifulSoup(req.text, "html.parser")
        # Si deseas guardar cada párrafo en un archivo, puedes hacerlo de la siguiente manera:
        with open(f"textos/{clase}/{nombre_archivo}.txt", "w", encoding="utf-8") as f:
                for para in html.find_all("p"):
                    f.write(para.text)

print("finalizo")
