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
    diccionario = {}

    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            key = line[0]
            val = int(line[2])
            if key in diccionario:
                diccionario[key][0] = val if val > diccionario[key][0] else diccionario[key][0]
                diccionario[key][1] = val if val < diccionario[key][1] else diccionario[key][1]
            else:
                diccionario[key] = [val, val]

    print(diccionario)

    lista = []

    for i in diccionario:
        print(i)
        lista.append((i, diccionario[i][0], diccionario[i][1]))

    lista = sorted(lista)
    print(lista)

    return lista

pregunta_05()