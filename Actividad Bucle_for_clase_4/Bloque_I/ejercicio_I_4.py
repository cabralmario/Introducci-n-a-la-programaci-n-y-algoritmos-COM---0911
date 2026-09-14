# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.4. Deletreo del apellido
# En mesa de entradas, cuando un trámite se hace por teléfono, el apellido se deletrea letra por
# letra para evitar errores de carga.
# CONSIGNA
# a) Solicitar un apellido.
# b) Mostrar cada letra en una línea, en mayúscula.
# c) Mostrar la cantidad de letras que tiene el apellido.
# d) Indicar en un comentario qué toma la variable del for en cada vuelta: una posición o una letra

apellido = input("Ingrese su apellido: ")

for letra in apellido:  # El for aqui toma letra por letra del apellido 
    print(letra.upper())

print(f"Cantidad de letras: {len(apellido)}")
