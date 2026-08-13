import pandas as pd
import matplotlib.pyplot as plt

produtos = {
    "Produto": ["Arroz", "Feijão", "Café", "Açucar", "Leite", "Óleo", "Macarão"],
    "Preço" : [32, 11, 24, 6, 8, 9, 7]
 }
df = pd.DataFrame(produtos)

plt.bar(df["Produto"], df["Preço"])
plt.title("Preço dos produtos")
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.show()

