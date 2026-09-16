import numpy as np

requisicoes = np.random.choice(["Sucesso", "Erro"], size=10000, p=[0.95, 0.05])

total = len(requisicoes)
total_erros = (requisicoes == "Erro").sum()
porcentagem_erros = (total_erros / total) * 100

print(f"Total de requisições: {total}")
print(f"Total de error: {total_erros}")
print(f"Porcentagem de erros: {porcentagem_erros}%")