"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    lista = []
    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            elem_col_5 = line.strip().split('\t')[4].split(',')
            for sub_elem in elem_col_5:
                lista.append([line[0], int(sub_elem[4:])])
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

pregunta_12()