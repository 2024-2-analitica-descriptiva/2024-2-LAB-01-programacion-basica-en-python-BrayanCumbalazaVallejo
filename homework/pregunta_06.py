"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

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
    fila = []
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            renglon = list(line.strip().split("\t"))
            letras1 = renglon[-1]
            letras = letras1.split(",")
            for x in letras:
                v = x.split(":")
                fila.append((v[0], int(v[1])))

    sequence = sorted(fila)
    diccionary = {}
    #Aprovechando el orden, saca el min y max
    for key, value in sequence:
        if key in diccionary:
            diccionary[key][0] = value
        else:
            diccionary[key] = [value, value]
    tuplas3 = []
    for key, value in diccionary.items():
        tuplas3.append((key, diccionary[key][1], diccionary[key][0]))
               

    return tuplas3
