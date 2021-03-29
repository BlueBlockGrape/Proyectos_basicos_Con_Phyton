#Ejercicio4_6 Tabla de multiplicar

numero = int(input("Digite un numero: "))
lista = []

for i in range (1,11):
    lista.append(i*numero)

print(f"\nTabla de multiplicar \n{lista}")
