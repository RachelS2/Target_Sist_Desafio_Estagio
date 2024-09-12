import json
from pathlib import Path
import pandas as pd

DADOS_PATH = Path(r".\Target_Sist_Desafio_Estagio\questao3\dados.json")

with open(DADOS_PATH, 'r') as arquivo:
    dados = json.load(arquivo)

