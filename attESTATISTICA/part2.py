import pandas as pd
import matplotlib.pyplot as plt 

dados = {
    "usuario": [1,2,3,4,5,6,7,8,9,10],
    "idade": [18,22,25,31,28,35,42,24,29,33],
    "requisicoes": [10,15,8,20,12,25,18,9,14,21],
    "tempo_ms": [120,130,115,140,125,150,135,110,128,145],
    "erros": [0,1,0,2,0,3,1,0,1,2],
    "sistema": [
        "Android", "iOS", "Android", "Android", "iOS",
        "Android", "Windows", "Android", "iOS", "Android"
    ]
}

df = pd.DataFrame(dados)

###    QUESTÃO 4 - INSPEÇÃO DOS DADOS
print(df.head(5)) # Mostra as 5 primeiras linhas
print(df.shape) # Retorna as quantidades de linhas e colunas
print(df.info()) # Exibe as informações do DataFrame
print(df.describe()) # Exibe o resumo estatístico.

###    QUESTÃO 5 - FREQUENCIA
# a) Quantidade de usuários por sistema operacional (Frequência Absoluta)
qtd_usuarios = df['sistema'].value_counts()

# b) Percentual de usuários por sistema operacional (Frequência Relativa %)
percentual_usuarios = df['sistema'].value_counts(normalize=True) * 100

resultado = pd.DataFrame({
    '\nQuantidade Usuário': qtd_usuarios,
    'Percentual de Usuário (%)': percentual_usuarios
})

print(resultado)

###    QUESTÃO 6 - VISUALIZAÇÃO
# Criando o gráfico de barras
plt.figure(figsize=(8, 5))
qtd_usuarios.plot(kind='bar', color=["#231BB5", "#49BAD6", '#0078D4'])

plt.title('Quantidade de Usuários por Sistema Operacional')
plt.xlabel('Sistema Operacional')
plt.ylabel('Quantidade de Usuários')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# Qual SO possui maior frequência na amostra? Android

###    QUESTÃO 7 - ANÁLISE
# Usando tempo_ms
media_tempo = df['tempo_ms'].mean()
mediana_tempo = df['tempo_ms'].median()
moda_tempo = df['tempo_ms'].mode()  
minimo_tempo = df['tempo_ms'].min()
maximo_tempo = df['tempo_ms'].max()
amplitude_tempo = maximo_tempo - minimo_tempo

print("\n--- ESTATÍSTICAS DE TEMPO (ms) ---")
print(f"Média: {media_tempo} ms")
print(f"Mediana: {mediana_tempo} ms")
print(f"Moda: {moda_tempo.values}")
print(f"Mínimo: {minimo_tempo} ms")
print(f"Máximo: {maximo_tempo} ms")
print(f"Amplitude: {amplitude_tempo} ms")

# Média e mediana são próximas? o que isso pode indicar sobre os dados? São próximos, o que indica que os 
# números dentro de tempo_ms estão próximos, sem valores extremos.
