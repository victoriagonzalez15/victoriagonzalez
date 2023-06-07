# Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
class Pila:
    def __init__(self):
        self._elementos = []

    def push(self, value):
        self._elementos.append(value)

    def pop(self):
        if self.size() > 0:
            return self._elementos.pop()

    def size(self):
        return len(self._elementos)

    def top(self):
        if self.size() > 0:
            return self._elementos[-1]


class Cola:
    def __init__(self):
        self._elementos = []

    def arrive(self, value):
        self._elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self._elementos.pop(0)

    def size(self):
        return len(self._elementos)

    def on_front(self):
        if self.size() > 0:
            return self._elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux

    def eliminar_notificacion_facebook(self):
        cola_aux = Cola()
        while self.size():
            notificaciones = self.atention()
            if notificaciones["app"] != "Facebook":
                cola_aux.arrive(notificaciones)
        self._elementos = cola_aux._elementos

    def mostrar_notificaciones(self):
        for notificacion in self._elementos:
            print(notificacion)

    def mostrar_notificacion_twiter(self):
        for notificacion in self._elementos:
            if notificacion["app"] == "twiter" and "python" in notificacion["mensaje"]:
                print(notificacion)


cola_notificaciones = Cola()
cola_notificaciones.arrive(
    {"hora": "11:30", "app": "Facebook", "mensaje": "Notificacion de facebook 1"}
)
cola_notificaciones.arrive(
    {"hora": "12:20", "app": "twiter", "mensaje": "notificacion de twiter 1 con python"}
)
cola_notificaciones.arrive(
    {"hora": "13:50", "app": "twiter", "mensaje": "notificacion twiter 2 python"}
)
cola_notificaciones.arrive(
    {"hora": "14:00", "app": "Facebook", "mensaje": "notificacion de facebook 2"}
)
cola_notificaciones.arrive(
    {"hora": "15:20", "app": "twiter", "mensaje": "notiicacion de twiter 3 python"}
)


# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

cola_notificaciones.eliminar_notificacion_facebook()
cola_notificaciones.mostrar_notificaciones()
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
print()
print("las notificaciones de twiter que contiene en el mensaje la palabra python")
cola_notificaciones.mostrar_notificacion_twiter()
print()
##c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.
pila_temporal = Pila()
cantidad_notificaciones = 0
while cola_notificaciones.size():
    notificaciones = cola_notificaciones.atention()
    if "11:43" <= notificaciones["hora"] <= "15:57":
        pila_temporal.push(notificaciones)
        cantidad_notificaciones += 1
print(
    "las notificaciones que estan comprendida entre las 11:43 y:15:57 son",
    cantidad_notificaciones,
)
