import pandas as pd 

dados = {
    "Produto" : ["Mouse", "Teclado", "Monitor", "Gabinete"],
    "Preço" : [80, 50, 800, 250],
    "Quantidade": [10, 50, 15, 25]
}

df =pd.DataFrame(dados)
print(df)

#criando uma nova tabela a partir do calculo de outras duas
df["Valor_total"] = df["Quantidade"] * df["Preço"]
print(df)

#método sort para ordenar em crescente o df
print(df.sort_values("Preço"))
#método sort para ordenar em decrescente o df
print(df.sort_values("Preço", ascending=False))

#filtra algo e retorna TRUE ou FALSE 
print(df["Quantidade"] < 20 )

#exibe apenas os atributos que possuem satisfazem a expressão
print(df[df["Quantidade"] < 20])

#combinando condições
print(df[(df["Quantidade"] < 20) & (df["Preço"] < 300)])

# TABELA VERDADE DO E &
# V e V = V
# V e F = F
# F e V = F
# F e F = F

# TABELA VERDADE DO OU 
# V e V = V
# V e F = V
# F e V = V
# F e F = F

