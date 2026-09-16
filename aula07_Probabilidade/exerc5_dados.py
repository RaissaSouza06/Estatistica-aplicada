import numpy as np
import pandas as pd

# mostra todos os resultado dps de ser lançado 10000x
resultado_10000 = np.random.randint(1, 7, size=10000)
# print(50*"-")
# print("Depois de ser lançado 10000x...")
# print(resultado_10000[:15]) # mostra só os 15 primeiros

# Calcula a frequência relativa de CADA uma das 6 faces (em %)
serie=pd.Series(resultado_10000)
frequencia = serie.value_counts().sort_index()
freq_relativa = frequencia/len(resultado_10000)

# Probabilidade teorica
probabilidade_teorica = 1/6

tabela = pd.DataFrame({
    "Frequencia" : frequencia,
    "Frequencia Relativa" : freq_relativa * 100,
    "Probabilidade" : probabilidade_teorica * 100
})

print(tabela)




