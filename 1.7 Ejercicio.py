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
