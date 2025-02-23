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
    files = glob.glob(f'{input_directory}/*')  # Lee todos los archivos en el directorio indicado
    with fileinput.input(files=files) as f:
        sequence = [(fileinput.filename(), line) for line in f]  # Crea una lista de tuplas (nombre_archivo, línea)
    return sequence

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    conteo = {}
    for _, line in data:
        # Separa la línea usando el tabulador y extrae la primera columna (letra)
        letra = line.strip().split("\t")[0]
        conteo[letra] = conteo.get(letra, 0) + 1
    return sorted(conteo.items())

if __name__ == "__main__":
    print(pregunta_02())
