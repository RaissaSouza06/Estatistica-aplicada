import pandas as pd

#Criando o DataFrame da população
dados = {
    'Curso': ['DSM', 'Processos Gerenciais', 'Gestão Empresarial'],
    'Quantidade': [500, 300, 200]
}
df = pd.DataFrame(dados)

total_populacao = df['Quantidade'].sum() # Total: 1000 alunos
tamanho_amostra = 100

#Calculando a proporção de cada curso e o tamanho da amostra
# Divide a quantidade de alunos do curso pelo total geral de alunos -> Transforma esse número decimal em porcentagem.
df['Proporção (%)'] = (df['Quantidade'] / total_populacao) * 100

# Pega a fatia do curso e multiplica pelo tamanho da amostra que você quer montar (100).
df['Qtd na Amostra'] = (df['Quantidade'] / total_populacao) * tamanho_amostra

print(df)

# Por que não seria adequado simplesmente selecionar 100 alunos sem considerar os cursos?
# pq pode distorcer as proporções reais dos cursos