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
        sequence = [(fileinput.filename(), line) for line in f]  # Crea una lista de tuplas (nombre_archivo, línea)
    return sequence

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    suma_por_letra = {}
    for _, line in data:
        # Separa la línea usando tabulador y extrae la letra y el valor de la columna 2
        partes = line.strip().split("\t")
        letra = partes[0]
        valor = int(partes[1])
        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    # Retorna las tuplas ordenadas alfabéticamente por la letra
    return sorted(suma_por_letra.items())

if __name__ == "__main__":
    print(pregunta_03())
