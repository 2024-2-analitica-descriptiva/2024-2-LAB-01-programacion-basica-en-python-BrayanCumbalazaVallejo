"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    fila = []
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            renglon = list(line.strip().split("\t"))
            letras1 = renglon[-1]
            letras = letras1.split(",")
            for x in letras:
                v = x.split(":")
                fila.append((v[0], 1))

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
    print(pregunta_09())


