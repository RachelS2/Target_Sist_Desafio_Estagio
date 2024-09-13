import json
from pathlib import Path
import pandas as pd

DADOS_PATH = Path(r"questao3\dados.json")

with open(DADOS_PATH, 'r') as arquivo:
    dados = json.load(arquivo)

soma = 0
qtd_dias = 0

valores = []
for item in dados:
    valor = item['valor']
    if (valor == 0.0):
        continue
    soma += valor
    qtd_dias += 1
    valores.append(item['valor'])

media = soma/qtd_dias
valor_max = max(valores)
valor_min = min(valores)


print(f"\nMédia de faturamento mensal: R$ {media:.3f}\n")
#print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_media} dias.")
print(f"O maior valor de faturamento do mês é: {valor_max}")
print(f"O menor valor de faturamento do mês é: {valor_min}")
