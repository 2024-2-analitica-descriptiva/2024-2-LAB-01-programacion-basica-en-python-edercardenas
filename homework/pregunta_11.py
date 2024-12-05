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
    lista = []
    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            elem_col_4 = line.strip().split('\t')[3].split(',')
            for i in elem_col_4:
                lista.append((i, int(line[2])))
        print(lista)
    lista = sorted(lista)
    
    diccionario = {}
    for i in lista:
        key = i[0]
        val = i[1]
        if key in diccionario:
            diccionario[key] += val
        else:
            diccionario[key] = val
    print(diccionario)
    return diccionario

pregunta_11()