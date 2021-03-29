#Ejercicio6_1 Cambio de divisas

def cambio_Pesos_Dolares(pesos):
    return pesos/21.34

def cambio_Dolares_Pesos(dolares):
    return dolares*21.34

while True:
    print("""\t.:MENU:.
1.convertir Pesosa dolares
2. Convertir Dolares a Pesos
3. Salir""")
    opcion = int(input("Digite una opción: "))
    print()

    if opcion == 1:
        pesos = float(input("Digite la cantidad de pesos: "))
        print(f"Dólares -> ${cambio_Pesos_Dolares(pesos):.2f}")
    elif opcion == 2:
        dolares = float(input("Digite la cantidad de dólares: "))
        print(f"Pesos -> ${cambio_Dolares_Pesos(dolares):.2f}")
    elif opcion == 3:
        break
    else:
        print("Se equivocó de opción")
    print()