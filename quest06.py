from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#6. Permutações
v = criar_vetor(5, 1, 9)
print(v)

u = criar_vetor(5, 1, 9)
print(u)

m = [False]*len(v)

for i in range(len(v)):
  achou = False
  for j in range(len(v)):
    if u[i] == v[j] and m[j] == False:
      m[j] = True
      achou = True
      break

if achou == False:
  print("Não há permutações")
else:
  print("Há permutações")