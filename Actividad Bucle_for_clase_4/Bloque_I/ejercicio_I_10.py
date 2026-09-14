# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.10. Búsqueda en el padrón
# El sistema de acceso al examen busca un apellido en el padrón. Una vez encontrado, no tiene
# sentido seguir revisando el resto de la lista.
# CONSIGNA
# a) Definir un padrón con cinco apellidos y solicitar el apellido buscado.
# b) Recorrer el padrón mostrando cada apellido que se revisa.
# c) Cortar el bucle con break en cuanto se encuentre el apellido, e informarlo.
# d) Indicar en un comentario cuántas vueltas se ahorraron respecto de recorrer el padrón
# completo.
# EJEMPLO DE EJECUCIÓN
# Datos ingresados: «Cardozo»
# Reviso: Alvarez
# Reviso: Benitez
# Reviso: Cardozo
# Encontrado: Cardozo

patron_apellidos = ["Alvarez","Benitez","Cardozo","Duarte","Escobar"]

apellido_buscado = input("Ingrese el apellido buscado: ")


for buscar in patron_apellidos:
    print(f"Reviso: {buscar}")
    if buscar == apellido_buscado:
            break
print(f"Encontrado: {buscar}")
    
# Te ahorras las vueltas donde el break ya encuentra lo que busca
# El ejemplo cardozo se encontro en la 3ra vuelta por lo que se ahorro dos vueltas 

