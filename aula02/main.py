import pandas as pd 

dados = {
    "Nome" : ["Ana", "Carlos", "João", "Felipe", "Marcos", "José"],
    "Idade" : [20, 25, 63, 10, 58, 25],
    "Nota": [10, 5, 9, 8, 7, 3]
}

df =pd.DataFrame(dados)

print(df.shape) #(x,y) -> exibe qtd de linhas e de colunas 
print(df.columns) # exibe as colunas
print(df['Nome']) # exibe apenas o indice nome, retorna os valores da coluna nome
print(df.Nome) # igual a print(df['Nome']) -> o resultado é uma séries
# series = estrutura do pandas que representa sequência de valores (uma única coluna)

print(df[["Nome", "Nota"]]) # retorna duas colunas

print(df.iloc[0]) #retorna os atributos do índice 0 
print(df.iloc[0:2]) #retorna do indice 0 até o 2 (0 e 1)
print(df.iloc[0,2]) #seleciona item da linha 0 e coluna 2 (1 e 3)

print(df["Nota"].max()) #mostra a maior nota
print(df["Nota"].min()) #mostra a menor nota
print(df["Nota"].mean()) #mostra a média das notas
print(df["Nota"].sum()) #mostra a soma das notas

df["Nota_Final"] = df["Nota"] + 1.3 #cria uma nova coluna
print(df)