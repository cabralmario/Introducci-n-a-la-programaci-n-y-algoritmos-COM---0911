#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# CONSIGNA
# a) Solicitar el texto del reclamo.
# b) Solicitar la palabra que se desea buscar.
# c) Mostrar cuántas veces aparece y la posición de la primera aparición.


texto_de_reclamo = input("Igrese su reclamo: ")

palabra_clave = input("¿Que palabra desea buscar: ")

x = texto_de_reclamo.count(palabra_clave)

print(x)

                         