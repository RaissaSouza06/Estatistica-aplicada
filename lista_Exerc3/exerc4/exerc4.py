### CRIA AMOSTRA APENAS COM ALUNOS PRESENCIAIS

import pandas as pd

df = pd.read_csv("alunos_100.csv")

#cria uma nova coluna par apoder comparar
df["Modalidade"] = ["Presencial"] * 70 + ["Remoto"] * 30

#salva as linhas que possuem presencial na tabela modalidade na variavel presenciais
presenciais = df[df["Modalidade"] == "Presencial"]

amostra = presenciais.sample(n=20, random_state=14)

#mostra qtd de vezes que presencial apareceu em modalidades, tem que ser 20
print(amostra["Modalidade"].value_counts()) 

# Essa amostra representa adequadamente a população? Explique sua resposta
# não, pois exclui os alunos da modalidade remoto, criando um viés de seleção 