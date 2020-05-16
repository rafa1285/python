precio = 3.49
descuento = 0.4
precioDescuento = precio * descuento

numeroBarras = input("Introduce el numero de barras vendidas:")
numeroBarras = float(numeroBarras)

print("Precio habitual: " + str(precio))
print("Descuento: " + str(precioDescuento))
print("Coste final: " + str(numeroBarras * precioDescuento))