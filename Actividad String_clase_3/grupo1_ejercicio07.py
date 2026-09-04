#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# CONSIGNA
# a) Solicitar un teléfono tal como figura en la base.
# b) Eliminar los espacios, los guiones y los paréntesis.
# c) Mostrar el teléfono depurado y la cantidad de dígitos que quedaron

numero_telefono = input("Ingrese su telefono eje: (011) 1265-1235:  ")


numero_telefono_depurado = numero_telefono.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
cantidad_digitos_telefono_limpio = numero_telefono_depurado.__len__()

print(f"Su número de telefono es: {numero_telefono_depurado} // Cantidad de dígitos: {cantidad_digitos_telefono_limpio}" )