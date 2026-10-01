p_spam = 0.10
p_palavra_spam = 0.80
p_palavra_normal = 0.05
p_normal = 1 - p_spam
# Probabilidade Total da Evidência P(Palavra)
p_palavra = (p_palavra_spam * p_spam) + (p_palavra_normal * p_normal)
# Aplicação do Teorema de Bayes
p_spam_dado_palavra = (p_palavra_spam * p_spam) / p_palavra
print("Resultado em Decimal:", p_spam_dado_palavra)

# Formatando o resultado em porcentagem conforme a fonte
p_porcentagem = p_spam_dado_palavra * 100
print(f"Probabilidade de ser Spam: {p_porcentagem:.1f}%")
# Saída: Probabilidade de ser Spam: 64.0%
# Exibição resumida completa
print("-" * 40)
print(f"P(Spam) A Priori : {p_spam*100:.1f}%")
print(f"P(Palavra Total) : {p_palavra*100:.1f}%")
print(f"P(Spam | Palavra) : {p_porcentagem:.1f}%")
print("-" * 40)

# Função genérica para calcular P(A|B) via Teorema de Bayes
def calcular_bayes(p_b_dado_a, p_a, p_b):
 """
 Calcula a probabilidade a posteriori P(A|B).
 p_b_dado_a: Verossimilhança P(B|A)
 p_a: Probabilidade a priori P(A)
 p_b: Probabilidade total da evidência P(B)
 """
 return (p_b_dado_a * p_a) / p_b
# Executando para o filtro de spam:
resultado = calcular_bayes(p_palavra_spam, p_spam, p_palavra)
print("Resultado via Função:", resultado) # Saída: 0.64