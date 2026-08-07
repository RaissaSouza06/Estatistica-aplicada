import pandas as pd
import matplotlib.pyplot as plt

filmes = {
    "Filme": ["Avatar", "Matrix", "Interestelar", "Vingadores", "Barbie"],
    "Nota" : [9.2, 9.5, 9.8, 8.9, 7.5]
 }
df = pd.DataFrame(filmes)

df.info() 
print(df.head())
print(df.describe())

plt.bar(df["Filme"], df["Nota"]) #Cria gráfico de barras
plt.title("Nota dos filmes")
plt.xlabel("Filme")
plt.ylabel("Nota")
plt.show()