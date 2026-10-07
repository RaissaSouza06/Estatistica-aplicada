import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "usuario": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "idade": [18, 22, 25, 31, 28, 35, 42, 24, 29, 33],
    "requisicoes": [10, 15, 8, 20, 12, 25, 18, 9, 14, 21],
    "tempo_ms": [120, 130, 115, 140, 125, 150, 135, 110, 128, 145],
    "erros": [0, 1, 0, 2, 0, 3, 1, 0, 1, 2],
    "sistema": [
        "Android", "iOS", "Android", "Android", "iOS",
        "Android", "Windows", "Android", "iOS", "Android"
    ]
}

df = pd.DataFrame(dados)

# a) Estatística descritiva de tempo_ms
media_tempo = df['tempo_ms'].mean()
mediana_tempo = df['tempo_ms'].median()
amplitude_tempo = df['tempo_ms'].max() - df['tempo_ms'].min()
desvio_padrao_tempo = df['tempo_ms'].std(ddof=0)  

print("a) ESTATÍSTICA DESCRITIVA (tempo_ms)")
print(f"Média: {media_tempo:.1f} ms")
print(f"Mediana: {mediana_tempo:.1f} ms")
print(f"Amplitude: {amplitude_tempo} ms")
print(f"Desvio Padrão: {desvio_padrao_tempo:.2f} ms\n")

# b) Análise de frequência
freq_sistemas = df['sistema'].value_counts()
print("\nb) ANÁLISE DE FREQUÊNCIA")
print(freq_sistemas)
print()

# c) Probabilidade estimada de erro (erros > 0)
prob_erro = (df['erros'] > 0).mean()
print("\nc) PROBABILIDADE DE ERRO")
print(f"Probabilidade estimada de erro: {prob_erro * 100:.1f}%\n")

# d) Visualização (Dois gráficos)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1: Distribuição dos sistemas operacionais
freq_sistemas.plot(kind='bar', ax=axes[0], color=["#F774A9", "#C53C9E", "#930461"])
axes[0].set_title('Distribuição dos Sistemas Operacionais')
axes[0].set_xlabel('Sistema Operacional')
axes[0].set_ylabel('Quantidade de Usuários')
axes[0].tick_params(axis='x', rotation=0)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Gráfico 2: Distribuição dos tempos de resposta
axes[1].hist(df['tempo_ms'], bins=5, color='pink', edgecolor='black')
axes[1].set_title('Distribuição dos Tempos de Resposta (ms)')
axes[1].set_xlabel('Tempo de Resposta (ms)')
axes[1].set_ylabel('Frequência')
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()