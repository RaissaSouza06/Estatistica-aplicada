import pandas as pd

tabela = pd.read_csv('dados.csv')

# serie = tabela["idade"]

# # mostra a frqeuncia ACUMULADA
# frequencia = serie.value_counts().sort_index()
# frequencia_ACUMULADA = frequencia.cumsum()

# tabela = pd.DataFrame({
#     "Frequencia Absoluta": frequencia,
#     "Frequencia Relativa": frequencia/len(serie),
#     "Frequencia Acumulada": frequencia_ACUMULADA
# })

# print(tabela)

# ///////////////////////////////////////////////////////////////////////////////
# VARIAVEL CATEGORICA
serie = tabela["cidade"]

frequencia = serie.value_counts().sort_index()
frequencia_ACUMULADA = frequencia.cumsum()

tabela = pd.DataFrame({
    "Frequencia Absoluta": frequencia,
    "Frequencia Relativa": frequencia/len(serie),
    "Frequencia Acumulada": frequencia_ACUMULADA
})
print(tabela)