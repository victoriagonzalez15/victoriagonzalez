from arbol_binario import BinaryTree


arbol_mcu = BinaryTree()


lista_personajes = [
    {"name": "Iron Man", "heroe": True},
    {"name": "Thanos", "heroe": False},
    {"name": "Capitán América", "heroe": True},
    {"name": "Red Skull", "heroe": False},
    {"name": "ulk", "heroe": True},
    {"name": "Hblack widow", "heroe": True},
    {"name": "Rocket raccon", "heroe": True},
    {"name": "Dotor strage", "heroe": True},
    {"name": "Doctor octopus", "heroe": True},
    {"name": "Deadpool", "heroe": True},
]

# Inserta los personajes en el árbol
for personaje in lista_personajes:
    arbol_mcu.insert_node(personaje["name"], personaje["heroe"])


nombre_buscar = "Iron Man"
nodo = arbol_mcu.search(nombre_buscar)
if nodo:
    es_heroe = nodo.other_values
    if es_heroe:
        print(f"{nombre_buscar} es un superhéroe.")
    else:
        print(f"{nombre_buscar} es un villano.")
else:
    print(f"No se encontró el personaje {nombre_buscar}.")


##b. listar los villanos ordenados alfabéticamente


def villanos_ordenados(root):
    if root is not None:
        if not root.other_values:
            print(root.value)
        villanos_ordenados(root.left)
        villanos_ordenados(root.right)


print("los villanos ordenados alfabetamente :")
villanos_ordenados(arbol_mcu.root)


# c. mostrar todos los superhéroes que empiezan con C;
def superheroe_empiean_C(root):
    if root is not None:
        if root.other_values and root.value.startswith("C"):
            print(root.value)
        superheroe_empiean_C(root.left)
        superheroe_empiean_C(root.right)


print("SH empiean con C:")
superheroe_empiean_C(arbol_mcu.root)


# d. determinar cuántos superhéroes hay el árbol;


def cuantos_super_heroes_hay(root):
    contador = 0
    if root is not None:
        if root.other_values is True:
            contador += 1
        contador += cuantos_super_heroes_hay(root.left)
        contador += cuantos_super_heroes_hay(root.right)
    return contador


print(f"Hay {cuantos_super_heroes_hay(arbol_mcu.root)} Superheroes")


# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
def modificar_nombre(root):
    nombre_mal_cargado = "Dotor strage"
    nombre_bien_escrito = "Doctor Strange"
    if root is not None:
        if root.value == nombre_mal_cargado:
            root.value = nombre_bien_escrito
        modificar_nombre(root.left)
        modificar_nombre(root.right)


modificar_nombre(arbol_mcu.root)

nodo_modoficado = arbol_mcu.search("Doctor Strange")
if nodo_modoficado:
    print(f"el nombre fue modoficado a :{nodo_modoficado.value}")
else:
    print("el nombre no se encontro")


arbol_mcu.inorden()

print()


# f. listar los superhéroes ordenados de manera descendente;
def superheroes_desendentes(root):
    if root is not None:
        superheroes_desendentes(root.right)

        if root.other_values:
            print(root.value)
        superheroes_desendentes(root.left)


# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:


superheroes_desendentes(arbol_mcu.root)
arbol_superheroe = BinaryTree()
arbol_villano = BinaryTree()


def dividir_arbol(root):
    if root is not None:
        if root.other_values:
            arbol_superheroe.insert_node(root.value, True)
        else:
            arbol_villano.insert_node(root.value, False)
        dividir_arbol(root.left)
        dividir_arbol(root.right)


dividir_arbol(arbol_mcu.root)
print()


# I. determinar cuántos nodos tiene cada árbol;
def contar_nodos(root):
    if root is not None:
        return 1 + contar_nodos(root.left) + contar_nodos(root.right)
    else:
        return 0


num_nodos_superheroes = contar_nodos(arbol_superheroe.root)
num_nodos_villanos = contar_nodos(arbol_villano.root)

print(f"en el nodo hay {num_nodos_superheroes} super heroes")
print(f"en el nodo hay{num_nodos_villanos} villanos en el nodo")

# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("superheroe ordenados")
arbol_superheroe.inorden()
print()
print("villanos ordenados")
arbol_villano.inorden()
