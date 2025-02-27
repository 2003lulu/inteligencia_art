# Implementación simple del algoritmo A* (esto requiere una heurística)
import heapq

def a_estrella(grafo, inicio, fin, heuristica):
    abierta = []
    cerrada = set()
    heapq.heappush(abierta, (0 + heuristica(inicio), 0, inicio, []))

    while abierta:
        _, costo, nodo, camino = heapq.heappop(abierta)
        if nodo in cerrada:
            continue
        camino = camino + [nodo]
        if nodo == fin:
            return camino
        cerrada.add(nodo)
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in cerrada:
                heapq.heappush(abierta, (costo + peso + heuristica(vecino), costo + peso, vecino, camino))
    return None

# ALGORITMO A*

# Grafo con nodos y costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heurística de distancia (simple)
def heuristica(nodo):
    distancias = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
    return distancias.get(nodo, 0)

# Ejemplo de uso
camino = a_estrella(grafo, 'A', 'D', heuristica)
print(f"El camino más corto es: {camino}")