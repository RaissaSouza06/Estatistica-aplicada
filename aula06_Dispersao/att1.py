import pandas as pd

dados = [10, 12, 15, 18, 20]

serie = pd.Series(dados)

print(f"Média aritmética: {serie.mean()}")
print(f"Amplitude: {serie.max() - serie.min()}")
print(f"Variancia populacional: {serie.var(ddof=0)}")
print(f"Desvio padrão: {serie.std(ddof=0)}")