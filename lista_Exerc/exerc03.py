import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Lista" : [12, 25, 18, 40, 32, 11, 9, 28, 37, 15]
}

df = pd.DataFrame(dados)

print(len(df)) #Mostrar quantidade de elementos.
print(sum(df["Lista"])) #Soma dos valores
print("Média:", df["Lista"].mean()) #Média dos valores
print(max(df["Lista"])) #Valor máx
print(min(df["Lista"])) #Valor min

#Ordena a 'Lista' de forma crescente
df_ordenado = df.sort_values(by="Lista", ascending=True)
print(df_ordenado)