# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.2. Turnos del laboratorio
# CONSIGNA
# a) Solicitar la hora de inicio y la hora de fin, y convertirlas a número entero.
# b) Mostrar cada turno de dos horas utilizando el tercer argumento de range().
# c) Contar los turnos generados y mostrar la cantidad al final.

hora_inicio = int(input("Ingrese hora de incio: "))
hora_fin = int(input("Ingrese la horario de cierre: "))

hora_inicio_fin = range(hora_inicio, hora_fin, 2)
cantidad = 0

for i in hora_inicio_fin:
    print(f"Turno de {i} a {i+2}")
    cantidad += 1
print(f"Cantidad de turnos: {cantidad}")
