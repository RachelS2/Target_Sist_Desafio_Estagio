import json
from pathlib import Path
import pandas as pd

DADOS_PATH = Path(r"questao3\dados.json")

with open(DADOS_PATH, 'r') as arquivo:
    dados = json.load(arquivo)

soma = 0
for item in dados:
    dia = item['dia']
    soma += item['valor']
