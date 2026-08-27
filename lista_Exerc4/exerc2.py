import matplotlib.pyplot as plt
import pandas as pd

linguagens = [
    'Python', 'Java', 'Python', 'C#', 'JavaScript', 'Python', 'Java', 'PHP',
    'JavaScript', 'Python', 'C#', 'Java', 'Python', 'JavaScript', 'TypeScript',
    'Python', 'C#', 'Java', 'Python', 'JavaScript', 'PHP', 'Python',
    'TypeScript', 'Java', 'Python', 'C#', 'JavaScript', 'Python', 'Java', 'PHP'
]

serie = pd.Series(linguagens)

# mostra frequencia de cada linguagem
frequencia_absoluta = serie.value_counts()
print(frequencia_absoluta)

# mostra frequencia relativa
frequencia_relativa = frequencia_absoluta/len(serie)
print(frequencia_relativa)

# linguagem mais frequente.
frequencia_absoluta.idxmax() # retorna o index/nome
frequencia_absoluta.max() # retorna o valor

