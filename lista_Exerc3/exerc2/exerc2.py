import pandas as pd

df = pd.read_csv("alunos.csv")

media_populacao = df["Idade"].mean()
print(media_populacao)

amostra = df.sample(n=5, random_state=15)
media_amostra = amostra["Idade"].mean()
print(media_amostra)

amostra = df.sample(n=10, random_state=15)
media_amostra = amostra["Idade"].mean()
print(media_amostra)


