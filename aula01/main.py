# Nosso priemiro DataFrame
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Aluno": ["Rogério", "Matheus", "Camila", "Geovana"],
    "Nota": [8, 5, 9, 6]
}

df = pd.DataFrame(dados)

# df.info() #info traz informações sobre o df, não retorna algo, só mostra, como tipo e quantidade

# print(df.describe()) #retorna uma descrição como média, menor valor, porcentagem, maior valor

# print(df.head()) #retorna só os primeiros registros

plt.bar(df["Aluno"], df["Nota"]) #define as barras do gráfico
plt.show()
