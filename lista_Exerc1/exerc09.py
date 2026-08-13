import pandas as pd
import matplotlib.pyplot as plt

#Criando das listas individuais 
produtos = ["Mouse", "Teclado", "Monitor", "Headset", "Cadeira", "Gabinete", "Webcam", "Mousepad", "Caixa de Som", "Microfone"]
precos = [80, 150, 900, 250, 1200, 450, 200, 60, 180, 300]
quantidades = [10, 15, 3, 8, 4, 6, 12, 25, 10, 7]

#Criando do DataFrame combinando as listas com o desafio das colunas
dados = {
    "Produto": produtos,
    "Preço": precos,
    "Quantidade": quantidades
}

df = pd.DataFrame(dados)

#Criando a nova coluna "Valor em Estoque" (Preço x Quantidade)
df["Valor em Estoque"] = df["Preço"] * df["Quantidade"]

print("--- Tabela Completa (Primeiros Registros com head) ---")
print(df.head()) # Uso de head()

print("\n--- Informações do DataFrame (info) ---")
df.info() 

print("\n--- Resumo Estatístico (describe) ---")
print(df.describe()) 

print("\n--- Outras Funções Solicitadas ---")
print("Quantidade de registros (len):", len(df))
print("Soma total dos preços (sum):", df["Preço"].sum())
print("Maior preço (max):", df["Preço"].max())
print("Menor preço (min):", df["Preço"].min())

#Gráfico de Barras
plt.bar(df["Produto"], df["Valor em Estoque"], color='royalblue')
plt.title("Valor Total em Estoque por Produto")
plt.xlabel("Produto")
plt.ylabel("Valor em Estoque (R$)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()