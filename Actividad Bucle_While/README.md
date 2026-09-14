🐍 Trabajo Práctico — Bucle while en Python

👤 Alumno: Mario Cabral
🎓 Comisión: 11
📘 Tema: Bucle while

📌 Descripción

Este trabajo práctico corresponde a la unidad del bucle while en Python. Su objetivo es aplicar los contenidos trabajados hasta el momento y comprender cómo funcionan las repeticiones controladas por una condición, los contadores, los acumuladores, las validaciones de datos, los valores centinela y los bucles anidados.

El trabajo está dividido en tres grupos de actividades, organizados en carpetas separadas para mantener una estructura clara y ordenada.

🧰 Contenidos permitidos

Para resolver las actividades se utilizan únicamente los contenidos desarrollados hasta la fecha:

🔹 Variables.

⌨️ Entrada de datos mediante input().

🔤 Cadenas de texto y sus métodos.

🖥️ Formato de salida.

📋 Listas.

🔀 Instrucción condicional if.

🔁 Bucle for.

🔄 Bucle while.

🚫 Restricciones importantes

❌ No deben utilizarse funciones definidas por el alumno con def, ya que ese tema todavía no fue abordado.

📄 Cada actividad debe resolverse en un archivo independiente con extensión .py.

⌨️ Todos los programas que soliciten datos deben utilizar input() sin texto de indicación dentro de los paréntesis.

🧪 Los ejemplos de ejecución son solamente ilustrativos: cada programa debe funcionar correctamente con cualquier dato válido del mismo tipo.

✍️ Si una actividad incluye un diagrama, cuadro de vueltas o cuadro comparativo, debe completarse a mano antes de escribir el código cuando así lo indique la consigna.

📎 Los diagramas y cuadros forman parte de la entrega.

👤 Cada archivo debe incluir al comienzo un comentario con el nombre del autor.

Ejemplo:

# Mario Cabral

🗂️ Organización del trabajo

El trabajo está separado en tres carpetas principales, una por cada grupo de actividades:

TP_while/
│
├── README.md
│
├── 📁 Grupo_I/
│   ├── ejercicio_I_1.py
│   ├── ejercicio_I_2.py
│   ├── ejercicio_I_3.py
│   ├── ...
│   └── ejercicio_I_15.py
│
├── 📁 Grupo_II/
│   ├── ejercicio_II_1.py
│   ├── ejercicio_II_2.py
│   ├── ejercicio_II_3.py
│   ├── ...
│   └── ejercicio_II_15.py
│
└── 📁 Grupo_III/
    ├── ejercicio_III_1.py
    ├── ejercicio_III_2.py
    ├── ejercicio_III_3.py
    ├── ...
    └── ejercicio_III_15.py

🟢 Grupo I — Actividades básicas

El Grupo I contiene las actividades básicas de resolución obligatoria.

📂 Los archivos están numerados desde:

ejercicio_I_1.py

hasta:

ejercicio_I_15.py

🟡 Grupo II — Actividades medias

El Grupo II contiene actividades de dificultad media y su resolución es voluntaria.

📂 Los archivos están numerados desde:

ejercicio_II_1.py

hasta:

ejercicio_II_15.py

🔵 Grupo III — Actividades para pensar

El Grupo III contiene actividades que se resuelven con la asistencia de una herramienta de Inteligencia Artificial.

🤖 El objetivo de este grupo no es solamente obtener una respuesta de la IA, sino también analizarla, probarla, detectar errores y corregirlos.

📂 Los archivos están numerados desde:

ejercicio_III_1.py

hasta:

ejercicio_III_15.py

📚 Contenidos trabajados

Durante el trabajo práctico se desarrollan los siguientes temas:

🔄 Estructura del while.

✅ Evaluación de la condición antes de cada vuelta.

↪️ Bloque indentado y regreso a la condición.

🔢 Contadores y acumuladores manejados manualmente.

🧠 Condiciones que no son comparaciones.

⚖️ Valores que Python considera verdaderos o falsos.

📋 Recorrido y vaciado de listas con pop().

♾️ Bucles infinitos y formas de evitarlos.

🛑 Instrucción break.

🔁 Patrón while True.

⏭️ Instrucción continue.

🔚 Cláusula else del while y su relación con break.

🔄🔄 Bucles while anidados.

🔃 Reinicio del contador interno.

🚩 Lectura de datos hasta un valor centinela.

✅ Validación de datos.

🔁 Repetición hasta obtener una entrada correcta.

🔢 Operaciones con dígitos.

➗ Resto de una división.

🧮 División entera.

⚔️ Diferencias entre while y for.

⚠️ Errores frecuentes a tener en cuenta

Durante la resolución de los ejercicios se debe prestar especial atención a los siguientes errores:

⚠️ Olvidar actualizar la variable utilizada en la condición del while.

♾️ Crear accidentalmente un bucle infinito.

🔃 No reiniciar el contador interno en un while anidado.

↕️ Colocar instrucciones en un orden incorrecto.

❓ Confundir el funcionamiento del else de un while.

🛑 Utilizar break en una condición que nunca puede cumplirse.

📋 Modificar una lista durante el recorrido sin controlar correctamente el índice.

♾️ Advertencia sobre bucles infinitos

Un bucle while continúa ejecutándose mientras su condición sea verdadera.

Antes de ejecutar un programa conviene preguntarse:

❓ ¿Qué línea dentro del bucle hace que la condición pueda llegar a ser falsa?

Si ninguna instrucción modifica la condición de salida, el programa puede quedar atrapado en un bucle infinito.

Ejemplo:

x = 5

while x > 0:
    print(x)

🚨 En este ejemplo x nunca cambia, por lo que la condición x > 0 siempre seguirá siendo verdadera.

Para detener manualmente un programa que quedó ejecutándose en un bucle infinito se puede utilizar:

Ctrl + C

⚠️ Las actividades III.1 y III.13 contienen bucles infinitos de manera intencional, por lo que deben leerse y analizarse antes de ejecutarlas.

✏️ Forma de trabajo

Cada actividad se resuelve en su archivo correspondiente. Por ejemplo:

Grupo_I/ejercicio_I_1.py

El código debe respetar la consigna de la actividad y utilizar solamente las herramientas permitidas en este trabajo práctico.

Cuando una consigna tenga varios puntos, se mantienen separados para facilitar la lectura. Ejemplo:

# CONSIGNA:
# a) Definir una variable con los minutos disponibles, en cinco.
# b) Mientras queden minutos, mostrar el aviso y descontar uno.
# c) Mostrar, al terminar el bucle, el mensaje de tiempo cumplido.
# d) Antes de escribir el programa, completar el cuadro de vueltas.

▶️ Ejecución de los programas

Los ejercicios pueden ejecutarse desde la terminal de Visual Studio Code.

Ejemplo:

python ejercicio_I_1.py

Si se está trabajando desde la carpeta principal, también puede indicarse la carpeta:

python Grupo_I/ejercicio_I_1.py

🎯 Objetivo general

El objetivo de este trabajo práctico es comprender el funcionamiento del bucle while, aprender a controlar correctamente sus repeticiones y poder identificar cuándo conviene utilizarlo en lugar de un for.

También se busca desarrollar la capacidad de leer, probar, analizar y corregir código, especialmente en las actividades del Grupo III donde se utiliza Inteligencia Artificial como herramienta de apoyo.

👨‍💻 Mario Cabral — Comisión 11
🐍 Programación en Python — Trabajo Práctico: Bucle while