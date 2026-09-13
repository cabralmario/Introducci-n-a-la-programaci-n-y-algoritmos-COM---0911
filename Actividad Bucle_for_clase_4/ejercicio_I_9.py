# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.9. Acta de calificaciones
# Los apellidos y las notas llegan en dos listas separadas, 
# en el mismo orden: el primer apellido corresponde a la primera nota.
# CONSIGNA
# a) Definir las dos listas, con cuatro elementos cada una.
# b) Recorrerlas al mismo tiempo utilizando zip().
# c) Mostrar una línea por alumno con su apellido y su nota.
# d) Indicar en un comentario qué ocurriría si una lista tuviera un elemento menos.
# EJEMPLO DE EJECUCIÓN
# Alvarez obtuvo 8
# Benitez obtuvo 4
# Cardozo obtuvo 10
# Duarte obtuvo 6
lista_apellidos = ["Alvarez","Benitez","Cardozo","Duarte"]
lista_notas = [6,7,9,8]

for apellido, notas in zip(lista_apellidos,lista_notas):
    print(f"{apellido} obtuvo {notas}")

#Cuando una lista tienen un elemento menos lo que hace zip()
#Es terminar el contador en la lista mas corta y el elemento sobrante de la otra lista no se muesta 
