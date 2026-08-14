import pandas as pd

loja = {
    "Produto" : ["Arroz", "Lamotrigina", "Dipirona", "Shampoo", "Bolacha", "Pasta", "Mucilon", "Feijão", "Lítio", "Trident"],
    "Categoria" : ["Comida", "Remédio", "Remédio", "Cabelo", "Comida", "Higiene", "Comida", "Comida", "Remédio", "Comida"],
    "Preco" : [5, 30, 10, 60, 7, 10, 90, 7, 110, 3],
    "Quantidade" : [9, 5, 8, 2, 15, 4, 93, 45, 23, 2]
}

df = pd.DataFrame(loja)

df["Valor_total"] = df["Preco"] * df["Quantidade"]
print(df)

print(df[df["Preco"] > 100]) 
print(df[df["Quantidade"] < 10])