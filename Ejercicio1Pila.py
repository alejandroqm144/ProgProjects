

def operar(pila, operadores):
    for i in range(len(pila) - 1):
        elemento = pila.pop()
        if elemento in operadores:
            if len(pila) < 2:
                raise ValueError("Error: falta un operando")
            operand2 = float(pila.pop())
            operand1 = float(pila.pop())
            resultado = operadores[elemento](operand1, operand2)
            pila.append(resultado)

def evaluar_expresion(expresion, operadores):
    pila = []
    tokens = expresion.split()
    for token in tokens:
        if token in operadores:
            operar(pila, operadores)
        else:
            pila.append(float(token))
    while len(pila) > 1:
        operar(pila, operadores)
    if len(pila) == 1:
        return pila.pop()
    else:
        raise ValueError("Error: la expresión no está en notación posfija")

operadores = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

expresion = "3 4 5 + *"
resultado = evaluar_expresion(expresion, operadores)
print("El resultado de la expresión posfija ", expresion, " es: ", resultado)