import pandas as pd

A = pd.Series([100, 102, 98, 101, 99])
B = pd.Series([70, 130, 90, 110, 100])

print(f"Média do grupo A: {A.mean()}")
print(f"Média do grupo B: {B.mean()}")

amp_a = A.max() - A.min()
print(f"Amplitude do grupo A: {amp_a}")
amp_b = B.max() - B.min()
print(f"Amplitude do grupo B: {amp_b}")

print(f"Desvio padrão da variancia populacional do grupo A: {A.std(ddof=0)}")
print(f"Desvio padrão da variancia populacional do grupo B: {B.std(ddof=0)}")

# Análise: Qual dos servidores apresenta maior estabilidade e previsibilidade de serviço 
# para o cliente final? Justifique detalhadamente com os números
# o servidor A é mais estavel (desvio padrão é menor do que do de B)





