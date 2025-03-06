from nltk.sem.logic import Expression

# Inicializar el analizador de expresiones lógicas
read_expr = Expression.fromstring

# Definir constantes (nombres de personas)
antonia = read_expr('antonia')
israel = read_expr('israel')
alvaro = read_expr('alvaro')

# Definir predicados y relaciones
estudiante = read_expr('estudiante(antonia)')  
profesor = read_expr('profesor(israel)')  # Israel es profesor
amigo = read_expr('amigo(antonia, alvaro)')  

amigos_antonia_alvaro = read_expr('amigos(antonia, alvaro)')
amigos_israel_antonia = read_expr('no_son_amigos(israel, antonia)')
no_amigos_antonia_alvaro = read_expr('tienen_la_misma_edad(antonia, alvaro)')
trabajan_juntos_antonia_alvaro = read_expr('trabajan(antonia, alvaro)')
# Crear un conjunto de fórmulas (hechos lógicos)
formulas = [
    amigos_antonia_alvaro,
    amigos_israel_antonia,
    no_amigos_antonia_alvaro,
    trabajan_juntos_antonia_alvaro
    ]

# Imprimir las expresiones lógicas

for formula in formulas:
    print(f"{formula}")