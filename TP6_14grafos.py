# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.
from grafo import Grafo
from grafo import Grafo
from random import randint


class Ambiente:
    def __init__(self, nombre):
        self.nombre = nombre


mi_grafo = Grafo(dirigido=False)

ambientes = [
    Ambiente("cocina"),
    Ambiente("comedor"),
    Ambiente("cochera"),
    Ambiente("quincho"),
    Ambiente("baño1"),
    Ambiente("baño2"),
    Ambiente("habitacion1"),
    Ambiente("habitacion2"),
    Ambiente("sala de estar"),
    Ambiente("terraza"),
    Ambiente("patio"),
]

for ambiente in ambientes:
    mi_grafo.insert_vertice(ambiente.nombre)

for i in range(len(ambientes)):
    puntoA = mi_grafo.get_element_by_index(i)
    for j in range(i + 1, len(ambientes)):
        puntoB = mi_grafo.get_element_by_index(j)
        valor = randint(1, 11)
        mi_grafo.insert_arist(puntoA[0], puntoB[0], valor)

# Se insertan aristas manualmente para cumplir condición de que dos habitaciones tengan 5 aristas
mi_grafo.insert_arist("patio", "cochera", randint(1, 11))
mi_grafo.insert_arist("cochera", "sala de estar", randint(1, 11))
mi_grafo.insert_arist("baño1", "comedor", randint(1, 11))
mi_grafo.insert_arist("comedor", "terraza", randint(1, 11))

mi_grafo.barrido()

# Se obtiene el árbol de expansión mínima
arbol_min = mi_grafo.kruskal()

cable = sum(
    int(arista.split("-")[2]) for arbol in arbol_min for arista in arbol.split(";")
)
print(
    f"El total de cables necesario para conectar todos los ambientes es: {cable} metros"
)

# Se determina el camino más corto desde la habitación 1 hasta la sala de estar
camino = mi_grafo.dijkstra("habitacion1", "sala de estar")
ultimo_paso = camino.pop()
while ultimo_paso[0] != "sala de estar":
    ultimo_paso = camino.pop()

print(
    f"Para conectar habitacion1 y sala de estar son necesarios: {ultimo_paso[1]} metros"
)
