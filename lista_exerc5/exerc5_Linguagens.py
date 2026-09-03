import pandas as pd
import matplotlib.pylab as plt

linguagens = ['Python', 'Java', 'Python', 'JavaScript', 'Python', 'C#', 
'Java', 'Python', 'C#', 'Python']

# 1. Converta a lista de linguagens em uma Series do Pandas.
serie = pd.Series(linguagens)

# 2. Calcule a frequência absoluta de cada uma e descubra qual linguagem é a Moda do conjunto.
FAB = serie.value_counts()
print(f"Frequencia absoluta: {FAB}")
moda = serie.mode()
print (f"Moda: {moda}")


# 3. Calcule a frequência relativa em porcentagem para cada categoria registrada.
FR = serie.value_counts(normalize=True)
print(FR)

# 4. Crie um Gráfico de Barras com Matplotlib mostrando a preferência das linguagens.
FAB.plot(kind="bar")
plt.title("Preferencia de linguagem")
plt.show()