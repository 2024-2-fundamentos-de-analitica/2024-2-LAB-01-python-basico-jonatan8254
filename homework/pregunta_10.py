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

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    resultado = []
    
    for _, line in data:
        partes = line.strip().split("\t")
        # La letra se encuentra en la primera columna (índice 0)
        letra = partes[0]
        # La columna 4 (índice 3) contiene una lista de elementos separados por coma
        elementos_col4 = partes[3].split(",")
        # La columna 5 (índice 4) codifica un diccionario, y la cantidad de elementos es
        # el número de pares clave-valor separados por coma
        elementos_col5 = partes[4].split(",")
        resultado.append((letra, len(elementos_col4), len(elementos_col5)))
    
    return resultado

if __name__ == "__main__":
    print(pregunta_10())

