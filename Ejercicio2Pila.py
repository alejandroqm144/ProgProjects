

class Pila:
    def _init_(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        destino.apilar(origen.desapilar())
        print("Mueve un disco de", origen, "a", destino)
    else:
        hanoi(n-1, origen, destino, auxiliar)
        destino.apilar(origen.desapilar())
        print("Mueve un disco de", origen, "a", destino)
        hanoi(n-1, auxiliar, origen, destino)


if _name_ == "_main_":
    pila_origen = Pila()
    pila_auxiliar = Pila()
    pila_destino = Pila()

    discos = 3
    for i in range(discos, 0, -1):
        pila_origen.apilar(i)

    print("Pasos a seguir para resolver el juego de las Torres de Hanoi:")
    hanoi(discos, pila_origen, pila_auxiliar, pila_destino)