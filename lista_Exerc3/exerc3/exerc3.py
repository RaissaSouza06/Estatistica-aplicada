import pandas as pd

df = pd.read_csv("clientes.csv")

gastoMedio_populacao = df["Valor gasto"].mean()
print(gastoMedio_populacao)

amostra = df.sample(n=10, random_state=14)
gastoMedio_amostra1 = amostra["Valor gasto"].mean()
print(gastoMedio_amostra1)

amostra = df.sample(n=30, random_state=14)
gastoMedio_amostra2 = amostra["Valor gasto"].mean()
print(gastoMedio_amostra2)