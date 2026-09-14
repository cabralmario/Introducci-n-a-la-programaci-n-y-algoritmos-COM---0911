#Apellido y nombre: Cabral mario 

#Curso / comisión: comision 11

#Fecha: 31/08/2026

# CONSIGNA
# a) Solicitar la fecha en formato compacto.
# b) Separar el año, el mes y el día usando cortes.
# c) Mostrar la fecha en el formato DD/MM/AAAA.

fecha_compacta = input("Ingrese la fecha sin espacio ni separadores (AAAAMMDD): ")

año= fecha_compacta[0:4]
mes= fecha_compacta[4:6]
día= fecha_compacta[6:8]

print(f"La fecha en formato DD/MM/AAAA es: {día}/{mes}/{año}")



