#Ejercicio5_3 Palabra o frase palindroma

cadena = input("Digite una cadena: ")

#Quitar espacios en blanco
cadena = cadena.replace(" ","")

#Invertir la cadena
cadena2 = cadena[::-1] #Cadena Invertida
print(cadena2)

if cadena == cadena2:
    print("La cadena es palindroma")
else:
    print("La cadena no es palindroma")