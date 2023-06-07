class Cola:
    def __init__(self):
        self._elementos = []

    def arrive(self, personaje):
        self._elementos.append(personaje)

    def atention(self):
        if self.size() > 0:
            return self._elementos.pop(0)

    def size(self):
        return len(self._elementos)

    def on_front(self):
        if self.size() > 0:
            return self._elementos[0]


cola_personajes = Cola()
cola_personajes.arrive(
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"}
)
cola_personajes.arrive(
    {"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"}
)
cola_personajes.arrive(
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"}
)
cola_personajes.arrive(
    {"nombre": "Wanda Maximoff ", "superheroe": "Bruja escarlata", "genero": "F"}
)
cola_personajes.arrive({"nombre": "Zoe Saldaña", "superheroe": "Gamora", "genero": "F"})
cola_personajes.arrive({"nombre": "Bruce Banner", "superheroe": "Hulk", "genero": "M"})
cola_personajes.arrive(
    {"nombre": " Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"}
)
cola_personajes.arrive({"nombre": "Scott Lang", "superheroe": "At-man", "genero": "M"})
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
nombre_capitana_marvel = "nombre"
for personaje in cola_personajes._elementos:
    if personaje["superheroe"] == "Capitana Marvel":
        nombre_capitana_marvel = personaje["nombre"]
        break
print("el nombre de la Capitana Marvel es:", nombre_capitana_marvel)
# b. mostrar los nombre de los superhéroes femeninos;
super_heroes_femenino = []
for personaje in cola_personajes._elementos:
    if personaje["genero"] == "F":
        super_heroes_femenino.append(personaje["superheroe"])

print("los nombres de los personajes femeninos son", super_heroes_femenino)

# c. mostrar los nombres de los personajes masculinos;
super_heroes_masculinos = []
for personaje in cola_personajes._elementos:
    if personaje["genero"] == "M":
        super_heroes_masculinos.append(personaje["superheroe"])
print("los nombres de los personajes masculinos son", super_heroes_masculinos)
# d. determinar el nombre del superhéroe del personaje Scott Lang;
superheroe_scottLang = None
for personaje in cola_personajes._elementos:
    if personaje["nombre"] == "Scott Lang":
        superheroe_scottLang = personaje["superheroe"]
        break
print("El nombre del personaje de scott lang es:", superheroe_scottLang)
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
for personaje in cola_personajes._elementos:
    if personaje["nombre"][0] == "S":
        print("los nombres que comienzan con S son", personaje)
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
Carol_Danvers_se_encuentra_en_la_cola = None
for personaje in cola_personajes._elementos:
    if personaje["nombre"] == " Carol Danvers":
        Carol_Danvers_se_encuentra_en_la_cola = personaje["superheroe"]
        break
print("su nombre de super heroe es", Carol_Danvers_se_encuentra_en_la_cola)
