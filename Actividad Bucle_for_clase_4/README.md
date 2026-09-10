# 🔄 Indicaciones Generales — Bucle `for`

La presente guía corresponde a la unidad del **bucle `for`** y se resuelve empleando únicamente los contenidos desarrollados hasta la fecha.

---

### 📌 Reglas de Resolución y Entrega

* **Contenidos permitidos:** Variables, entrada de datos (`input()`), cadenas de texto, listas, diccionarios, la instrucción condicional `if` y el bucle `for`.
* **⚠️ Restricciones importantes:** **No utilizar** el bucle `while` ni **funciones definidas por el alumno**, ya que dichos temas aún no han sido abordados en la materia.
* **Formato de archivos:** Cada ejercicio debe entregarse en un archivo independiente `.py`, siguiendo el formato de nombre:  
  `grupo1_ejercicioXX.py` *(Ejemplo: `grupo1_ejercicio05.py`)*.
* **Encabezado:** Todos los archivos deben incluir, en la primera línea, un comentario con el **Apellido y Nombre** del autor.
* **Pruebas de código:** Los ejemplos de ejecución en los enunciados son ilustrativos; el programa debe funcionar correctamente con cualquier dato del mismo tipo.
* **Diagramas y cuadros:** Los ejercicios que incluyan un diagrama o un cuadro requieren completarlo a mano antes de escribir el código, ya que forma parte de la entrega.

---

### 📚 Contenidos que Abarca la Guía

* **Estructura del `for`:** Encabezado, uso de dos puntos (`:`) y bloque indentado.
* **Función `range()`:** Manejo de argumentos de inicio, fin y paso.
* **Recorrido de Secuencias:** Iteración sobre listas, cadenas, tuplas y diccionarios.
* **Iterables e Iteradores:** Funciones `iter()`, `next()` y manejo de la excepción `StopIteration`.
* **Patrones Comunes:** Implementación del patrón **acumulador** y el patrón **contador**.
* **Condicionales en Bucles:** Filtrado durante el recorrido mediante la instrucción `if`.
* **Funciones Auxiliares de Iteración:**
  * `enumerate()`: Obtención simultánea de elemento y posición.
  * `zip()`: Recorrido simultáneo de dos o más secuencias.
* **Recorrido de Diccionarios:** Métodos `.keys()`, `.values()` y `.items()`.
* **Control de Flujo:** Instrucciones `break` y `continue`, y uso de la cláusula `else` asociada al `for`.
* **Bucles Anidados:** Recorrido de listas de listas y matrices.
* **Optimización y Modificaciones:**
  * Cortes (*slicing*) aplicados al recorrido: inversión y salteo de elementos.
  * Listas por comprensión (*list comprehensions*), con y sin condición.
* **Prevención de Errores Frecuentes:** Desfases en el conteo de `range()`, alcance de la variable de control posterior al bucle y modificación de listas durante el recorrido.