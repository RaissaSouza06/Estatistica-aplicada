import pandas as pd
import matplotlib.pyplot as plt

Cadastro = {
    "Nome": ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda"],
    "Idade": [18, 20, 19, 22, 21, 18, 23, 20]
}
df = pd.DataFrame(Cadastro)

print(df) #Exibindo o df
print(df.head(5)) #Mostra as 5 primeiras linhas
df.info() #Exiba as informações do DataFrame
print(df.describe()) #Exiba o resumo estatístico.