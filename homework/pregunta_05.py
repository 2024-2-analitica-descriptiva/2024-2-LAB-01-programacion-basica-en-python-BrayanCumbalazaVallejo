"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    fila = []
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            renglon = list(line.strip().split("\t"))
            letra = renglon[0]
            numero = int(renglon[1])
            fila.append((letra, numero))
    sequence = sorted(fila)
    diccionary = {}
    #Aprovechando el orden, saca el max y min
    for key, value in sequence:
        if key in diccionary:
            diccionary[key][0] = value
        else:
            diccionary[key] = [1, value]
    tuplas3 = []
    for key, value in diccionary.items():
        tuplas3.append((key, diccionary[key][0], diccionary[key][1]))
               

    return tuplas3


