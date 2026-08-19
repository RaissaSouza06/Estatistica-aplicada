import pandas as pd

alunos = pd.DataFrame({
    "Nome": [
        "ana", "bruno", "carlos", "daniela",
        "eduardo", "fernanda", "gabriel", "helena",
        "igor", "julia", "lucas", "marina"
    ],
    "Notas" : [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

print(len(alunos)) # retorna tamanho da população
# OU print(alunos.shape[0])

mediaPopulacao = alunos["Notas"].mean()
print(mediaPopulacao) #retorna média da POPULAÇÃO

amostra = alunos.sample(n=5, random_state=42) #retira uma amostra de 5 alunos
mediaAmostra = amostra["Notas"].mean() #retorna média da amostra
print(mediaAmostra)

print(mediaPopulacao - mediaAmostra) #calcula o erro amostral

