import pandas as pd

salarios = pd.Series([2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 
2800, 20000])

print(f"Média de salário: {salarios.mean()}")
print(f"Mediana dos salários: {salarios.median()}")
print ("Moda: ")
print(salarios.mode())

# 2. A média salarial representa bem a realidade da maioria dos funcionários comum? NÂO
# 3. Explique o que aconteceu por conta do salário de R$ 20.000 (Diretor) e qual medida 
# representa melhor o salário típico. Por conta do salário houve um discrepancia na média, medida ideal seria a mediana

