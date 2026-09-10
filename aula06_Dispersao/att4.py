import pandas as pd

tempos = [110, 115, 120, 112, 118, 121, 117, 113, 119, 300]

serie = pd.Series(tempos)

print(f"Média de tempos: {serie.mean()}")
print (f"Mediana de tempos: {serie.median()}")
print(f"Amplitude de tempos: {serie.max()-serie.min()}")
print(f"Variancia de tempos: {serie.var(ddof=0)}")
print(f"Desvio padrão de tempos: {serie.std(ddof=0)}")

