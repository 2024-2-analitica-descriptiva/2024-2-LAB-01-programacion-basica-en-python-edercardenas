"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    diccionario = {}

    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            key = line[0]
            if key in diccionario:
                diccionario[key] += 1
            else:
                diccionario[key] = 1

    lista = []

    print(diccionario)

    for i in diccionario:
        print(i)
        lista.append((i, diccionario[i]))

    lista = sorted(lista)
    print(lista)

    return lista

pregunta_02()