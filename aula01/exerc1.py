import pandas as pd

dados = {
    "Nome": ["João", "Maria", "Pedro", "Ana"],
    "Idade": [18, 20, 19, 22]
}

df = pd.DataFrame(dados)

print(df) #exibir o dataframe

#contar os registros do dataframe
print(len(df)) #mostra quantidade de dados 
print(df.shape) #retorna as quantidades de linhas e colunas (4, 2)

df.info() #visualizar as informações
