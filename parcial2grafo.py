from lista import Lista as ListaArista


class Grafo:
    def __init__(self, dirigido=False):
        self.__elements = []
        self.dirigido = dirigido

    def insert_vertice(self, nombre_personaje):
        if not self.search_vertice(nombre_personaje):
            self.__elements.append([nombre_personaje, ListaArista(), False])

    def insert_arista(self, nombre_personaje1, nombre_personaje2, cantidad_episodios):
        if self.search_vertice(nombre_personaje1) and self.search_vertice(
            nombre_personaje2
        ):
            # Agregar una arista entre los vértices con la cantidad de episodios
            pos1 = self.search_vertice(nombre_personaje1)
            pos2 = self.search_vertice(nombre_personaje2)
            self.get_element_by_index(pos1)[1].insert(
                nombre_personaje2, cantidad_episodios
            )
            self.get_element_by_index(pos2)[1].insert(
                nombre_personaje1, cantidad_episodios
            )

    def search_vertice(self, nombre_personaje):
        for index, vertex in enumerate(self.__elements):
            if vertex[0] == nombre_personaje:
                return index
        return None

    def get_element_by_index(self, index):
        return self.__elements[index]

    def obtener_aristas(self):
        aristas = []
        for vertice in self.__elements:
            nombre_personaje1 = vertice[0]
            adyacentes = vertice[1]
            for i in range(adyacentes.size()):
                arista = adyacentes.get_element_by_index(i)
                nombre_personaje2 = arista[0]  # Nombre del personaje como una cadena
                episodios = arista[1]  # Cantidad de episodios como un número
                aristas.append((nombre_personaje1, nombre_personaje2, episodios))
        return aristas


mi_grafo = Grafo(dirigido=False)
mi_grafo.insert_vertice("Luke Skywalker")
mi_grafo.insert_vertice("Han Solo")
mi_grafo.insert_vertice("Leia Organa")
mi_grafo.insert_arista("Luke Skywalker", "Han Solo", 3)
mi_grafo.insert_arista("Leia Organa", "Han Solo", 2)

aristas = mi_grafo.obtener_aristas()
for arista in aristas:
    personaje1, personaje2, episodios = arista
    print(f"{personaje1} y {personaje2} compartieron {episodios} episodios.")

    print(f"{personaje1} y {personaje2} compartieron {episodios} episodios.")


def kruskal_min_spanning_tree(grafo):
    arbol_expansion_minima = []

    aristas = grafo.obtener_aristas()
    aristas.sort(key=lambda x: x[2])
    vertices_visitados = set()

    for arista in aristas:
        personaje1, personaje2, episodios = arista

        if personaje1 not in vertices_visitados or personaje2 not in vertices_visitados:
            arbol_expansion_minima.append(arista)
            vertices_visitados.add(personaje1)
            vertices_visitados.add(personaje2)

    return arbol_expansion_minima


arbol_expansion_minima = kruskal_min_spanning_tree(mi_grafo)


nombre_yoda = "Yoda"


def contiene_yoda(arbol, nombre_personaje):
    for arista in arbol:
        personaje1, personaje2, _ = arista
        if nombre_personaje in (personaje1, personaje2):
            return True
    return False


if contiene_yoda(arbol_expansion_minima, nombre_yoda):
    print(f"El árbol de expansión mínima contiene a {nombre_yoda}.")
else:
    print(f"El árbol de expansión mínima NO contiene a {nombre_yoda}.")
