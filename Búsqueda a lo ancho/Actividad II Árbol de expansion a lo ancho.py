# -*- coding: utf-8 -*-
"""
Created on Mon March 4 00:20:15 2024
Este script implementa el algoritmo de búsqueda en anchura (BFS) para encontrar
el camino más corto entre dos nodos en un grafo no ponderado.
@author: Dea 

"""


from collections import deque


grafo = {"a": ["b", "c", "g"], "b": ["a", "d"], "c": ["a", "e"], "d": ["b", "f"], "e": ["c"], "f": ["d", "h"], "g": ["a"], "h": ["f"]}
 

ni = input("Nodo fuente: ")
nf = input("Nodo destino: ")

def ancho(grafo, ni, nf):
  """
    Implementación del algoritmo de búsqueda en anchura (BFS).

    Args:
        grafo (dict): Diccionario que representa el grafo.
        ni (str): Nodo fuente.
        nf (str): Nodo destino.

    Returns:
        list or str: Lista de aristas que forman el camino más corto entre ni y nf o "error" si no existe un camino.
    """
    visitados = set()
    padres = {}
    cola = deque([ni])
    
    while cola:
        nodo = cola.popleft()
       
        if nodo not in visitados:
            visitados.add(nodo)
            vecinos = grafo[nodo]
            for vecino in vecinos:
                if vecino not in visitados:
                    padres[vecino] = nodo
                    cola.append(vecino)
                    
    if nf not in padres:
        return "error"
    
    camino = []
    nodo_actual = nf
    while nodo_actual != ni:
        padre = padres[nodo_actual]
        camino.append((padre, nodo_actual))
        nodo_actual = padre
    
    camino.reverse()
    return camino

camino = ancho(grafo, ni,nf)

if isinstance(camino, str):
    print(camino)
else:
    print("Aristas recorridas de:", ni, "a", nf, ":")
    for eslabon in camino:
        print(f"Eslabón {eslabon}")

