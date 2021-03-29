#Ejercicio4_5 Factorial numero positivo

numero = int(input("Digite un numero: "))

while numero < 0:
    print("Error -> El numero no es positivo")
    numero = int(input("Digite un numero"))
7
#Calcular el facorial

factorial = 1
for i in range(1, numero+1):
    factorial *= i

print(f"\nEl factorial del numero {numero} es {factorial}")