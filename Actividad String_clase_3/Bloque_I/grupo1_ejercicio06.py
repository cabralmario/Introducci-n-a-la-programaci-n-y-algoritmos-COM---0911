#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# CONSIGNA
# a) Solicitar el nombre y el apellido.
# b) Construir la dirección de correo respetando la regla.
# c) Mostrar la dirección obtenida.

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

nombre_apellido = nombre+ "." +apellido 
nombre_apellido_minus = nombre_apellido.lower().strip()
print(f"Tu correo electronico es: {nombre_apellido_minus}@unpilar.edu.ar")

