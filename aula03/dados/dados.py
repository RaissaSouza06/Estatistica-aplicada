import pandas as pd

df=pd.read_csv("dados.csv")

nAmostra = 1000
amostra = df.sample(n=nAmostra, random_state=15)

# print(df.shape)
# print(df.head())

# amostra = df.sample(n=50) #cria uma amostra com 50 elementos
# print(amostra)

# amostra = df.sample(n=100, random_state=15) # random state define uma semente (seed) para o gerador de números aleatórios
# amostra = df.sample(n=100)

medPopulacao = df["idade"].mean() #calcula a média de idade da POPULAÇÃO
print(f"Média da população: {medPopulacao}") 

medAmostra = amostra["idade"].mean() #calcula média da idade da AMOSTRA
print(f"Média da amostra: {medAmostra}")

print(f"Erro amostral: {medPopulacao - medAmostra}")