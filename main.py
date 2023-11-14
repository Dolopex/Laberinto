import os
import random
from readchar import readkey, key
from functools import reduce

class Juego:
    def __init__(self, laberinto, posicion_inicial, posicion_final):
        self.laberinto = self.convertir_a_matriz(laberinto)
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final
        self.px, self.py = posicion_inicial
        self.laberinto[self.px][self.py] = 'P'

    def borrar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mover_personaje(self, direccion):
        nueva_px, nueva_py = self.px, self.py

        if direccion == key.DOWN:
            nueva_px += 1
        elif direccion == key.LEFT:
            nueva_py -= 1
        elif direccion == key.RIGHT:
            nueva_py += 1
        elif direccion == key.UP:
            nueva_px -= 1

        if (
            0 <= nueva_px < len(self.laberinto) and
            0 <= nueva_py < len(self.laberinto[0]) and
            self.laberinto[nueva_px][nueva_py] != '#'
        ):
            self.laberinto[self.px][self.py] = '.'
            self.px, self.py = nueva_px, nueva_py
            self.laberinto[self.px][self.py] = 'P'

    def jugar(self):
        while (self.px, self.py) != self.posicion_final:
            self.mostrar_mapa()
            direccion = readkey()

            if direccion in [key.DOWN, key.LEFT, key.RIGHT, key.UP]:
                self.mover_personaje(direccion)

    def mostrar_mapa(self):
        self.borrar_terminal()
        for fila in self.laberinto:
            print("".join(fila))

    def convertir_a_matriz(self, laberinto_str): #Parte 6
        return list(map(list, laberinto_str.split('\n')))



class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas

    def leer_mapa(self, nombre_archivo):
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)

        try:
            with open(path_completo, 'r') as file:
                lineas = file.readlines()

            # Concatenar las filas usando reduce
            mapa = reduce(lambda x, y: x + y, lineas[2:], "").strip() # Parte 6

            # Separar las dimensiones y posiciones inicial y final
            dimensiones = tuple(map(int, lineas[0].replace(',', ' ').split()))
            if len(dimensiones) != 4:
                raise ValueError("Las dimensiones y posiciones iniciales/finales del laberinto no son válidas.")

            filas, columnas, px, py = dimensiones
            posicion_inicial = (px, py)

            # Separar las coordenadas finales
            posicion_final = tuple(map(int, lineas[1].replace(',', ' ').split()))

            # Ajustar la dimensión del laberinto si es necesario
            while len(mapa.split('\n')) < filas:
                mapa += '\n' + ' ' * columnas

            return dimensiones, posicion_inicial, posicion_final, mapa.strip()

        except Exception as e:
            print(f"Error al leer el mapa: {e}")
            raise

    def obtener_mapa_aleatorio(self):
        archivos_mapas = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos_mapas)
        return self.leer_mapa(nombre_archivo)

    def iniciar_juego(self, dimensiones, posicion_inicial, posicion_final, mapa):
        filas, columnas, _, _ = dimensiones
        super().__init__(mapa, posicion_inicial, posicion_final)
        self.jugar()


def main():
    path_a_mapas = "carpeta_de_mapas"  
    juego_archivo = JuegoArchivo(path_a_mapas)
    
    Jugador = input("Escribe Tu Nombre: ")
    print(f"Bienvenido/a, {Jugador}")

    print("Probemos los controles: Muevete usando (UP, DOWN, LEFT, RIGHT). Y presiona n para sumar un número")
    print("Cuando estés listo, presiona UP para iniciar el laberinto.")

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
            try:
                dimensiones, posicion_inicial, posicion_final, mapa = juego_archivo.obtener_mapa_aleatorio()
                juego_archivo.iniciar_juego(dimensiones, posicion_inicial, posicion_final, mapa)
            except ValueError as e:
                print(f"Error al leer el mapa: {e}")
                continue

            if (juego_archivo.px, juego_archivo.py) == juego_archivo.posicion_final:
                print("Felicidades, Has completado el laberinto")
                break

        elif k == 'n':
            juego_archivo.borrar_terminal()
            print(f"Número actual: {numero}")
            numero += 1
            if numero > 50:
                numero = 0
        else:
            print(k)

if __name__ == "__main__":
    main()
