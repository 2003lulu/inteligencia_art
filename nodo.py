class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Crear nodos y enlazarlos
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo1.siguiente = nodo2  # Enlazar nodo1 con nodo2

print(nodo1.valor)  # 10
print(nodo1.siguiente.valor)  # 20
