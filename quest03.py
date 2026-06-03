from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#3. O mais próximo da média

v = criar_vetor(8, 0, 9)
print(v)

soma = 0

for i in range(len(v)):
  soma = soma + v[i]

media = soma/len(v)

melhor = v[0]
menor_Dif = abs(v[0] - media)

for i in range(len(v)):
  if abs(v[i] - media) < menor_Dif:
    menor_Dif = abs(v[i] - media)
    melhor = v[i]

print("Média:", media)
print("O mais próximo da média:", melhor)