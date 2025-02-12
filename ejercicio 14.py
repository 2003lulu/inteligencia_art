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