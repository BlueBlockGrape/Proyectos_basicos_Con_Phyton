#Ejercicio6_4 Factorial de un numero (Recursividad)

def factorial(num):
    if num > 0:
        resultado = num * factorial(num-1)
    else:
        resultado = 1
    return resultado

valor = factorial(5)
print(valor)
