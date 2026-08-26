import pandas as pd

notas = [
    7, 8, 6, 9, 7,
    5, 8, 7, 10, 6,
    8, 9, 7, 5, 6,
    8, 7, 9, 8, 10
]

# dataframe é um conjunto de séries
# cada linha do dataframe é uma série
serie=pd.Series(notas)

# print(serie)

# mostra quantas vezes cada elemento aparece
# print(serie.value_counts())
# # número X qtd

# # ordena a partir do index, a nota
# # elementos X frequencia absoluta
# print(serie.value_counts().sort_index())


# # mostra a frqeuencia RELATIVA
# print(serie.value_counts(normalize=True))
# # mostra a frqeuencia RELATIVA em PORCENTAGEM
# print(serie.value_counts(normalize=True)*100)


# mostra a frqeuncia ACUMULADA
frequencia = serie.value_counts().sort_index()
frequencia_ACUMULADA = frequencia.cumsum()
# print(frequencia_ACUMULADA)

tabela = pd.DataFrame({
    "Frequencia Absoluta": frequencia,
    "Frequencia Relativa": frequencia/len(serie),
    "Frequencia Acumulada": frequencia_ACUMULADA
})

print(tabela)