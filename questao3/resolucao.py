import json
from pathlib import Path
import pandas as pd

DADOS_PATH = Path(r"questao3\dados.json")

with open(DADOS_PATH, 'r') as arquivo:
    dados = json.load(arquivo)

df = pd.DataFrame(dados)
media = df['valor'].mean()

valor_max = df['valor'].max()
valor_min = df['valor'].min()

df_acima_media = df[df['valor'] > media]
dias_acima_media = len(df_acima_media)
print(f"\nMédia de faturamento mensal: R$ {media:.3f}\n")
print(f"O valor de faturamento foi maior do que a média em {dias_acima_media} dias do mês.")
print(f"O maior valor de faturamento do mês é: {valor_max}")
print(f"O menor valor de faturamento do mês é: {valor_min}")
