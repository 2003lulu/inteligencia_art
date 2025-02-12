import random

num_ale = random.randint(1, 10)
adivina = int(input("adivina el nuemero entre 1 y 10: "))
print(f"el num aleatorio es {num_ale}.")
if adivina == num_ale:
    print("correcto. has adivinado el numero.")
else:
    print(f"incorrecto. el numero era {num_ale}.")