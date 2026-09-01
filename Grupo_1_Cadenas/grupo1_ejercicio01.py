#Apellido y nombre: Cabral mario 


#Curso / comisión: comision 11

#Fecha: 31/08/2026


#Ejercicio I.1 — Ficha de inscripción.

#Además, la primera línea del archivo tiene que ser un comentario con tu apellido y nombre.

#Solicitar nombre y apellido por separado.
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
#Armar el nombre completo en una sola variable, dejando un espacio entre ambos.

nombre_completo = nombre + " " + apellido 
#Mostrar el nombre completo.
print("Tu nombre completo es:", nombre_completo)

#Mostrar cuántos caracteres ocupa.
total_caracteres = len(nombre_completo)
print("Tu nombre completo tienen un  cantidad de caracteres de:", total_caracteres)

