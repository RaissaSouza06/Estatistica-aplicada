import pandas as pd
import numpy as np

tempos = [100, 200, 500]
qts = [500, 300, 200]

# Média ponderada - average
m_ponderada = np.average(
    tempos,
    weights=qts
)

print(f"Média ponderada dos tempos de requisição: {m_ponderada}")

# Média ponderada - zip
numerador = sum (
    tempos * qts
    for tempos, qts in zip(tempos, qts)
)

denominador = sum(qts)

m_pond = numerador / denominador
print(f"Média ponderada usando o zip e o for: {m_pond}")