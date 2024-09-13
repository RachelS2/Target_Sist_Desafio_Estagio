#Escreva um programa na linguagem que desejar onde calcule o percentual de 
# representação que cada estado teve dentro do valor total mensal da distribuidora.  

estado_faturamento = {"SP": 67836.43, "RJ":36678.66, "MG": 29229.88, "ES": 27165.48, 
                      "Outros": 19849.53}

apenas_valores = list(estado_faturamento.values())
soma_total = sum(apenas_valores)

print("\n")
for estado, valor in estado_faturamento.items():
    percentual = (valor/soma_total) * 100
    print(f"O estado de {estado} ocupa {percentual:.2f}% do valor total mensal da distribuidora.\n")