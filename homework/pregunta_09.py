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

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """
    ruta = "files/input/"
    data = load_input(ruta)
    conteo = {}
    
    for _, line in data:
        partes = line.strip().split("\t")
        # La columna 5 es la que contiene el diccionario codificado en formato string
        diccionario_str = partes[4]
        pares = diccionario_str.split(",")
        for par in pares:
            clave, _ = par.split(":")
            conteo[clave] = conteo.get(clave, 0) + 1
    
    return conteo

if __name__ == "__main__":
    print(pregunta_09())

