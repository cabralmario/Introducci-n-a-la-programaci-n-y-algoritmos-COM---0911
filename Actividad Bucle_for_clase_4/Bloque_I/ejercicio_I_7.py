# Nombre y apellido: Mario Alberto Cabral
# Comisión: 11
# Ejercicio I.7. Alumnos que promocionan
# La cátedra necesita saber cuántos alumnos alcanzaron la promoción directa, que se obtiene con
# siete o más.
# CONSIGNA
# a) Definir una lista con siete notas.
# b) Recorrerla y, con un if dentro del bucle, contar cuántas llegan a siete.
# c) Contar también cuántas no llegan.
# d) Mostrar ambos totales.
# EJEMPLO DE EJECUCIÓN
# Promocionan: 4
# No promocionan: 3

lista_notas = [7,8,9,3,4,5,6]
promocionan = 0 
no_promocionan = 0 
for notas in lista_notas:
    if notas >= 7:
         promocionan += 1
    else:
         no_promocionan +=1  
print(f"Promocionan: {promocionan}")
print(f"No promocionan: {no_promocionan}")
   

   

  
        
         
            

         
    
    