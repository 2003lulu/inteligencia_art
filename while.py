import random
numero = random.randint(1, 10)
intento = 0
while intento != numero:
    intento = int(input("Adivina el número (1-10): "))
print("¡Adivinaste!")
