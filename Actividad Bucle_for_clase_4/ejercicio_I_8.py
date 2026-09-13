# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.8. Listado numerado de la comisión

# El acta de examen exige que cada alumno figure con su número de orden, empezando por el uno. 4
# El bucle for · Guía de ejercicios 

# CONSIGNA 
# a) Definir una lista con cuatro apellidos. 
# b) Mostrar el listado numerado utilizando enumerate() con start igual a uno. 
# c) Volver a mostrar el mismo listado, ahora con una variable contadora propia. 
# d) Indicar en un comentario cuál de las dos versiones prefiere y por qué. 
# EJEMPLO DE EJECUCIÓN 
# 1 Alvarez 
# 2 Benitez 
# 3 Cardozo 
# 4 Duarte 
# --- 
# 1 Alvarez 
# 2 Benitez 
# 3 Cardozo 
# 4 Duarte 
lista_apellidos = ["Alvarez","Benitez","Cardozo","Duarte"]

for lugar,apellido in enumerate(lista_apellidos, start=1):
    print(f"{lugar} {apellido}")

lineas = "-" * 7
print(lineas)

lugar_apellido = 1 

for apellido  in lista_apellidos:
    print(f"{lugar_apellido} {apellido}")
    lugar_apellido += 1
# Me parecio ambas formas iguales pero con la funcion enumerate() es mas corta, 
# no tengo que recordar que debo sumarle 1 o de donde arranque el contador  




