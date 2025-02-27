# Heurística simple para encontrar el número más cercano al objetivo
def heuristica(a, b):
    return abs(a - b)

# Lista de valores ya definida en el código
valores = [20, 35, 55, 60, 70]

# Permitir que el usuario ingrese el número objetivo
objetivo = int(input("Ingrese el número objetivo: "))

# Encontrar el valor más cercano al objetivo usando heurística
mejor_valor = min(valores, key=lambda x: heuristica(x, objetivo))

print(f"El valor más cercano al objetivo {objetivo} es: {mejor_valor}")
