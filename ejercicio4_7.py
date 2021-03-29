#Ejercicio4_7 Juego adivina el numero

import random
aleatorio = random.randint(0,100) #Genera numero aleatorio
print("\t.:Juego adivina el numero:.")
contador = 0
while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("No es el numero, digita uno menor")
    elif numero < aleatorio:
        print("\tNo es el numero, digita uno mayor")
    else:
        print(f"\tFelicidades adivinaste el numero {aleatorio}")
        break
print(f"\nNumero de intentos: {contador}")