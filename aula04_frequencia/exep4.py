import matplotlib.pyplot as plt
import pandas as pd

idades = [18, 19, 20, 21, 22, 25, 27, 30, 31, 35]

# bins=2 cria dois intervalos
plt.hist(idades, bins=2)
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.title("Distribuição das Idades")
plt.show()