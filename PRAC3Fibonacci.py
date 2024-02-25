

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def main():
    try:
        n = int(input("Ingrese la cantidad de números de la serie de Fibonacci que desea generar: "))
        if n <= 0:
            print("Por favor ingrese un número entero positivo.")
            return
        series = fibonacci(n)
        print("La serie de Fibonacci hasta el término", n, "es:")
        print(series)
    except ValueError:
        print("Por favor ingrese un número entero.")

main()
