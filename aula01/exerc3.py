import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto": ["Pão", "Arroz", "Pipoca"],
    "Preço": [2, 5, 10],
    "Quantidade": [5, 3, 7]
}
df = pd.DataFrame(dados)

print(df)

plt.bar(df["Produto"], df["Preço"],
        width=0.5,
        color="red")
plt.title("Preço dos produtos")
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.show()

plt.bar(df["Produto"], df["Quantidade"],
        width=0.2,
        color="green")
plt.title("Quantidade dos produtos")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.show()

plt.bar(df["Preço"], df["Quantidade"],
        width=0.8,
        color="yellow")
plt.title("Quantidade de preços")
plt.xlabel("Preço")
plt.ylabel("Quantidade")
plt.show()

plt.plot(df["Produto"], df["Quantidade"])
plt.title("Quantidade dos Produtos")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.show()