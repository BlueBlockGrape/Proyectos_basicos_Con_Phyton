#Ejercicio2_5
saldo = 1000
print("\t.:MENU:.")
print("1. Ingresar dinero a la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Digite una opcion de menu: "))
print()

if opcion == 1:
    extra = float(input("Cuánto dindero desea ingresar: "))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 2:
    retirar = float(input("Cuánto dinero desea retirar: "))
    if retirar > saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 4:
    print("Gracias por utilizar el cajero")
else:
    print("Error, se equivoco de opcion de menú")