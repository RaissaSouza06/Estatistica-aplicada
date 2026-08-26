import numpy as np
import pandas as pd

np.random.seed(15)

dados = {"Notas" : np.random.normal(70, 10, 10000)} #gera dez mil registros aleatórios, de 70 em 70 com desvio padrão de 10

df = pd.DataFrame(dados)

mediaPopulacao = df["Notas"].mean()
print(mediaPopulacao) 

amostra = df.sample(n=100, random_state=42)
mediaAmostra = amostra["Notas"].mean()

print(f"Média da população: {mediaPopulacao}")
print(f"Média da amostra: {mediaAmostra}")

for tamanho in [10, 50, 100, 500, 1000]:
    amostra = df.sample(n=tamanho, random_state=42)
    media = amostra["Notas"].mean()
    print(tamanho, media) #p um amostra de tamanho 50 a média é de 68.

# SAÍDA:
# 10 68.7726697143834
# 50 68.4346100229267
# 100 69.49645365222966
# 500 69.68953310545659
# 1000 69.76911624321548