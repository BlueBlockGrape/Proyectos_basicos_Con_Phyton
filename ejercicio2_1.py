#Ejercicio2_1

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

if num1%2 == 0 and num2%2 == 0:
    print("Ambos son numeros pares")
elif num1%2 == 0 and num2%2 != 0:
    print(f"{num1} en par")
elif num1%2 != 0 and num2%2 == 0:
    print("{num2} es par")
else:
    print("Ambos son numeros impares")