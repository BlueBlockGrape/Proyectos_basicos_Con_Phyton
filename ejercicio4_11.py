#Ejercicio4_11 Agenda Telefónica
agenda = {}
while True:
    print("\t.:MENU:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una nueva opción de menu: "))
    print()
    if opcion == 1:
        nombre = input("Nombre del contacto: ")
        telefono = input("Numero de telefono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado")
        else:
            print("Ese nombre de contacto ya existe")
    elif opcion == 2:
        nombre = input("Nombre del contacto: ")
        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto eliminado")
        else:
            print("El contacto no existe")
    elif opcion == 3:
        print("\t.:Agenda de contactos:.")
        for clave,valor in agenda.items():
            print(f"Nobre: {clave},Telefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Se equivoco de opción")
    print()