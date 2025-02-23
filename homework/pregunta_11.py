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

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    ruta = "files/input/"
    data = load_input(ruta)
    suma_por_letra = {}
    
    for _, line in data:
        partes = line.strip().split("\t")
        valor = int(partes[1])
        # La columna 4 (índice 3) contiene letras separadas por comas
        letras = partes[3].split(",")
        for letra in letras:
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    
    # Se ordena el diccionario por clave alfabéticamente
    return {clave: suma_por_letra[clave] for clave in sorted(suma_por_letra.keys())}

if __name__ == "__main__":
    print(pregunta_11())

