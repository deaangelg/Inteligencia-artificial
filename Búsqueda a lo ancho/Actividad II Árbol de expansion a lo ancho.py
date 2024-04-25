# -*- coding: utf-8 -*-
"""
Created on Mon March 4 00:20:15 2024

@author: Dea 

"""


from collections import deque


grafo = {"a": ["b", "c", "g"], "b": ["a", "d"], "c": ["a", "e"], "d": ["b", "f"], "e": ["c"], "f": ["d", "h"], "g": ["a"], "h": ["f"]}
 

ni = input("Nodo fuente: ")
nf = input("Nodo destino: ")

def ancho(grafo, ni, nf):
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

