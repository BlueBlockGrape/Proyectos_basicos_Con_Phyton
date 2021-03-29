#ejercicio4_10 No repetir caracteres

cadena = input("Digite una cadena: ")
lista = []

for i in cadena:
    if i not in lista: #Si el carácter no está en la lista se agrega
        lista.append(i)
print(f"\nLista de caracteres sin repetir: \n{lista}")