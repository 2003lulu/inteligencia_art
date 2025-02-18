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
    elif 22 <= temperatura_usuario < 24:
        lugar = "Putla"
        lugar2 = None 
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