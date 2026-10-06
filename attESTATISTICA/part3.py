import numpy as np
import pandas as pd

# QUESTÃO 8 — MEDIDAS DE DISPERSÃO (SEM OUTLIER)
tempo_ms = pd.Series([120, 130, 115, 140, 125, 150, 135, 110, 128, 145])
print("--- QUESTÃO 8 ---")
print(f"Variância populacional: {tempo_ms.var(ddof=0)}")
print(f"Desvio padrão da variancia populacional: {tempo_ms.std(ddof=0)}")

# QUESTÃO 9 — MEDIDAS DE DISPERSÃO (COM OUTLIER = 500 ms)
tempo_ms_q9 = pd.Series([120, 130, 115, 140, 125, 150, 135, 110, 128, 500])

media_tempo = tempo_ms_q9.mean()
mediana_tempo = tempo_ms_q9.median()
minimo_tempo = tempo_ms_q9.min()
maximo_tempo = tempo_ms_q9.max()
amplitude_tempo = maximo_tempo - minimo_tempo
desvio_padrao_tempo = tempo_ms_q9.std(ddof=0)

print("\n--- QUESTÃO 9 ---")
print(f"Média: {media_tempo:.1f} ms")
print(f"Mediana: {mediana_tempo:.1f} ms")
print(f"Amplitude: {amplitude_tempo} ms")
print(f"Desvio padrão populacional: {desvio_padrao_tempo:.2f} ms")