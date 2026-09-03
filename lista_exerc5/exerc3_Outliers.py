import pandas as pd
import matplotlib.pylab as plt

tempos = pd.Series([100, 105, 110, 108, 115, 120, 125, 130, 500, 550])

# Retorna média, mediana e moda
print('Média: ', tempos.mean())
print('Mediana: ', tempos.median())
print('Moda: ')
print(tempos.mode())

# Retorna valor máximo e minimo
print(tempos.max())
print(tempos.min())

# Retorna o histograma
tempos.plot(kind="hist")
plt.title("Historgrama dos tempos")
plt.show()

# Retorna o boxplot
tempos.plot(kind="box")
plt.title("Boxplot dos tempos")
plt.show()

# 3. Os valores extremos de 500 ms e 550 ms alteraram de forma relevante o valor da média? E o da mediana?
# a mediana não altera já a média puxou bastante p cima