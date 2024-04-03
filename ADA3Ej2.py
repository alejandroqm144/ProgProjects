

def eliminar_elementos_repetidos(postres):
    postres_sin_repetidos = {}
    for postre, ingredientes in postres.items():
        ingredientes_sin_repetidos = list(set(ingredientes))
        postres_sin_repetidos[postre] = ingredientes_sin_repetidos
    return postres_sin_repetidos


POSTRES = {
    "Pastel de chocolate": ["harina", "azúcar", "chocolate", "huevos", "mantequilla", "chocolate"],
    "Tarta de manzana": ["harina", "azúcar", "manzanas", "canela", "mantequilla", "canela"],
    "Helado de vainilla": ["leche", "nata", "azúcar", "vainilla", "azúcar"],
    "Brownie": ["harina", "azúcar", "chocolate", "huevos", "nueces", "nueces"],
}

POSTRES = eliminar_elementos_repetidos(POSTRES)
print(POSTRES)