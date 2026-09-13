# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.6. Promedio del cuatrimestre

# El sistema de gestión académica calcula el promedio de un alumno a partir de la lista de sus
# notas.
# CONSIGNA
# a) Definir una lista con cinco notas.
# b) Sumarlas con un acumulador dentro del bucle.
# c) Calcular el promedio dividiendo la suma por la cantidad de notas.
# d) Mostrar el promedio con dos decimales.
# EJEMPLO DE EJECUCIÓN
# Suma de notas: 35
# Promedio: 7.00

lista_notas = [6,7,8,5,9]
notas_completa = 0 

for i in lista_notas:
    notas_completa += i
promedio = notas_completa / len(lista_notas)
print(f"Suma de notas: {notas_completa}")
print(f"Promedio: {promedio:.2f}")



