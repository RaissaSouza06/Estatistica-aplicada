import numpy as np

# Simulando um único lançamento de dado (de 1 a 6)
# resultado = np.random.randint(1, 7)
# print(50*"-")
# print("Lançando o dado...")
# print(resultado)

# mostra todos os resultado dps de ser lançado 1000x
resultado_1000 = np.random.randint(1, 7, size=1000)
print(50*"-")
print("Depois de ser lançado 1000x...")
print(resultado_1000[:15]) # mostra só os 15 primeiros
# print(resultado_1000)

# mostra quantas vezes o número 5 caiu dps de ser lançado 1000x
qtd_5 = np.sum(resultado_1000 == 5)
print(f"Quantidade de vezes que caiu o número 5: {qtd_5}")

probabilidade_de_cair_5 = qtd_5/ len(resultado_1000)
print(f"Probabilidade de cair o número 5: {probabilidade_de_cair_5}")
print(f"Probabilidade real teórica 1/6: {1/6:.4f}")



