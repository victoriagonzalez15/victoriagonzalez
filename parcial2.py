from arbol_binario import BinaryTree


pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": "Planta/Veneno"},
    {"nombre": "Ivysaur", "numero": 2, "tipo": "Planta/Veneno"},
    {"nombre": "Venusaur", "numero": 25, "tipo": "Planta/Veneno"},
]


nombre_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

for pokemon in pokemons:
    nombre = pokemon["nombre"]
    numero = pokemon["numero"]
    tipo = pokemon["tipo"]

    nombre_tree.insert_node(nombre, pokemon)
    numero_tree.insert_node(numero, pokemon)
    tipo_tree.insert_node(tipo, pokemon)


# a) Buscar Pokémon por número
def buscar_pokemon_por_numero(numero):
    result = numero_tree.search(numero)
    if result:
        print("Datos del Pokémon con número", numero)
        print(result.other_values)
    else:
        print("No se encontró un Pokémon con el número", numero)


buscar_pokemon_por_numero(25)


def buscar_pokemon_por_nombre(nombre):
    result = nombre_tree.search(nombre)
    if result:
        print("Pokémon(s) con nombre que contiene '{}'".format(nombre))
        for node in result:
            print(node.other_values)
    else:
        print(
            "No se encontró ningún Pokémon con un nombre que contiene '{}'".format(
                nombre
            )
        )


buscar_pokemon_por_nombre("Bul")


def nombres_de_pokemon_por_tipo(tipo):
    def inorden_tipo(root, tipo, result):
        if root is not None:
            inorden_tipo(root.left, tipo, result)
            if tipo in root.other_values:
                result.append(root.other_values)
            inorden_tipo(root.right, tipo, result)

    result = []
    inorden_tipo(tipo_tree.root, tipo, result)
    return result


tipo_a_buscar = "Planta/Veneno"
pokemons_de_tipo = nombres_de_pokemon_por_tipo(tipo_a_buscar)

if pokemons_de_tipo:
    print(f"Nombres de Pokémon de tipo {tipo_a_buscar}:")
    for pokemon in pokemons_de_tipo:
        print(f"Nombre: {pokemon[0]}, Número: {pokemon[1]}, Tipo: {pokemon[2]}")
else:
    print(f"No se encontraron Pokémon de tipo {tipo_a_buscar}")


def listado_orden_ascendente():
    print("Listado en orden ascendente por número:")
    numero_tree.inorden()
    print("\nListado en orden ascendente por nombre:")
    nombre_tree.inorden()


def listado_por_nivel():
    print("Listado por nivel por nombre:")
    nombre_tree.by_level()


listado_orden_ascendente()
listado_por_nivel()


def mostrar_datos_pokemon(nombre):
    result = nombre_tree.search(nombre)
    if result:
        for node in result:
            print("Datos de Pokémon '{}'".format(node.value))
            print(node.other_values.__dict__)
            print()
    else:
        print("No se encontró ningún Pokémon con el nombre '{}'".format(nombre))


pokemons_a_mostrar = ["Jolteon", "Lycanroc", "Tyrantrum"]
for nombre_pokemon in pokemons_a_mostrar:
    mostrar_datos_pokemon(nombre_pokemon)


def contar_pokemons_por_tipo(tipo):
    count = tipo_tree.contar(tipo)
    return count


tipo_electrico = "Eléctrico"
tipo_acero = "Acero"

pokemons_electricos = contar_pokemons_por_tipo(tipo_electrico)
pokemons_acero = contar_pokemons_por_tipo(tipo_acero)

print("Cantidad de Pokémon de tipo Eléctrico:", pokemons_electricos)
print("Cantidad de Pokémon de tipo Acero:", pokemons_acero)
