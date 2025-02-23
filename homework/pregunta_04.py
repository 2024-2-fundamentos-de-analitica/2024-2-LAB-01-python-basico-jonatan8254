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

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    ruta = "files/input/"
    data = load_input(ruta)
    conteo = {}
    for _, line in data:
        partes = line.strip().split("\t")
        # La fecha se encuentra en la tercera columna (índice 2)
        fecha = partes[2]
        # Se extrae el mes de la fecha en formato 'YYYY-MM-DD'
        mes = fecha[5:7]
        conteo[mes] = conteo.get(mes, 0) + 1
    # Se retorna la lista de tuplas ordenadas por el mes
    return sorted(conteo.items())

if __name__ == "__main__":
    print(pregunta_04())
