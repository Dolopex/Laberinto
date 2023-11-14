1.1 El jugador se define mediante la variable "Jugador" 

1.2 Se le indica al Jugador escribir su nombre antes de empezar mediante el comando "input" 

1.3 Se da un mensaje de bienvenida 

2.1 Importamos la libreria "Readchar"

2.2 Se definen las teclas de movimiento (UP,DOWN,LEFT,RIGHT)

2.3 Cuando se presiona "UP" el bucle se termina

3.0 Se cambia el nombre del archivo de "Laberinto.py" a "main.py"

3.0.1 Se agregó la funcion de que otras teclas a parte de (UP,DOWN,LEFT,RIGHT) aparecieran en la terminal al momento de presionarlas

3.1 Se añade la libreria "OS"

3.2 Se define la funcion para borrar la terminal

3.3 Definimos "numero"

3.4 Se agrega una una posibilidad al codigo donde si se presiona la tecla "n" la terminal se borre y muestre un numero desde 0 a 50, borrando la terminal cada que se presione la tecla "n" y sumando "+1" al numero anterior.

4.0 Se corrigió la posicion de los imports

4.1 Se creó una variable donde se contiene el laberinto y esta pasa a ser una matriz y se define una funcion que lo muestra

4.2 Se define la posicion inicial y final con (Px, Py)

4.3 Se crea una funcion (mover_personaje) en la que se definen los movimientos modificando las coordenadas al presionar (Up,Down,Left,Right) respectivamente

4.4 Se crea una funcion (jugar) que muestre el laberinto y use la funcion de mover personaje para empezar a jugar

4.5 Al presionar "Up" se borra la terminal y me muestra el mapa del laberinto completamente funcional

4.6 Al completar el laberinto se muestra un mensaje de felicitaciones (no he podido hacer que el mensaje se muestre, me pueden ayudar con esto, por favor)

5.0 Al completar el laberinto salta el mensaje de felicitaciones

5.1 Se encapsula el juego usando la clase "Juego" y se le asignan los atributos de :laberinto, posicion inicial, posicion final y las funciones se le adjuntan a la clase

5.2 El juego se instancia y se ejecuta desde "main"

5.3 Se importa la libreria "random" para que se escoja un laberinto aleatoriamente

5.4 Se crea la carpeta "carpeta_de_mapas" donde se almaenan los archivos de mapa en formato "txt"

5.5 Se crea otra clase llamada "JuegoArchivo" la cual hereda de "Juego" la funcion para leer los archivos y hacer que las funciones de moverse, mensaje final, paredes y pasillo se ajusten a cada mapa

5.6 Se crea una funcion encargada de mostrar un "ValueError" si el formato del archivo del mapa es incorrecto, si no tiene las coordenadas correctas, si salta uno de estos errores hay unos condicionales que mostraran el archivo como un "str" que verifica que se lee bien pero que un error debe ser corregido antes de poder jugar

5.7 los archivos de mapas deben ser en formato txt y las 2 primerras lineas deben mostrar: (ancho,alto,posicion inicial y posicion final)

6.0 Se importa reduce desde functools

6.1 Se crea una funcion que convierta el mapa en una matriz

6.2 Nn la función "leer_mapa" se concatenan las filas con reduce
