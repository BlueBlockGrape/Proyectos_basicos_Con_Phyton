#Ejercicio3_2 Operaciones de conjuntos con listas

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

#Eliminar elementos repetidos
a = set(lista1)
b = set(lista2)

union = list(a|b)
soloA = list(a-b)
soloB = list(b-a)
interseccion = list(a&b)

print(f"Elementos en ambos {union}")
print(f"solo A {soloA}")
print(f"Solo B {soloB}")
print(f"Compartidos de A y B {interseccion}")