import pandas as pd
import matplotlib.pyplot as plt

tempo = [
    110, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 220, 230, 250, 300, 500
]

series = pd.Series(tempo)

# BOXPLOT
plt.boxplot(tempo)
plt.ylabel("Tempo(ms)")
plt.title("Distribuição de tempo de resposta")
plt.show()

# HISTOGRAMAS
plt.hist(tempo)
plt.xlabel("Tempo")
plt.ylabel("Frequência")
plt.title("Distribuição do tempo de resposta")
plt.show()

# Existem valoresque parecem diferentes?
### sim, valores 300 ms e 500 ms afastam-se visivelmente do padrão do conjunto de dados, comportando-se como pontos discrepantes (outliers).

# Qual região concentra a maior parte dos dados?
### Na faixa entre 110 ms e 210 ms.

# O valor 500 parece seguir o comportamento dos demais?
### Não. O valor 500 fica bem acima do limite superior do boxplot (que é de 295 ms para este conjunto de dados). No histograma, ele aparece isolado no extremo direito, indicando um tempo de resposta atípico em relação ao padrão observado.
