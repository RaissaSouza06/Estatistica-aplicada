import pandas as pd
import matplotlib.pyplot as plt

alunos = {
    "Nome" : ["Ana", "Léo", "Ivo", "Lia", "Otto", "Bia", "Caio", "Eva", "Rael", "Lara", "Gael", "Maya", "Yuri", "Zuri", "Theo", "Nina", "Davi", "Luna", "Luke", "Mila"],
    "Idade" : [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "Nota" : [3, 5, 7, 9, 2, 6, 1, 8, 3, 9, 4, 6, 7, 2, 3, 1, 5, 9, 3, 6]
}

df = pd.DataFrame(alunos)

print(df)
print(df.head())
print(df.describe())
df.info()