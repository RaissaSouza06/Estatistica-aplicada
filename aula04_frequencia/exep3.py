import matplotlib.pyplot as plt
import pandas as pd

notas = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 7, 8, 9, 10, 8, 7, 6, 8, 9, 8] 
serie = pd.Series(notas) 
frequencia = serie.value_counts().sort_index()
frequencia.plot(kind="bar")
plt.title("Frequência das Notas")
plt.xlabel("Nota")
plt.ylabel("Quantidade")
plt.show()