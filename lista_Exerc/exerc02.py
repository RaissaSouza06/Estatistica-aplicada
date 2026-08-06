import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto" : ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "Preço" : [85, 150, 980, 220, 320],
    "Quantidade" : [12, 8, 4, 10, 6]
}

df = pd.DataFrame(dados)

print(len(df))
print(max(df['Preço'])) #Mostra o que tem menor preço
print(min(df['Preço'])) #Mostra o que tem maior preço
print(sum(df["Quantidade"])) #Soma a quantidade de todos
