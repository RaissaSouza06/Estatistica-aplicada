### AMOSTRAGEM ALEATÓRIA SIMPLES ###

import random #gera elementos aleatórios

alunos = ["Rogério", "Ricardo", "Shimada", "Kaio", "Camila", "Vitor", "Geovana", "Renan", 
          "Carlos", "Miguel", "Ana", "Stevens", "Guilherme", "Raissa", "Mateus", "Felipe", 
          "Andrew", "Artur", "Gabi", "Pedro"]

random.seed(15) #com o SEED as amostras não mudam ao rodar o código

amostra = random.sample(alunos, 3) #seleciona 3 alunos de forma ALEATÓRIA
#método SAMPE não repete o mesmo elemento dentro da amostra

print(amostra)