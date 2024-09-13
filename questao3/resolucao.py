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
    soma += item['valor']
    qtd_dias += 1
    valores.append(item['valor'])

media = soma/qtd_dias
valor_max = max(valores)
valor_min = min(valores)

print(f"O maior valor do mês é: {valor_max}")
print(f"O menor valor do mês é: {valor_min}")
