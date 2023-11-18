from arbol_binario import BinaryTree

# Crear un árbol binario para representar personajes del MCU
arbol_mcu = BinaryTree()

# Lista de personajes con sus nombres y si son superhéroes o villanos
lista_personajes = [
    {"name": "Iron Man", "heroe": True},
    {"name": "Thanos", "heroe": False},
    {"name": "Capitán América", "heroe": True},
    {"name": "Red Skull", "heroe": False},
    {"name": "Hulk", "heroe": True},
    {"name": "Black Widow", "heroe": True},
    {"name": "Rocket Raccoon", "heroe": True},
    {"name": "Doctor Strange", "heroe": True},
    {"name": "Doctor Octopus", "heroe": True},
    {"name": "Deadpool", "heroe": True},
]

# Insertar personajes en el árbol
for personaje in lista_personajes:
    arbol_mcu.insert_node(personaje["name"], personaje["heroe"])

# Buscar un personaje específico ("Iron Man") y mostrar si es superhéroe o villano
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


# Función para imprimir los villanos ordenados alfabéticamente
def villanos_ordenados(root):
    if root is not None:
        if not root.other_values:
            print(root.value)
        villanos_ordenados(root.left)
        villanos_ordenados(root.right)


print("Los villanos ordenados alfabéticamente:")
villanos_ordenados(arbol_mcu.root)


# Función para imprimir superhéroes que empiezan con 'C'
def superheroe_empieza_con_C(root):
    if root is not None:
        if root.other_values and root.value.startswith("C"):
            print(root.value)
        superheroe_empieza_con_C(root.left)
        superheroe_empieza_con_C(root.right)


print("Superhéroes que empiezan con 'C':")
superheroe_empieza_con_C(arbol_mcu.root)


# Función para contar cuántos superhéroes hay en el árbol
def cuantos_super_heroes_hay(root):
    contador = 0
    if root is not None:
        if root.other_values is True:
            contador += 1
        contador += cuantos_super_heroes_hay(root.left)
        contador += cuantos_super_heroes_hay(root.right)
    return contador


print(f"Hay {cuantos_super_heroes_hay(arbol_mcu.root)} Superhéroes.")


# Función para modificar el nombre de "Dotor strage" a "Doctor Strange"
def modificar_nombre(root):
    nombre_mal_cargado = "Dotor strage"
    nombre_bien_escrito = "Doctor Strange"
    if root is not None:
        if root.value == nombre_mal_cargado:
            root.value = nombre_bien_escrito
        modificar_nombre(root.left)
        modificar_nombre(root.right)


# Modificar el nombre
modificar_nombre(arbol_mcu.root)

# Verificar que el nombre fue modificado correctamente
nodo_modificado = arbol_mcu.search("Doctor Strange")
if nodo_modificado:
    print(f"El nombre fue modificado a: {nodo_modificado.value}")
else:
    print("El nombre no se encontró.")

# Mostrar el recorrido inorden del árbol modificado
arbol_mcu.inorden()


# Función para imprimir superhéroes en orden descendente
def superheroes_descendentes(root):
    if root is not None:
        superheroes_descendentes(root.right)
        if root.other_values:
            print(root.value)
        superheroes_descendentes(root.left)


print("Superhéroes ordenados de manera descendente:")
superheroes_descendentes(arbol_mcu.root)

# Crear árboles separados para superhéroes y villanos
arbol_superheroe = BinaryTree()
arbol_villano = BinaryTree()


# Función para dividir el árbol original en superhéroes y villanos
def dividir_arbol(root):
    if root is not None:
        if root.other_values:
            arbol_superheroe.insert_node(root.value, True)
        else:
            arbol_villano.insert_node(root.value, False)
        dividir_arbol(root.left)
        dividir_arbol(root.right)


# Dividir el árbol
dividir_arbol(arbol_mcu.root)


# Función para contar nodos en un árbol
def contar_nodos(root):
    if root is not None:
        return 1 + contar_nodos(root.left) + contar_nodos(root.right)
    else:
        return 0


# Contar nodos en los árboles de superhéroes y villanos
num_nodos_superheroes = contar_nodos(arbol_superheroe.root)
num_nodos_villanos = contar_nodos(arbol_villano.root)

print(f"En el árbol hay {num_nodos_superheroes} superhéroes.")
print(f"En el árbol hay {num_nodos_villanos} villanos.")

# Mostrar recorrido inorden de superhéroes y villanos
print("Superhéroes ordenados:")
arbol_superheroe.inorden()
print("Villanos ordenados:")
arbol_villano.inorden()
