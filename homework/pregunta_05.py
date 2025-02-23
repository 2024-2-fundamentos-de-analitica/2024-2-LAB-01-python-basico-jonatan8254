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

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    resultados = {}
    
    for _, line in data:
        partes = line.strip().split("\t")
        letra = partes[0]
        valor = int(partes[1])
        if letra not in resultados:
            # Inicializa con el primer valor encontrado para la letra
            resultados[letra] = (valor, valor)
        else:
            max_actual, min_actual = resultados[letra]
            if valor > max_actual:
                max_actual = valor
            if valor < min_actual:
                min_actual = valor
            resultados[letra] = (max_actual, min_actual)
    
    # Se ordena el resultado alfabéticamente por la letra
    lista_resultados = [(letra, resultados[letra][0], resultados[letra][1]) for letra in sorted(resultados.keys())]
    return lista_resultados

if __name__ == "__main__":
    print(pregunta_05())

