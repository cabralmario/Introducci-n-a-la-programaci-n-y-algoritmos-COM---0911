#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# a) Solicitar el nombre del producto, el precio unitario y la cantidad.
# b) Convertir el precio y la cantidad a número.
# c) Mostrar una línea de comprobante usando f-strings, con el total calculado, dos decimales y separador de miles.

nombre_producto = input("Ingrese nombre del producto: ")
precio_producto = input("Ingrese precio del producto: ")
cantidad_producto = input("Ingrese cantidad de producto: ")

precio_producto_convertido = float(precio_producto)
cantidad_producto_convertido = int(cantidad_producto)
total_producto_convertido = precio_producto_convertido * cantidad_producto_convertido 


print("="*30)
print(f"Nombre del preducto: {nombre_producto}")
print(f"Precio del preducto: {precio_producto_convertido:,.2f}")
print(f"cantidad del preducto: {cantidad_producto_convertido}")
print(f"Total: {total_producto_convertido:,.2f}")
print("="*30)
