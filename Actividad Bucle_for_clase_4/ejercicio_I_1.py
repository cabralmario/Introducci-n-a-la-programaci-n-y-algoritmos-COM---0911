# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11

# Ejercicio I.1. Numeración de aulas

# La bedelía del pabellón necesita imprimir un cartel por cada aula, numeradas.
# CONSIGNA:
# a) Mostrar los carteles de las aulas 1 a 10, uno por línea, utilizando range().
# b) Mostrar al final la cantidad total de carteles impresos.
# c) Indicar en un comentario los argumentos utilizados en range() (inicio, fin y paso).

#El ejercicio pide que se se imprima los carteles de las aulas del 1 al 10 
#Luego se tiene que ver la cantidad de carteles se imprimieron 
# comentar los argumentos que se ulilizaron en el range()



for numero in range(1,11):   # inicio 1 es donde empiza la vuelta, 11 es el fin como no se puede incluir este numero finaliza en 10, pasos 1 en 1 

    print(f"Aula: {numero}")

print(f"Total de aulas: {len(range(1,11))}")




