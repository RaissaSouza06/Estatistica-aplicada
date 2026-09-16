total_requisicoes = 10000
requisicoes_com_erro = 350

# Cálculo da taxa estimada de erro
probabilidade_erro = requisicoes_com_erro / total_requisicoes
percentual_erro = probabilidade_erro * 100
print(f"Total de requisições: {total_requisicoes}")
print(f"Erros encontrados: {requisicoes_com_erro}")
print(f"Probabilidade estimada de erro: {probabilidade_erro}")
print(f"Taxa de Erro: {percentual_erro:.2f}%")