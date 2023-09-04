#Importamos la libreria
import readchar

key = readchar.readkey()

#Definimos Jugador
Jugador = (input("Escribe Tu Nombre:"))
print(Jugador)
print(f"Bienvenido/a", Jugador) 

from readchar import readkey, key

while True:
  k = readkey()
    
  if k == key.DOWN:
      print("Abajo")
     
  if k == key.LEFT:
      print("Izquierda")
    
  if k == key.RIGHT:
      print("Derecha")
    
  if k == key.UP:
    print("Arriba")
    break
  