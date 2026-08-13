import pandas as pd
import matplotlib.pyplot as plt

naruto = {
    "Ninja" : ["Naruto", "Sasuke", "Kakashi", "Gaara", "Itachi", "Killer", "Shikamaru", "Hinata", "Jiraya", "Tsunade"],
    "Aldeia" : ["Folha", "Folha", "Folha", "Areia", "Folha", "Nuvem", "Folha", "Folha", "Folha", "Folha",], 
    "Chakra" : [95, 94, 90, 88, 96, 91, 82, 80, 93, 92]
}

df = pd.DataFrame(naruto)

print(df)

plt.bar(df["Ninja"], df["Chakra"], color="green")
plt.title("Relação Chakra X Ninja")
plt.xlabel("Ninja")
plt.ylabel("Chakra")
plt.xticks(rotation=45, ha='right') # Rotaciona os rótulos do eixo X em 45 graus para evitar sobreposição
# Exibe o gráfico ajustado
plt.tight_layout() # Ajusta automaticamente os elementos para caber na janela
plt.show()

print(df.head())
print()