from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#1. O maior número Ímpar

v = criar_vetor(5, 0, 20)
print(v)

maior = v[0]
encontrou_impar = False

for num in v:
  if num%2 != 0:
    encontrou_impar = True
    if num >= maior:
      maior = num

if encontrou_impar:
  print(f"maior ímpar: {maior}")
else:
  print("não existe")