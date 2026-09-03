import pandas as pd

tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])

print('Média: ', tempos.mean())
print('Mediana: ', tempos.median())
print('Moda: ')
print(tempos.mode())

# Retorna valor máximo e minimo
print(tempos.max())
print(tempos.min())

# 5. Refletir: Qual dessas medidas melhor representa o comportamento central dos dados?]
# Mediana

# Média:  129.0
# Mediana:  125.0
# Moda:
# 0    120
# 1    125