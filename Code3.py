

class Pila:
    def __init__(self, capacidad_maxima):
        self.items = []
        self.capacidad_maxima = capacidad_maxima

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.capacidad_maxima

    def insertar(self, elemento):
        if not self.esta_llena():
            self.items.append(elemento)
            print(f"Se ha insertado {elemento} en la pila.")
        else:
            print("Error: La pila está llena.")

    def eliminar(self):
        if not self.esta_vacia():
            elemento_eliminado = self.items.pop()
            print(f"Se ha eliminado {elemento_eliminado} de la pila.")
            return elemento_eliminado
        else:
            print("Error: La pila está vacía.")

def main():
    pila = Pila(8)  # Capacidad máxima de la pila es 8

    operaciones = [
        ("Insertar", "X"),
        ("Insertar", "Y"),
        ("Eliminar", "Z"),
        ("Eliminar", "T"),
        ("Eliminar", "U"),
        ("Insertar", "V"),
        ("Insertar", "W"),
        ("Eliminar", "p"),
        ("Insertar", "R"),
    ]

    for operacion, elemento in operaciones:
        if operacion == "Insertar":
            pila.insertar(elemento)
        elif operacion == "Eliminar":
            pila.eliminar()

    elementos_restantes = len(pila.items)
    print(f"La pila tiene {elementos_restantes} elementos.")

main()
