def __init__(self, planeta, objetivo, recompensa):
    self.planeta = planeta
    self.objetivo = objetivo
    self.recompensa = recompensa


class BitacoraMision:
    def __init__(self, planeta, objetivo, recompensa):
        self.planeta = planeta
        self.objetivo = objetivo
        self.recompensa = recompensa


class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None


def mostrar_planetas_visitados(bitacora):
    planetas_visitados = []
    while not bitacora.is_empty():
        mision = bitacora.pop()
        planetas_visitados.append(mision.planeta)

    # Mostrar los planetas visitados en el orden de las misiones
    for planeta in reversed(planetas_visitados):
        print(planeta)


def calcular_creditos_recaudados(bitacora):
    total_creditos = 0
    while not bitacora.is_empty():
        mision = bitacora.pop()
        total_creditos += mision.recompensa

    return total_creditos


def buscar_mision_han_solo(bitacora):
    mision_han_solo = None
    num_mision = 0
    while not bitacora.is_empty():
        mision = bitacora.pop()
        num_mision += 1
        if mision.objetivo == "Han Solo":
            mision_han_solo = mision
            break

    if mision_han_solo:
        print(
            f"Han Solo fue capturado en la misión {num_mision} en el planeta {mision_han_solo.planeta}"
        )
    else:
        print("No se encontró la misión de captura de Han Solo en la bitácora.")


# Crear una pila para almacenar la bitácora de misiones
bitacora_pila = Pila()

# Agregar misiones a la bitácora
bitacora_pila.push(BitacoraMision("Tatooine", "Bounty #1", 100))
bitacora_pila.push(BitacoraMision("Hoth", "Bounty #2", 200))
bitacora_pila.push(BitacoraMision("Bespin", "Bounty #3", 300))
bitacora_pila.push(BitacoraMision("Endor", "Han Solo", 500))
bitacora_pila.push(BitacoraMision("Coruscant", "Bounty #4", 400))

# a. Mostrar los planetas visitados en el orden de las misiones
print("Planetas visitados en el orden de las misiones:")
mostrar_planetas_visitados(bitacora_pila)

# Crear una pila para almacenar la bitácora de misiones
bitacora_pila = Pila()

# Agregar misiones a la bitácora
bitacora_pila.push(BitacoraMision("Tatooine", "Bounty #1", 100))
bitacora_pila.push(BitacoraMision("Hoth", "Bounty #2", 200))
bitacora_pila.push(BitacoraMision("Bespin", "Bounty #3", 300))
bitacora_pila.push(BitacoraMision("Endor", "Han Solo", 500))
bitacora_pila.push(BitacoraMision("Coruscant", "Bounty #4", 400))

# Copiar la pila para calcular los créditos sin vaciar la original
bitacora_copia = Pila()
while not bitacora_pila.is_empty():
    bitacora_copia.push(bitacora_pila.pop())

# Calcular los créditos galácticos recaudados en total
total_creditos = calcular_creditos_recaudados(bitacora_copia)
print(f"Total de créditos galácticos recaudados: {total_creditos}")

# Crear una pila para almacenar la bitácora de misiones
bitacora_pila = Pila()

# Agregar misiones a la bitácora
bitacora_pila.push(BitacoraMision("Tatooine", "Bounty #1", 100))
bitacora_pila.push(BitacoraMision("Hoth", "Bounty #2", 200))
bitacora_pila.push(BitacoraMision("Bespin", "Bounty #3", 300))
bitacora_pila.push(BitacoraMision("Endor", "Han Solo", 500))
bitacora_pila.push(BitacoraMision("Coruscant", "Bounty #4", 400))

# c. Determinar el número de la misión en la que capturó a Han Solo y el planeta
buscar_mision_han_solo(bitacora_pila)
