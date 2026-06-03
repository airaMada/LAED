from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#5. Alguém e o dobro - a. Apresente um algoritmo que resolve esse problema na lista nâo-ordenada.

v = criar_vetor(10, 0, 5)
print(v)

i = 0
achou = False

for i in range(len(v)):
  for j in range(len(v)):
    if i != j:
      if v[i] == 2*v[j]:
        print("aiguém e o dobro" ,v[j], "e"  ,v[i])
        achou = True
        break

    if achou:
      break
if not achou:
  print("não existem elementos")

