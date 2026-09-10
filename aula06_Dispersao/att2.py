import pandas as pd

A = pd.Series([100, 100, 100, 100, 100])
B = pd.Series([80, 90, 100, 110, 120])

print(f"Média do grupo A: {A.mean()}")
print(f"Média do grupo B: {B.mean()}")

print(f"Variância amostral grupo A: {A.var(ddof=1)}")
print(f"Variância amostral grupo B: {B.var(ddof=1)}")

print(f"Variância populacional grupo A: {A.var(ddof=0)}")
print(f"Variância populacional grupo B: {B.var(ddof=0)}")

print(f"Desvio padrão da variancia amostral do grupo A: {A.std(ddof=1)}")
print(f"Desvio padrão da variancia amostral do grupo B: {B.std(ddof=1)}")

print(f"Desvio padrão da variancia populacional do grupo A: {A.std(ddof=0)}")
print(f"Desvio padrão da variancia populacional do grupo B: {B.std(ddof=0)}")

# Pergunta: Qual grupo apresenta maior dispersão de dados e por quê?






