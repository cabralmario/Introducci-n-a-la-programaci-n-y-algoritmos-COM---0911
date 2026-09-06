#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# CONSIGNA
# a) Solicitar la palabra del cartel.
# b) Convertirla a mayúsculas.
# c) Mostrarla con un espacio entre cada letra.

palabra_cartel = input("Ingrese las palabras del cartel: ")

palabra_cartel_mayus = palabra_cartel.upper()

palabra_cartel_separada= " ".join(palabra_cartel_mayus)

print(f"{palabra_cartel_separada}")
