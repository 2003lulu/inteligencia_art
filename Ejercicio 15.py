import datetime
import os

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
print(f"Folio: {folio:04d}")  # Formato 0001, 0002, etc.
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
