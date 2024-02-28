

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numb = int(input("Ingresa un número entero para calcular su factorial: "))

if numb < 0:
    print("El factorial no está definido para números negativos.")
else:
    print("El factorial de", numb, "es", factorial(numb))
