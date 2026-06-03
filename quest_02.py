from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#2.O segundo maior ímpar

v = criar_vetor(10, 0, 10)
print(v)

maior = None
maior1 = None

for num in v:
  if num%2 != 0:

    if maior is None or num >= maior:
      maior1 = maior
      maior = num

    elif (maior1 is None or num > maior1) and num != maior:
      maior1 = num

if maior is not None and maior1 is not None:
  print(f"maior ímpar: {maior}")
  print(f"segundo maior ímpar: {maior1}")
else:
  print(f"não existe")