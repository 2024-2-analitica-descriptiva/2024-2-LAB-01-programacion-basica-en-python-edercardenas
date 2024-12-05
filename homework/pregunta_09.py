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
    lista_1 = []
    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip().split('\t')[4].split(',')
            lista_1 += line
            # print(line)
        print(lista_1)
        lista_1 = sorted(lista_1)
    
    diccionario = {}

    for elemento in lista_1:
        key = elemento[0:3]
        if key in diccionario:
            diccionario[key] += 1
        else:
            diccionario[key] = 1

    print(diccionario)

    return diccionario

pregunta_09()