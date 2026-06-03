from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#8. Trabalhando com duas listas
v = criar_vetor(5, 1, 10)
print(v)

u = criar_vetor(5, 1, 10)
print(u)

for i in range(len(v)):
  for j in range(len(v)):
    if v[i] == u[j]:
      print(v[i])