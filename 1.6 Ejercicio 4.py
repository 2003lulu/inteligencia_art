# Simulación de un agente cognoscitivo tomando decisiones basadas en criterios predefinidos
opciones = ["ir al cine", "estudiar", "hacer ejercicio"]

# Función para tomar decisiones basadas en prioridades del usuario
def tomar_decision(prioridades):
    if not prioridades:
        return f"El agente decide: {', '.join(opciones)}"
    decisiones = [opcion for opcion in prioridades if opcion in opciones]
    return f"El agente decide: {', '.join(decisiones)}" if decisiones else "El agente no decide nada."

# Solicitar prioridades al usuario
prioridades = input("Ingrese sus prioridades separadas por coma: ").split(", ")

# Imprimir la decisión del agente
print(tomar_decision(prioridades))
