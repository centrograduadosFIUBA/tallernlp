import os
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Descargar recursos de NLTK
## Descarga los datos del tokenizador de frases y palabras del NLTK. 
#Esto es necesario para poder utilizar la función word_tokenize() y sent_tokenize() de NLTK 
# para dividir el texto en palabras y frases.
nltk.download('punkt')
## Descarga una lista de palabras vacías, también conocidas como stop words, que son 
# palabras muy comunes en un idioma y que no suelen tener un significado importante en un texto.
nltk.download('stopwords')
## Descarga la base de datos léxica WordNet del NLTK, que es una base de datos de sinónimos 
# y relaciones semánticas entre palabras en inglés.
nltk.download('wordnet')

# Ruta donde se encuentran los archivos de texto
ruta = './textos/'

# Definir stopwords y lematizador (reduce las palabras a su forma base o lema)
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Iterar sobre las carpetas y archivos de texto
for carpeta in os.listdir(ruta):
    # Ignorar archivos que no son carpetas
    if not os.path.isdir(os.path.join(ruta, carpeta)):
        continue
        
    # Iterar sobre los archivos de texto de la carpeta
    for archivo in os.listdir(os.path.join(ruta, carpeta)):
        # Ignorar archivos que no son archivos de texto
        if not archivo.endswith('.txt'):
            continue
        
        # Leer el archivo de texto y eliminar signos de puntuación
        with open(os.path.join(ruta, carpeta, archivo), 'r', encoding='utf-8') as f:
            # `translate` se usa para reemplazar caracteres en una cadena, en este caso, 
            # se utiliza para eliminar los signos de puntuación en el texto
            # `string.punctuation` es una cadena predefinida que contiene todos los signos de puntuación en inglés. 
            # La función `maketrans` crea una tabla de traducción para ser utilizada por translate, 
            # donde se especifica que se desea traducir todos los caracteres de la cadena 
            # string.punctuation a None (es decir, borrarlos).
            texto = f.read().translate(str.maketrans('', '', string.punctuation))
        
        # Tokenizar el texto y eliminar stopwords
        tokens = word_tokenize(texto.lower())
        # crea una nueva lista tokens que contiene todos los tokens de la lista original tokens, 
        # excepto aquellos que se encuentran en la lista de stop_words.
        tokens = [token for token in tokens if token not in stop_words]
        
        # Lematizar los tokens
        ## para cada token en la lista "tokens", el código comprobará si ese token no está en la lista "stop_words"
        # Si el token no está en la lista "stop_words", entonces la función lemmatize() y se agrega a la lista "lemmas"
        lemmas = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]

        # Contar la frecuencia de los términos y obtener las palabras más comunes
        ## crear un objeto Counter que cuenta el número de ocurrencias de cada elemento en la lista lemmas. 
        # Esto es útil para contar la frecuencia de cada palabra o token en una lista.
        freq = Counter(lemmas)
        ## top_words se utiliza para obtener los 20 elementos más comunes en el objeto freq. 
        # El método most_common devuelve una lista de tuplas, donde cada tupla contiene un elemento y 
        # su frecuencia en orden descendente.
        top_words = freq.most_common(25)
        
        # Imprimir las palabras más comunes
        print(f'Carpeta: {carpeta}, Archivo: {archivo}')
        print(f'Top palabras: {top_words}\n')
