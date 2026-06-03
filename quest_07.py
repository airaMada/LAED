from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#7. Contando inversões
v = criar_vetor(4, 1, 10)
print(v)

cont = 0

for i in range(len(v)):
  j = i + 1
  for j in range(len(v)):
    if v[i] > v[j]:
      cont = cont + 1

print("Quantidade de inversões:",cont)