from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#1. O terceiro maior elemento
v = criar_vetor(8, 0, 9)
print(v)

m1 = m2 = m3 = float('-inf')
i = 0

while i < len(v):
  if v[i] > m1:
    if v[i] != m1:
      m3 = m2
      m2 = m1
      m1 = v[i]

  elif v[i] > m2:
    if v[i] != m2:
      m3 = m2
      m2 = v[i]

  elif v[i] > m3 and v[i] != m1 and v[i] != m2:
    m3 = v[i]
  i+=1
print("Terceiro maior elemento:", m3)