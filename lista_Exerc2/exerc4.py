import pandas as pd

filmes = {
    "Filme": [
        "A Viagem de Chihiro",
        "Meu Amigo Totoro",
        "O Castelo Animado",
        "Princesa Mononoke",
        "Túmulo dos Vagalumes",
        "O Serviço de Entregas da Kiki",
        "Ponyo: Uma Amizade que Veio do Mar",
        "O Menino e a Garça"
    ],
    "Gênero": [
        "Animação / Fantasia",
        "Animação / Família",
        "Animação / Fantasia",
        "Animação / Aventura",
        "Animação / Drama",
        "Animação / Aventura",
        "Animação / Família",
        "Animação / Fantasia"
    ],
    "Ano": [2001, 1988, 2004, 1997, 1988, 1989, 2008, 2023],
    "Nota": [8.6, 8.1, 8.2, 8.4, 8.5, 7.8, 7.6, 7.6]
}

df = pd.DataFrame(filmes)

print(df[df["Nota"] > 8])
print(df.sort_values("Nota"))
print(df["Nota"].min())
print(df["Nota"].mean())