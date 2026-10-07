import numpy as np

# Definir a semente para resultados reproduzíveis
np.random.seed(42)

# Simulação de 10.000 lançamentos de um dado de 6 faces
lancamentos = np.random.randint(1, 7, size=10000)

# Verificar quais lançamentos resultaram em números primos (2, 3 ou 5)
primos = np.isin(lancamentos, [2, 3, 5])

# Probabilidade experimental
prob_experimental = primos.mean()
pct_experimental = prob_experimental * 100

# Probabilidade teórica (3 números primos em 6 lados)
prob_teorica = 3 / 6
pct_teorica = prob_teorica * 100

print(f"Probabilidade Teórica: {pct_teorica:.2f}%")
print(f"Probabilidade Experimental (Simulação): {pct_experimental:.2f}%")