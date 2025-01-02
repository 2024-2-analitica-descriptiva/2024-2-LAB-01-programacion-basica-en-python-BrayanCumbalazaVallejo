"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    fila = []
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            renglon = list(line.strip().split("\t"))
            letras1 = renglon[3]
            numero = int(renglon[1])
            letras = letras1.split(",")
            for letra in letras:
                fila.append((letra, numero))

    sequence = sorted(fila)
    diccionary = {}
    #Aprovechando el orden, saca el min y max
    for key, value in sequence:
        if key in diccionary:
            diccionary[key] += value
        else:
            diccionary[key] = value      

    return diccionary

if __name__ == "__main__":
    print(pregunta_11())
