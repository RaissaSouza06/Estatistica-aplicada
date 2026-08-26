import pandas as pd
import matplotlib.pyplot as plt

notas = [
     7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10
 ]

# 1. Criar uma Series.
series = pd.Series(notas)

# 2. Calcular a frequência absoluta.
FAB = series.value_counts()

# 3. Calcular a frequência relativa.
FR = series.value_counts(normalize=True)

# 4. Calcular a frequência acumulada.
FAC = FAB.cumsum()

# 5. Criar uma tabela.
tabela = pd.DataFrame({
    "Frequencia_absoluta": FAB,
    "Frequencia_relativa": FR,
    "Frequencia_acumulada": FAC
})

# 6. Criar um gráfico de barras.
FAB.plot(kind="bar")
plt.title("Frequencia de notas")
plt.xlabel("Notas")
plt.ylabel("Frequencia")
plt.show()

# 7. Criar um gráfico de pizza.
FAB.plot(
    kind="pie",
    autopct="%1.1%%"
)
plt.title("Frequencia das notas")
plt.show()