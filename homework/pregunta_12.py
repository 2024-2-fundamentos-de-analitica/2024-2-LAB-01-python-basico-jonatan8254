"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import fileinput
import glob
import os.path

def load_input(input_directory):
    files = glob.glob(f'{input_directory}/*')  # Lee todos los archivos del directorio indicado
    with fileinput.input(files=files) as f:
        # Crea una lista de tuplas (nombre_archivo, línea)
        sequence = [(fileinput.filename(), line) for line in f]
    return sequence

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    ruta = "files/input/"
    data = load_input(ruta)
    suma_por_letra = {}

    for _, line in data:
        partes = line.strip().split("\t")
        letra = partes[0]
        # La columna 5 es la que contiene el diccionario en formato string.
        # Se parsea para sumar todos sus valores.
        col5 = partes[4]
        suma_valores = 0
        for par in col5.split(","):
            _, valor_str = par.split(":")
            suma_valores += int(valor_str)
        
        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores

    return suma_por_letra

if __name__ == "__main__":
    print(pregunta_12())

