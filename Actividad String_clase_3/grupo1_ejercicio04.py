#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# CONSIGNA
# a) Solicitar un número de documento de ocho dígitos.
# b) Mostrar el primer dígito, el último dígito y los tres dígitos centrales (posiciones 2, 3 y 4).
# c) Antes de escribir el programa, completar el diagrama de posiciones.

usuario_dni = input("Ingrese su DNI, máximo 8 dígitos: ")

primer_digito = usuario_dni[0]
ultimo_digito = usuario_dni[-1]


print(f"Tu primer dígito del DNI es: {primer_digito}")
print(f"Tu último dígito del DNI es: {ultimo_digito}")
print(f"Tus tres dígitos  del DNI es: {usuario_dni[2]}, {usuario_dni[3]}, {usuario_dni[4]}")


# if  len(usuario_dni) > 8:
#     print("Error, solo 8 dígitos")
# else:
#     print(f"Correcto. Tu DNI es: {usuario_dni}")





