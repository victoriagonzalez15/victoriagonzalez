class Personaje:
    def __init__(self, superheroe, nombre_personaje, grupo, anio_aparicion):
        self.superheroe = superheroe
        self.nombre_personaje = nombre_personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion


class Lista:
    def __init__(self):
        self.__elements = []

    def insert(self, value):
        self.__elements.append(value)

    def search(self, search_value):
        for index, element in enumerate(self.__elements):
            if element.superheroe == search_value:
                return index
        return None

    def get_element_by_index(self, index):
        if 0 <= index < len(self.__elements):
            return self.__elements[index]
        return None


class Cola:
    def __init__(self):
        self.__elements = []

    def encolar(self, value):
        self.__elements.append(value)

    def desencolar(self):
        if not self.esta_vacia():
            return self.__elements.pop(0)
        return None

    def esta_vacia(self):
        return len(self.__elements) == 0

    def tamano(self):
        return len(self.__elements)


lista_personajes = Lista()

# Agregar personajes a la lista
lista_personajes.insert(Personaje("Superman", "Clark Kent", "Justice League", 1938))
lista_personajes.insert(Personaje("Batman", "Bruce Wayne", "Justice League", 1939))
lista_personajes.insert(
    Personaje("Wonder Woman", "Diana Prince", "Justice League", 1941)
)
lista_personajes.insert(Personaje("Flash", "Barry Allen", "Justice League", 1956))
lista_personajes.insert(
    Personaje("Green Lantern", "Hal Jordan", "Justice League", 1959)
)
lista_personajes.insert(Personaje("Aquaman", "Arthur Curry", "Justice League", 1941))
lista_personajes.insert(Personaje("Cyborg", "Victor Stone", "Justice League", 1980))
lista_personajes.insert(Personaje("Black Widow", "Natasha Romanoff", "Avengers", 1964))
lista_personajes.insert(Personaje("Thor", "Thor Odinson", "Avengers", 1962))
lista_personajes.insert(Personaje("Hulk", "Bruce Banner", "Avengers", 1962))
lista_personajes.insert(Personaje("Captain America", "Steve Rogers", "Avengers", 1941))
lista_personajes.insert(Personaje("Iron Man", "Tony Stark", "Avengers", 1963))
lista_personajes.insert(Personaje("Black Panther", "T'Challa", "Avengers", 1966))
lista_personajes.insert(Personaje("Spider-Man", "Peter Parker", "Avengers", 1962))
lista_personajes.insert(Personaje("Ant-Man", "Scott Lang", "Avengers", 1962))
lista_personajes.insert(Personaje("Wolverine", "Logan", "X-Men", 1974))
lista_personajes.insert(Personaje("Cyclops", "Scott Summers", "X-Men", 1963))
lista_personajes.insert(Personaje("Storm", "Ororo Munroe", "X-Men", 1975))
lista_personajes.insert(Personaje("Jean Grey", "Jean Grey", "X-Men", 1963))
lista_personajes.insert(Personaje("Gambit", "Remy LeBeau", "X-Men", 1990))
lista_personajes.insert(
    Personaje("Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976)
)

grupos = ["Los cuatro fantásticos", "Guardianes de la galaxia"]

capitana_marvel_index = lista_personajes.search("Capitana Marvel")

if capitana_marvel_index is not None:
    personaje = lista_personajes.get_element_by_index(capitana_marvel_index)
    print("El nombre del personaje de Capitana Marvel es:", personaje.nombre_personaje)
else:
    print("Capitana Marvel no está en la lista.")

# b. Almacenar los superhéroes que pertenezcan al grupo
# “Guardianes de la galaxia” en una cola e indicar cuántos son.
cola_guardianes = Cola()

for personaje in lista_personajes._Lista__elements:
    if personaje.grupo == "Guardianes de la galaxia":
        cola_guardianes.encolar(personaje)

# Mostrar la cantidad de superhéroes en la cola
print(
    "Cantidad de superhéroes en el grupo 'Guardianes de la galaxia':",
    cola_guardianes.tamano(),
)

# c. Mostrar de manera descendente los superhéroes que
# pertenecen al grupo “Los cuatro fantásticos” y “Guardianes de la galaxia”.
for grupo in grupos:
    print(f"Superhéroes del grupo '{grupo}' (en orden descendente):")
    for personaje in reversed(lista_personajes._Lista__elements):
        if personaje.grupo == grupo:
            print(personaje.superheroe)
    print()

# d. Listar los superhéroes que tengan nombre de personajes cuyo
# año de aparición sea posterior a 1960.
print("Superhéroes con nombre de personajes cuyo año de aparición es posterior a 1960:")
for personaje in lista_personajes._Lista__elements:
    if (
        personaje.nombre_personaje != personaje.superheroe
        and personaje.anio_aparicion > 1960
    ):
        print(personaje.superheroe)

# e. Hemos detectado que la superhéroe “Black Widow” está mal
# cargada por un error de tipeo, figura como “Vlanck Widow”,
# modifique dicho superhéroe para solucionar este problema.
# Corregir el nombre del superhéroe "Vlanck Widow" a "Black Widow"
for personaje in lista_personajes._Lista__elements:
    if personaje.superheroe == "Vlanck Widow":
        personaje.superheroe = "Black Widow"
        break

# Imprimir el nombre corregido del superhéroe "Black Widow"
for personaje in lista_personajes._Lista__elements:
    if personaje.superheroe == "Black Widow":
        print("Superhéroe corregido:", personaje.superheroe)
        break
# f. Dada una lista auxiliar con los siguientes personajes (‘Black
# Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
# información), agregarlos a la lista principal en el caso de no
# estar cargados.
# Lista auxiliar de personajes
lista_auxiliar = [
    Personaje("Black Cat", "Felicia Hardy", "", 1979),
    Personaje("Hulk", "", "Avengers", 1962),
    Personaje("Rocket Racoonn", "", "Guardianes de la galaxia", 1976),
    Personaje("Loki", "", "Avengers", 1962),
]

# Agregar los personajes de la lista auxiliar a la lista principal
for personaje_auxiliar in lista_auxiliar:
    if lista_personajes.search(personaje_auxiliar.superheroe) is None:
        lista_personajes.insert(personaje_auxiliar)

# Imprimir la lista de personajes actualizada
print("Lista de personajes actualizada:")
for personaje in lista_personajes._Lista__elements:
    print(personaje.superheroe)
# g. Mostrar todos los personajes que comienzan con C, P o S.
print("Personajes que comienzan con C, P o S:")
for personaje in lista_personajes._Lista__elements:
    if personaje.superheroe.startswith(("C", "P", "S")):
        print(personaje.superheroe)
