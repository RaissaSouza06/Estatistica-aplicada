import pandas as pd 

dados = {
    "Produto" : ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "Categoria" : ["Periférico", "Periférico", "Vídeo", "Vídeo", "Vídeo"],
    "Preço" : [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

df =pd.DataFrame(dados)

print(df)
print(df.shape) # retorna nº de Linha x Coluna
print(df.info())
print(df.describe())
print(df[["Produto", "Preço"]])
print(df.head(2))
print(df["Preço"].max())

#criando uma nova tabela a partir do calculo de outras duas
df["Valor_total"] = df["Quantidade"] * df["Preço"]
print(df)
