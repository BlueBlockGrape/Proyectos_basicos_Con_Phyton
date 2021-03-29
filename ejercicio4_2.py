#Ejercicio4_2 Modificar elementos de una lista

lista = list(range(1,11))
print("lista original:")
for i in lista:
    print(i, end = "-")
valor = int(input("\nDigite un valor a multiplicar: "))
#Multiplicar todos los elementos de la lista
indice = 0
for i in lista:
    lista[indice] *= valor
    indice += 1

print(f"\nLista final de elementos multiplicados por {valor}")

for i  in lista:
    print(i, end = "-")

#Otra forma

#for indice, i in enumerate(lista):
#   lista[indice] *= valor