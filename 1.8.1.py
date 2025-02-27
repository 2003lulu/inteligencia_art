# Implementación de BFS (Breadth-First Search)
from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(grafo, inicio):
    visitados = set()  # Conjunto de nodos visitados
    cola = deque([inicio])  # Cola para explorar los nodos en orden de amplitud

    while cola:
        nodo = cola.popleft()  # Sacamos el primer nodo de la cola
        if nodo not in visitados:
            visitados.add(nodo)  # Marcamos el nodo como visitado
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)  # Añadimos los nodos vecinos a la cola

    return visitados

# Ejemplo de uso
resultado = bfs(grafo, 'A')
print(f"Nodos visitados por BFS: {resultado}")
