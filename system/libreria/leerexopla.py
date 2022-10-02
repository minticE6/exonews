import pandas as pd #cp: se usa la libreria de pandas para tratar las tablas importadas de wikipedia
marca1 = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Planetas_extrasolares") #cp: enlace desde wikipedia con la tabla de ultimos exoplanetas descubiertos
marca1 = marca1[1] #cp: de las varias tablas dentro del enlace de arriba la 1 es la que contiene la que necesitamos
marca1 = marca1.sort_values('Descubrimiento', ascending=False, ) #cp: se organizan la tabla por descubrimiento
marca1.drop(marca1.head(2).index, inplace=True) #cp: se elimina las dos primeras lineas por que el a;o de descubrimiento es NAN o TTV
marca1 = marca1.drop(['Excentricidad', 'Semieje mayor', 'Tipo estelar', 'Temperatura', 'Constelación'], axis=1) #cp: eliminan columnas no necesarias.
print(marca1.head(8))
