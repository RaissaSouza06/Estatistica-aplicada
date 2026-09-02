import pandas as pd
import matplotlib.pyplot as plt

categorias = [
    'Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows','Windows',
    'Linux','Linux','Linux','Linux','Linux','Linux','Linux','Linux','Linux',
    'macOS','macOS','macOS','macOS','macOS','macOS','macOS','macOS','macOS',
    'Android','Android','Android','Android','Android','Android','Android','Android','Android',
    'iOS','iOS','iOS','iOS','iOS','iOS','iOS','iOS','iOS'
]

series = pd.Series(categorias)

# calcula frequencia absoluta
FAB = series.value_counts()
print(FAB)

# calcula frequencia relativa em porcentagem
FR = series.value_counts(normalize=True)
print(FR * 100)

# categoria mais frequente.
print(FAB.idxmax()) # retorna o index/nome

# gráfico de barras
FAB.plot(kind="bar")
plt.title("Frequencia de categorias")
plt.xlabel("Categoria")
plt.ylabel("Frequencia")
plt.show()

# gráfico de pizza.
FAB.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Frequencia de categorias")
plt.show()