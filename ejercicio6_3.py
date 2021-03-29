#Ejercicio6_3 Menu para clientes

def agregar_cliente(clientes,nombre,apellido,dni):
    cliente={}
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    cliente['dni'] = dni
    clientes.append(cliente)

def mostrar_clientes(clientes):
    for i in clientes:
        print(f"Nombre:{i['nombre']} \nApellido:{i['apellido']} \nDNI:{i['dni']}")

def mostrar_cliente(clientes, dni):
    for i in clientes:
        if i['dni'] == dni:
            print(f"Nombre:{i['nombre']} \nApellido:{i['apellido']} \nDNI:{i['dni']}")
            return True
    return False

def eliminar_cliente(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            clientes.remove(i)
            return True
    return False

clientes = [] #Lista
while True:
    print("""\t.:MENU:.
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar Cliente
5. Salir""")
    opcion = int(input("Digite una opción: "))
    print()

    if opcion == 1:
        nombre = input("Nombre del cliente -> ")
        apellido = input("Apellido del cliente -> ")
        dni = input("DNI del cliente -> ")
        agregar_cliente(clientes,nombre,apellido,dni)
    elif opcion == 2:
        mostrar_clientes(clientes)
    elif opcion == 3:
        dni = input("DNI del cliente -> ")
        if mostrar_cliente(clientes,dni):
            print("Cliente encontrado")
        else:
            print("Cliente no encontrado")
    elif opcion == 4:
        dni = input("DNI del cliente -> ")
        if eliminar_cliente(clientes,dni):
            print("cliente eliminado")
        else:
            print("Cliente no encontrado")
    elif opcion == 5:
        break
    else:
        print("Error, Opcion no valida")
    print()