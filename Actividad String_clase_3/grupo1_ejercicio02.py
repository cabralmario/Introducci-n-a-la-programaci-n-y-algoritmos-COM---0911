# Nombre y Apellido: Cabral Mario

# curso / comision : comision 11 

# a) Solicitar un nombre completo.
# b) Quitar los espacios sobrantes de los extremos.
#c) Mostrarlo en mayúsculas, minúsculas y formato de carnet.

nombre_completo = input("ingrese su nombre completo: ")

#print(f"Tu nombre con espacios: {nombre_completo}")

nombre_completo_sin_espacios = nombre_completo.strip()

nombre_completo_con_mayus = nombre_completo.upper().strip()

nombre_completo_en_minus = nombre_completo_con_mayus.lower().strip()

nombre_completo_formato_carnet = nombre_completo.title().strip()



print(f"Tu nombre completo sin espacios es: {nombre_completo_sin_espacios}")
print(f"Tu nombre completo con mayusculas es: {nombre_completo_con_mayus}")
print(f"Tu nombre completo en minuscula es: {nombre_completo_en_minus}")
print(f"Tu nombre completo en formato carnet es: {nombre_completo_formato_carnet}")