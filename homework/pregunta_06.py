"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    lista_1 = []
    with open('files/input/data.csv', "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip().split('\t')[4].split(',')
            lista_1 += line
            print(line)
        print(lista_1)
    
    diccionario = {}

    for elemento in lista_1:
        key = elemento[0:3]
        val = int(elemento[4:])
        if key in diccionario:
            diccionario[key][0] = val if val < diccionario[key][0] else diccionario[key][0]
            diccionario[key][1] = val if val > diccionario[key][1] else diccionario[key][1]
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

pregunta_06()