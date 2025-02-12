import datetime
nombre = input("ingresa tu nombre: ")
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"nombre del cliente. {nombre} y la fecha y hora: {fecha}")