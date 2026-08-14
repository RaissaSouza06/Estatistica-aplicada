import pandas as pd 

dados = {
    "Nome" : ["Ana", "Carlos", "João", "Felipe", "Marcos", "José", "Raissa", "Renan", "Gisely", "Heloisa"],
    "Idade" : [20, 25, 63, 10, 58, 25, 20, 20, 18, 20],
    "Nota": [10, 5, 9, 8, 7, 3, 10, 5, 9, 9]
}

df =pd.DataFrame(dados)

print(df["Nota"].mean()) #mostra a média das notas
print(df["Nota"].max()) #mostra a maior nota
print(df["Nota"].min()) #mostra a menor nota
print(df.sort_values("Nota")) #ordena pela nota
print(df[df["Nota"] >= 7] )