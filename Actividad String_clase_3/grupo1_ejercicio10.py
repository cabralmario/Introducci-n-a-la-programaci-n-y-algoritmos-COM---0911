#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# a) Solicitar la cadena exportada.
# b) Separarla en una lista usando la coma como separador.
# c) Mostrar la cantidad de asistentes y la lista unida con el separador ' | '.

lista_alumnos = input("Ingrese la lista de asistensias: ")


lista_alumnos_ordenada = lista_alumnos.split(",")

cantidad_asistencia = lista_alumnos_ordenada.__len__()


print(f"cantidad asistencias: {cantidad_asistencia}")
print(f"Listodo: {lista_alumnos.replace(",", " | ")}")

