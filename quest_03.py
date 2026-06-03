from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#3. Busca aproximada

v = criar_vetor(10, 0, 10)
print(v)

k = random.randint(0, 10)
print(k)

i = 0
m = v[1]

while i < len(v):
  if v[i]==k:
    print(f"Número: {v[i]}")
  if (v[i] - k) < (m - k):
    m = v[i]
    i+=1
  break
print(f"O mais próximo: {m}")
