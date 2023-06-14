def contadorpalabra(vector, palabra):
    # En caso de que el vector este vacìo
    if not vector:
        return 0
    return (vector[0] == palabra) + contadorpalabra(vector[1:], palabra)


vector = ["Hola", "mesa", "Hola", "chau", "animal"]
palabra = "Hola"
contador = contadorpalabra(vector, palabra)
print("La palabra", palabra, "aparece", contador, "veces en el vector.")
