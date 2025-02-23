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
    
    files = glob.glob(f'{input_directory}/*')  #lee todo el conyenido de la carpeta input_directory con /*, si ponemos /*.txt solo leee los txt
    with fileinput.input(files = files) as f:  #Va a leer secuencialmente cada arcivo, el primer file es lo que espera la funcion y el segundo es mi variable
        sequence = [ (fileinput.filename(), line) for line in f ] #agrega ctuplas a la lista con el nombre del archivo como calve , y la linea como valor

    return sequence

         

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    
    """
    ruta = "files/input/"
    data = load_input(ruta)
    suma=0
    for archive, line in data:
        line=line.strip().split("\t")
        suma+=int(line[1])
    return suma
if __name__ == "__main__":
    print(pregunta_01())