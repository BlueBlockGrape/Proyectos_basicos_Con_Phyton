#Ejercicio4_1 Llenar una lista

lista = []
i = 1
while i <= 50:
    lista.append(i)
    i += 1
#Imprimiendo elementos de la lista
for i in lista:
    print(i,end="-")

#Otra forma

#lista = list(range(1,51)) #del 1 al 50

#for i in lista:
#    print(i,end="-")