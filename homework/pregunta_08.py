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

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera columna que aparecen asociadas a dicho valor de la segunda columna.
    
    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    agrupacion = {}
    
    for _, line in data:
        partes = line.strip().split("\t")
        letra = partes[0]
        valor = int(partes[1])
        if valor not in agrupacion:
            agrupacion[valor] = set()
        agrupacion[valor].add(letra)
    
    # Se convierte el conjunto de letras en una lista ordenada y se organiza por el valor de la segunda columna
    resultado = []
    for valor in sorted(agrupacion.keys()):
        letras = sorted(list(agrupacion[valor]))
        resultado.append((valor, letras))
    
    return resultado

if __name__ == "__main__":
    print(pregunta_08())
