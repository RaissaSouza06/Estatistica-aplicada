import pandas as pd

notas = pd.Series([7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 
9, 8, 10])

print('Média: ', notas.mean())
print('Mediana: ', notas.median())
print('Moda: ')
print(notas.mode())

# 3. Discorra: Qual das três medidas estatísticas calculadas é a mais adequada para 
#  representar as notas da classe? Justifique matematicamente

# Média

