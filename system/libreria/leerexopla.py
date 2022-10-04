import pandas as pd #cp: se usa la libreria de pandas para tratar las tablas importadas de wikipedia


try:
    marca1 = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Planetas_extrasolares") #cp: enlace desde wikipedia con la tabla de ultimos exoplanetas descubiertos
    marca1 = marca1[1] #cp: de las varias tablas dentro del enlace de arriba la 1 es la que contiene la que necesitamos
    marca1 = pd.DataFrame(marca1)
    marca1 = marca1.sort_values('Descubrimiento', ascending=False, ) #cp: se organizan la tabla por descubrimiento
    marca1.drop(marca1.head(2).index, inplace=True) #cp: se elimina las dos primeras lineas por que el a;o de descubrimiento es NAN o TTV
    tabla_exoplanetas = marca1.drop(['Excentricidad', 'Semieje mayor', 'Tipo estelar', 'Constelación', 'Distancia', 'Método', 'Masa', 'Radio', 'Periodo orbital'], axis=1) #cp: eliminan columnas no necesarias.
    tabla_exoplanetas = tabla_exoplanetas.head(8)
    tabla_exoplanetas.to_csv('top_nuevos_exoplanetas.csv') #cp: se crea un archivo csv para facilitar la importacion de datos a MYSQL
except OSError:
    print("Error al intentar bajar la tabla de wikipedia, habilite la conexion con internet")