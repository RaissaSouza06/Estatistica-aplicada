import pandas as pd

df = pd.read_csv("exerc5_CSV.csv")

df["Valor_estoque"] = df["Quantidade"] * df["Preço"]
print(df)

print(df.head())
print(df.info())
print(df["Preço"].mean())
print(df.loc[df["Preço"].idxmax()]) #Retorna a LINHA COMPLETA do produto mais caro
print(df.loc[df["Preço"].idxmin()]) #Retorna a LINHA COMPLETA do produto mais barato
print(df.sort_values("Valor_estoque"))
print(df[df["Quantidade"] < 5])
