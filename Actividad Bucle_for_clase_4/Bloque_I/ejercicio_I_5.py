# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.5. Cuenta de la fotocopiadora
# El centro de estudiantes lleva registro de lo que gasta cada mes en fotocopias. Los importes
# llegan en una lista y hay que sumarlos.
# 3
# El bucle for · Guía de ejercicios
# CONSIGNA
# a) Definir una lista con cuatro importes.
# b) Sumarlos utilizando una variable acumuladora preparada antes del bucle.
# c) Mostrar la cantidad de comprobantes y el total a pagar.
# d) Antes de escribir el programa, completar el cuadro de acumulación.

lista_importes = [250, 1800, 640, 310]
importes = 0 

for i in lista_importes:
    importes += i
print(f"Fotocopias del mes: {len(lista_importes)}")
print(f"Total a pagar: {importes}")