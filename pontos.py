import numpy as np

def pontos(elemento, prop):
    elementos = prop['elementos']
    nos = prop['nos']
    graus_liberdade = prop['graus_liberdade']

    # Nós que o elemento está conectado
    fromNode = elementos[elemento][0]
    toNode = elementos[elemento][1]

    # Coordenadas de cada nó
    fromPoint = np.array(nos[fromNode])
    toPoint = np.array(nos[toNode])

    # Graus de liberdade de cada nó
    grlib = graus_liberdade[fromNode]
    grlib.extend(graus_liberdade[toNode])
    grlib = np.array(grlib)

    return fromPoint, toPoint, grlib

"""Retorna as coordenadas de cada nó do elemento 
e um vetor contendo os graus de liberdade associados."""