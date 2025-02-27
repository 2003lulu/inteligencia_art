import os
import datetime
import random
import math

def ejercicio_1():
    try:
        temperatura_usuario = int(input("Ingresa la temperatura en °C: "))
        
        if 16 <= temperatura_usuario < 19:
            lugar = "San Andrés Chicahuaxtla"
            lugar2 = "San Martín Itunyoso"
        elif 19 <= temperatura_usuario < 22:
            lugar = "Tlaxiaco"
            lugar2 = "Chalcatongo"
        elif 22 <= temperatura_usuario < 24:
            lugar = "Tlaxiaco"
            lugar2 = None 
        elif 24 <= temperatura_usuario < 26:
            lugar = "Putla"
            lugar2 = "Mesones"
        elif temperatura_usuario >= 30:
            lugar = "Pinotepa (posiblemente al mediodía en verano)"
            lugar2 = "Puerto Escondido (posiblemente al mediodía en verano)"
        else:
            lugar = "Una temperatura fuera del rango esperado"
            lugar2 = None

        if lugar2:
            print(f"La temperatura de {temperatura_usuario}°C corresponde a los lugares: {lugar} y {lugar2}.")
        else:
            print(f"La temperatura de {temperatura_usuario}°C corresponde a {lugar}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def ejercicio_2():
    archivo_folio = "folio.txt"

    def obtener_folio():
        reiniciar = input("¿Deseas reiniciar el folio a 0001? (s/n): ").strip().lower()
        if reiniciar == "s":
            with open(archivo_folio, "w") as f:
                f.write("1") 
            print("Folio reiniciado a 0001.\n")
            return 1
        
        if not os.path.exists(archivo_folio):
            with open(archivo_folio, "w") as f:
                f.write("1")
            return 1
        
        with open(archivo_folio, "r") as f:
            folio = int(f.read().strip())
        folio += 1 
        with open(archivo_folio, "w") as f:
            f.write(str(folio))
        return folio

    folio = obtener_folio()
    tienda = input("Tienda: ") 
    cliente = input("Cliente: ") 
    nombre_producto = input("Producto: ") 
    cantidad = int(input("Ingrese la cantidad del producto: ")) 
    precio_unitario = float(input("Ingrese el precio unitario del producto: ")) 

    total_compra = cantidad * precio_unitario 
    descuento = total_compra * 0.10 if total_compra > 100 else 0
    total_final = total_compra - descuento 

    print("\n==================== TICKET DE COMPRA ====================")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    print(f"Tienda: {tienda}")
    print(f"Folio: {folio:04d}") 
    print(f"Fecha y hora: {fecha}")
    print("---------------------------------------------------------")
    print(f"Cliente: {cliente}")
    print(f"Producto: {nombre_producto}")
    print(f"Cantidad: {cantidad}")
    print(f"Total de la compra: ${total_compra:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total a pagar: ${total_final:.2f}")
    print("=========================================================")
    print("¡Gracias por tu compra! ¡Vuelve pronto!")
    print("=========================================================")

def ejercicio_3():
    numero = int(input("Introduce un número: "))
    
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

def ejercicio_4():
    nota = int(input("Ingresa tu calificación (0-100): "))
    if 90 <= nota <= 100:
        print("Tu calificación es: A")
    elif 80 <= nota < 90:
        print("Tu calificación es: B")
    elif 70 <= nota < 80:
        print("Tu calificación es: C")
    elif 60 <= nota < 70:
        print("Tu calificación es: D")
    else:
        print("Tu calificación es: F")

def ejercicio_5():
    num_ale = random.randint(1, 10)
    adivina = int(input("Adivina el número entre 1 y 10: "))
    print(f"El número aleatorio es {num_ale}.")
    if adivina == num_ale:
        print("Correcto. Has adivinado el número.")
    else:
        print(f"Incorrecto. El número era {num_ale}.")

def ejercicio_6():
    numero = int(input("Ingresa un número: "))
    if numero > 0:
        print(f"{numero} es positivo.")
    elif numero < 0:
        print(f"{numero} es negativo.")
    else:
        print("El número es cero.")

def ejercicio_7():
    num = int(input("Ingresa un número: "))
    if num > 10:
        print(f"{num} es mayor que 10.")
    else:
        print(f"{num} no es mayor que 10.")
def ejercicio_8():
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        print(f"{num} es par.")
    else:
        print(f"{num} es impar.")

def ejercicio_9():
    radio = float(input("Ingresa el radio del círculo en metros:\n"))
    area = math.pi * (radio ** 2)
    print(f"\nEl área del círculo con radio {radio} metros es: {area:.2f} metros cuadrados")
    print("\nHecho por Antonia")

def ejercicio_10():
    num1 = float(input("Ingresa num1: "))
    num2 = float(input("Ingresa num2: "))
    resta = num1 - num2
    print("La resta es", resta)
    multiplicacion = num1 * num2
    print("La multiplicación es", multiplicacion)
    print("\nHecho por Antonia")

def ejercicio_11():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")
    
def ejercicio_12():
    Nombre = input("¿Cuál es tu nombre? ")
    Edad = int(input("¿Cuántos años tienes? "))
    Altura = float(input("¿Cuánto mides? (en metros) "))
    print("Hola", Nombre, "tienes", Edad, "años y mides", Altura, "metros.")

def ejercicio_13():
    Nombre = "Antonia"
    Edad = 21
    Altura = 1.60
    print("Nombre:", Nombre)
    print("Edad:", Edad)
    print("Altura:", Altura)
    suma = Edad + 5
    print("En 5 años, tendré", suma, "años")

def ejercicio_14():
    Nombre = "Antonia"
    Edad = "21"
    Altura = "1.60"
    print("Nombre:", Nombre)
    print("Edad:", Edad)
    print("Altura:", Altura)

def ejercicio_15():
    Nombre = str(input("Ingrese el nombre: "))
    Edad = int(input("Ingresa la edad: "))
    Altura = str(input("Ingresa la altura: "))
    suma = Edad + 5
    print("En 5 años, tendré", suma, "años")
    print(Nombre, Altura)

def ejercicio_16():
    frutas = ["Manzana", "Banana", "Cereza"]
    for fruta in frutas:
        print(f"Me gusta la {fruta}")

def ejercicio_17():
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None
    nodo1 = Nodo(10)
    nodo2 = Nodo(20)
    nodo1.siguiente = nodo2
    print(nodo1.valor)
    print(nodo1.siguiente.valor)

def ejercicio_18():
    nombre = input("Ingresa tu nombre: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Nombre del cliente: {nombre} y la fecha y hora: {fecha}")

def ejercicio_19():
    numero = random.randint(1, 10)
    intento = 0
    while intento != numero:
        intento = int(input("Adivina el número (1-10): "))
    print("¡Adivinaste!")
    
def ejercicio_20():
    opciones = ["ir al cine", "estudiar", "hacer ejercicio"]

    def tomar_decision(prioridades):
        if not prioridades:
            return f"El agente decide: {', '.join(opciones)}"
        decisiones = [opcion for opcion in prioridades if opcion in opciones]
        return f"El agente decide: {', '.join(decisiones)}" if decisiones else "El agente no decide nada."

    prioridades = input("Ingrese sus prioridades separadas por coma: ").split(", ")

    print(tomar_decision(prioridades))

def ejercicio_21():
    class Agente:
        def __init__(self, nombre, ubicacion):
            self.nombre = nombre
            self.ubicacion = ubicacion

        def mover(self, nueva_ubicacion):
            self.ubicacion = nueva_ubicacion
            print(f"{self.nombre} se movió a {self.ubicacion}")

    # Crear agentes
    agente1 = Agente("Agente 1", input("Ingrese la ubicación inicial del Agente 1: "))
    agente2 = Agente("Agente 2", input("Ingrese la ubicación inicial del Agente 2: "))

    # Mover agentes según la entrada del usuario
    nueva_ubicacion1 = input("Ingrese la nueva ubicación del Agente 1: ")
    agente1.mover(nueva_ubicacion1)

    nueva_ubicacion2 = input("Ingrese la nueva ubicación del Agente 2: ")
    agente2.mover(nueva_ubicacion2)

    # Comprobar si se encontraron
    if agente1.ubicacion == agente2.ubicacion:
        print("Los agentes se han encontrado en el punto", agente1.ubicacion)
    else:
        print("Los agentes no se han encontrado")

def ejercicio_22():
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

def ejercicio_23():
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

def ejercicio_24():
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

def ejercicio_25():
    # Implementación simple de descenso de colina
    def funcion_objetivo(x):
        return x**2 - 4*x + 4  # Función cuadrática

    def descenso_colina(inicio, tasa_aprendizaje=0.1, iteraciones=100):
        x = inicio
        for _ in range(iteraciones):
            gradiente = 2*x - 4  # Derivada de la función
            x = x - tasa_aprendizaje * gradiente  # Actualización
        return x

    # Ejemplo de uso
    solucion = descenso_colina(0)
    print(f"La solución óptima es: {solucion}")
    
while True:
    print("\nMenú de ejercicios:")
    print("1. Ejercicio 1 - Temperaturas")
    print("2. Ejercicio 2 - Ticket de compra")
    print("3. Ejercicio 3 - Número Par")
    print("4. Ejercicio 4 - Calificaciones")
    print("5. Ejercicio 5 - Adivinar Número")
    print("6. Ejercicio 6 - Número Positivo/Negativo")
    print("7. Ejercicio 7 - Mayor que 10")
    print("8. Ejercicio 8 - Par o impar")
    print("9. Ejercicio 9 - Área de un círculo")
    print("10. Ejercicio 10 - Operaciones matemáticas")
    print("11. Ejercicio 11 - Suma de dos números")
    print("12. Ejercicio 12 - Datos personales")
    print("13. Ejercicio 13 - Información con cálculos")
    print("14. Ejercicio 14 - Información básica")
    print("15. Ejercicio 15 - Cálculo de edad en 5 años")
    print("16. Ejercicio 16 - Lista de frutas")
    print("17. Ejercicio 17 - Nodos enlazados")
    print("18. Ejercicio 18 - Fecha y nombre")
    print("19. Ejercicio 19 - Adivina el número")
    print("20. Ejercicio 20 - Agente Cognoscitivo")
    print("21. Ejercicio 21 - Agentes en movimiento")
    print("22. Ejercicio 22 - Heurística simple")
    print("23. Ejercicio 23 - BFS (Breadth-First Search)")
    print("24. Ejercicio 24 - Algoritmo A*")
    print("25. Ejercicio 25 - Descenso de colina")
    print("26. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        ejercicio_1()
    elif opcion == "2":
        ejercicio_2()
    elif opcion == "3":
        ejercicio_3()
    elif opcion == "4":
        ejercicio_4()
    elif opcion == "5":
        ejercicio_5()
    elif opcion == "6":
        ejercicio_6()
    elif opcion == "7":
        ejercicio_7()
    elif opcion == "8":
        ejercicio_8()
    elif opcion == "9":
        ejercicio_9()
    elif opcion == "10":
        ejercicio_10()
    elif opcion == "11":
        ejercicio_11()
    elif opcion == "12":
        ejercicio_12()
    elif opcion == "13":
        ejercicio_13()
    elif opcion == "14":
        ejercicio_14()
    elif opcion == "15":
        ejercicio_15()
    elif opcion == "16":
        ejercicio_16()
    elif opcion == "17":
        ejercicio_17()
    elif opcion == "18":
        ejercicio_18()
    elif opcion == "19":
        ejercicio_19()
    elif opcion == "20":
        ejercicio_20()
    elif opcion == "21":
        ejercicio_21()
    elif opcion == "22":
        ejercicio_22()
    elif opcion == "23":
        ejercicio_23()
    elif opcion == "24":
        ejercicio_24()
    elif opcion == "25":
        ejercicio_25()
    elif opcion == "26":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
