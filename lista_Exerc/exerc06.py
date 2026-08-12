import pandas as pd
import matplotlib.pyplot as plt

campeonato = {
    "Time" : ["Palmeiras", "Flamengo", "Corinthians", "São Paulo", "Santos"],
    "Pontos" : [48, 46, 41, 38, 35]
}

df = pd.DataFrame(campeonato)

print(df) #Exibe a tabela
plt.bar(df["Time"], df["Pontos"])
plt.title("Quantidade de pontos por time")
plt.xlabel("Time")
plt.ylabel("Pontos")
plt.show()