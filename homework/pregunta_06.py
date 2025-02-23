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

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor después del caracter ':' corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado más
    pequeño y el valor asociado más grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    resultados = {}

    for _, line in data:
        partes = line.strip().split("\t")
        # La columna 5 es el índice 4
        diccionario_str = partes[4]
        pares = diccionario_str.split(",")
        for par in pares:
            clave, valor_str = par.split(":")
            valor = int(valor_str)
            if clave not in resultados:
                resultados[clave] = (valor, valor)
            else:
                min_actual, max_actual = resultados[clave]
                min_actual = valor if valor < min_actual else min_actual
                max_actual = valor if valor > max_actual else max_actual
                resultados[clave] = (min_actual, max_actual)
    
    # Se ordena el resultado alfabéticamente por la clave
    lista_resultados = [(clave, resultados[clave][0], resultados[clave][1]) for clave in sorted(resultados.keys())]
    return lista_resultados

if __name__ == "__main__":
    print(pregunta_06())

