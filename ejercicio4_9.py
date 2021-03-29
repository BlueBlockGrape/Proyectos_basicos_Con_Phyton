#Ejercicio4_9 Frase sin espacios y contar

frase = input("Digite una frase: ")
frase2 = ""
for i in frase:
    if i != " ":
        frase2 += i;
frase = frase2
print(f"\nFrase final: {frase}")
print(f"\nN° de caracteres: {len(frase)}")