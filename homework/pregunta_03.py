"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    diccionario = {}

    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            key = line[0]
            if key in diccionario:
                diccionario[key] += int(line[2])
            else:
                diccionario[key] = int(line[2])

    lista = []

    print(diccionario)

    for i in diccionario:
        print(i)
        lista.append((i, diccionario[i]))

    lista = sorted(lista)
    print(lista)

    return lista

pregunta_03()