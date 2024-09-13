#5) Escreva um programa que inverta os caracteres de um string.

texto = list(input("Insira um texto: "))

otxet = []
for char in range(len(texto) -1, -1, -1):
    otxet.append(texto[char])

otxet_final = ""

for char in otxet:
    otxet_final += char

print(otxet_final)