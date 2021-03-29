#Ejercicio3_1 Eliminar duplicados de una lista

lista = [1,2,3,"Alejandro",2,2,1,"Alejandro",3]
conjunto = set(lista)
lista = list(conjunto)
print(lista)

#otra forma
#lista = list(set(lista))