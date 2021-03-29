#Ejercicio4_4 Sumar números pares de un rango

a = int(input("Digite dónde va a comenzar: "))
b = int(input("Digite dónde va a finalizar"))
suma = 0

for i in range (a,b+1):
    if i%2 == 0: #Si es par
        suma += i
print(f"\nLa suma de numeros pares del rango es: {suma}")