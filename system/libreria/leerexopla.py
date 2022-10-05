import pandas as pd #cp: se usa la libreria de pandas para tratar las tablas importadas de wikipedia
import pymysql
import csv
import re

try:
    marca1 = pd.read_html("https://es.wikipedia.org/wiki/Anexo:Planetas_extrasolares") #cp: enlace desde wikipedia con la tabla de ultimos exoplanetas descubiertos
    marca1 = marca1[1] #cp: de las varias tablas dentro del enlace de arriba la 1 es la que contiene la que necesitamos
    marca1 = pd.DataFrame(marca1)
    marca1 = marca1.sort_values('Descubrimiento', ascending=False, ) #cp: se organizan la tabla por descubrimiento
    marca1.drop(marca1.head(2).index, inplace=True) #cp: se elimina las dos primeras lineas por que el a;o de descubrimiento es NAN o TTV
    tabla_exoplanetas = marca1.drop(['Excentricidad', 'Semieje mayor', 'Tipo estelar', 'Temperatura', 'Método', 'Masa', 'Radio', 'Periodo orbital'], axis=1) #cp: eliminan columnas no necesarias.
    tabla_exoplanetas = tabla_exoplanetas.head(8)
    tabla_exoplanetas.to_csv('top_nuevos_exoplanetas.csv') #cp: se crea un archivo csv para facilitar la importacion de datos a MYSQL
except OSError:
    print("Error al intentar bajar la tabla de wikipedia, habilite la conexion con internet")

try:
    archivo_csv = open('top_nuevos_exoplanetas.csv', 'r')
    filas = csv.reader(archivo_csv, delimiter=',')
    listas = list (filas)
    del (listas[0])
    listas = listas
except:
    print('fallo la lectura del archivo csv o la coneccion con la base de datos')

for i in listas:
    dato_solo = [0,0,0,0,0,0]
    dato_insertar = i
    for j in range(0, len(dato_insertar)):
        dato_solo[j] =  re.sub("Â\xa0"," ",dato_insertar[j])
    dato_solo = tuple (dato_solo[1:6])
    print(dato_solo)
    try:
        conexionBD = pymysql.connect(host='localhost', user='root', password='', db='exonews')
        conexionBD2 = conexionBD.cursor()
        sql = "INSERT INTO libreria_explanetas (nombre, descubrimiento, tipo, constelacion, distancia) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(dato_solo[0], dato_solo[3], dato_solo[1], dato_solo[4], dato_solo[2])
        conexionBD2.execute(sql)
        conexionBD.commit()
        conexionBD.close()
    except:
        print("problemas de conexion con la base de datos")
#cp: es para eliminar registros duplicados en la base de datos apartir del nombre del exoplaneta
try:
    conexionBD = pymysql.connect(host='localhost', user='root', password='', db='exonews')
    conexionBD2 = conexionBD.cursor()
    sql = "ALTER IGNORE TABLE libreria_explanetas ADD UNIQUE INDEX(nombre)"
    conexionBD2.execute(sql)
    conexionBD.commit()
    conexionBD.close()
except:
     print("problemas de conexion con la base de datos")
#cp: para facilitar eliminar los datos duplicados se convierte nombre en unique y se debe eliminar para volver a escribir dadtos.
try:
    conexionBD = pymysql.connect(host='localhost', user='root', password='', db='exonews')
    conexionBD2 = conexionBD.cursor()
    sql = "ALTER TABLE libreria_explanetas DROP INDEX nombre"
    conexionBD2.execute(sql)
    conexionBD.commit()
    conexionBD.close()
except:
     print("problemas de conexion con la base de datos")