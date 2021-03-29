#Ejercicio6_2 Dibujar un rectangulo

def dibujar(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print("*",end="")
        print()

ancho = int(input("Digite el ancho: "))
alto = int(input("Digite el alto: "))
print()
dibujar(ancho,alto)