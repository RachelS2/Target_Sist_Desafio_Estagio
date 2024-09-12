#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou 
# não a sequência.

n = int(input("\nInsira uma quantidade de números para a Sequência de Fibonacci: "))

inicio = 0
parte_da_sequencia = False
aux = 0
for contador in range(0, n/2):
    if (inicio == n or aux == n):
        parte_da_sequencia = True

    if (inicio == 0):
        aux = inicio + 1 
    else: 
        aux = inicio + aux
    print(aux) 
    inicio = inicio + aux