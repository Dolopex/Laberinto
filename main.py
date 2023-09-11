#Importamos la libreria
import readchar
import os

key = readchar.readkey()

# Definimos la función para borrar la terminal
def borrar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Definimos Jugador
Jugador = (input("Escribe Tu Nombre:"))
print(Jugador)
print(f"Bienvenido/a", Jugador) 

#Definimos Teclas de movimiento
print("Muevete usando (UP,DOWN,LEFT,RIGHT)")

from readchar import readkey, key #No puedo subir este "import", si lo hago el codigo no funciona, como lo puedo solucionar?

numero = 0

while True:
  k = readkey()
 
  if k == key.DOWN:
      print("Abajo")
     
  elif k == key.LEFT:
      print("Izquierda")
    
  elif k == key.RIGHT:
      print("Derecha")
      
  elif k == key.UP:
    print("Arriba")
    break
  
  elif k == 'n':
    borrar_terminal()  # Borra la terminal
    print(f"Número actual: {numero}")
    numero += 1
    if numero > 50:
     numero = 0  # Reinicia el número a 0
  else:
       print(k)


