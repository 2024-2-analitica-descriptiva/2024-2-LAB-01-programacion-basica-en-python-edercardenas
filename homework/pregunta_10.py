"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]

    """
    lista = []
    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            num_elem_col_4 = len(line.strip().split('\t')[3].split(','))
            num_elem_col_5 = len(line.strip().split('\t')[4].split(','))
            lista.append((line[0], num_elem_col_4, num_elem_col_5))
        print(lista)
    return lista

pregunta_10()