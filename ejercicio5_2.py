#Ejercicio5_2 Frase terminada en punto

cadena = input("Digite un a cadena: ")
if cadena.endswith('.'): #Si el ultimo caracter es .
    print("\nLa cadena finaliza con '.'")
else:
    print("\nLa cadena no finaliza con '.'")