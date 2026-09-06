#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# a) Solicitar el título del informe y el código del área.
# b) Mostrar el título centrado en cuarenta caracteres, usando puntos como relleno.
# c) Mostrar el código del área alineado a la derecha en cuarenta caracteres.

solicitar_titulo = input("Ingrese el titulo del informe: ")
codigo_area = input("Ingrese codigo de área: ")
lineas = "-"*20
print(f"{lineas} {solicitar_titulo} {lineas}")
print(codigo_area)
