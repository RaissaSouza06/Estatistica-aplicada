# Desenvolva um programa completo em Python que simule o comportamento de 100.000 requisições HTTP em um servidor de grande porte.
# • Premissa: O servidor possui uma taxa teórica de erro de exatamente 2% (0,02).
# • Simulação: Gere 100.000 eventos rotulados como 'SUCESSO' ou 'ERRO'.
# • Relatório Final: O programa deverá imprimir na tela:
#  • Total de Requisições Simuladas
#  • Quantidade e Taxa Percentual de Sucessos
#  • Quantidade e Taxa Percentual de Erros
# • Análise Comparativa: O programa deve exibir a diferença entre a taxa simulada e a probabilidade teórica esperada (2,00%)

import numpy as np

total_req = 100000
taxa_erro_teorica = 0.02

requisicoes = np.random.choice(
    ["Sucesso", "Erro"] ,
    size=100000,
    p=[0.98, 0.02]
)

quantidade_sucessos = (requisicoes == "Sucesso").sum()
quantidade_erros = (requisicoes == "Erro").sum()

taxa_sucesso = quantidade_sucessos / total_req # ou -> / len(requisicoes)
taxa_erro = quantidade_erros / total_req

diferenca_erro = taxa_erro - taxa_erro_teorica

print("=" * 50)
print("Relatório de monitoramento da API")
print("=" * 50)

print(f"Total de Requisições Simuladas: {total_req}")

print(
    f"Sucessos: {quantidade_sucessos}"
    f"  ({taxa_sucesso * 100:.2f})%"
    )

print(
    f"Erros:    {quantidade_erros}"
    f"  ({taxa_erro * 100:.2f})%"
)

print(f"Taxa de erro teórica: 2.00%")
print(f"Taxa de erro simulada: {taxa_erro * 100:.2f}%")
print(f"Diferença: {diferenca_erro * 100:.2f}%")

print("=" * 50)