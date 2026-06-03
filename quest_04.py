from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#4. ímpar-ímpar

v = criar_vetor(10, 0, 5)
print(v)

i = 0
achou = False

while i < len(v):
  if v[i]%2 != 0:
    print(v[i])
    cont = 0
    j = 0
    while j < len(v):
      if v[i] == v[j]:
        cont+=1
      j+=1
    if cont % 2 != 0:
      print(f"quantidades impares: {cont}")
      achou = True
      break
  i+=1
if achou == False:
  print(f"não há quantidade impares")
