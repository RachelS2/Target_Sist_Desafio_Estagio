#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou 
# não a sequência.

n = int(input("Insira uma quantidade de números para a Sequência de Fibonacci: "))

inicio = 0

check = False

for contador in range(0, n):
    print(inicio) 
    if (inicio == 0):
        aux = inicio + 1 
    else: 
        aux = inicio + aux
    print(aux) 

    if (n == inicio or n == aux):
        check = True

    inicio = inicio + aux

if (check == True):
    print(f"O número escolhido ({n}) pertence à Sequência de Fibonacci!")
else:
    print(f"O número escolhido ({n}) NÃO pertence à Sequência de Fibonacci!")