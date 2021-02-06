import datetime
import pandas as pd
import numpy as np
import csv

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas,file_name)
    funcion_minimo(datos_pandas,file_name)
    funcion_promedio(datos_pandas,file_name)

    funcion_mediana(datos_pandas,file_name)
    funcion_desviacion(datos_pandas,file_name)
    funcion_varianza(datos_pandas,file_name)

    datos_graficar = leer_datos(file_name)

    """"
    Inserte aqui las otras funciones.
    funcion_Minimo()
    funcion_Mediana()
    funcion_Promedio()
    funcion_Desviacion()
    funcion_Varianza()
    """
   
    return datos_graficar


def funcion_maximo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    dato_max= max(valores_temperatura)
    dato_guardar = [1, date_string, "Maximo", dato_max]
    guardar(dato_guardar, file_name)

def funcion_minimo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    dato_min= min(valores_temperatura)
    dato_guardar = [1, date_string, "Minimo", dato_min]
    guardar(dato_guardar, file_name)

def funcion_promedio(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    promedio=np.mean(valores_temperatura)
    dato_guardar = [1, date_string, "Promedio", promedio]
    guardar(dato_guardar, file_name)

def funcion_mediana(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    mediana=np.median(valores_temperatura)
    dato_guardar = [1, date_string, "Mediana", mediana]
    guardar(dato_guardar, file_name)

def funcion_varianza(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    varianza=np.var(valores_temperatura)
    dato_guardar = [1, date_string, "Varianza", varianza]
    guardar(dato_guardar, file_name)

def funcion_desviacion(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    desviacion= np.std(valores_temperatura)
    dato_guardar = [1, date_string, "Desviacion", desviacion]
    guardar(dato_guardar, file_name)


def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas