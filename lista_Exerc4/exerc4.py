import pandas as pd
import matplotlib.pyplot as plt

tempo = [
    120, 11, 246, 234, 150, 150, 160, 120, 130, 50,
    23, 467, 598, 124, 134, 156, 234, 160, 170, 190, 
    120, 11, 246, 234, 150, 150, 160, 120, 130, 50,
    23, 467, 598, 124, 134, 156, 234, 160, 170, 190, 
    130, 140, 140, 150, 150, 150, 150, 160, 160, 170
]

series = pd.Series(tempo)

FAB = series.value_counts()
print(FAB)

# HISTOGRAMAS
plt.hist(tempo, bins=2)
plt.xlabel("Tempo")
plt.ylabel("Frequência")
plt.title("Distribuição do tempo de resposta")
plt.show()

# BINS -> Matplotlib pega o menor valor da lista (11) e o maior (598),
#  calcula a diferença total e divide esse intervalo em 10 colunas de largura igual (aproximadamente ~58.7 unidades por coluna).
plt.hist(tempo, bins=10)
plt.xlabel("Tempo")
plt.ylabel("Frequência")
plt.title("Distribuição do tempo de resposta")
plt.show()

plt.hist(tempo, bins=20)
plt.xlabel("Tempo")
plt.ylabel("Frequência")
plt.title("Distribuição do tempo de resposta")
plt.show()

# O que acontece com o gráfico quando aumentamos ou diminuimos o número de classes?
### Aumentar o número de classes detalha o gráfico e destaca variações locais, enquanto diminuí-lo simplifica a visualização e destaca o padrão geral dos dados.