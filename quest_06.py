from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#6. Os dois elementos mais próximos
v = criar_vetor(8, 1, 20)
print(v)

a = v[0]
b = v[1]
min_dif = abs(v[0]-v[1])

for i in range(len(v)):
  j = i + 1
  for j in range(len(v)):
    if v[i] != v[j]:
      dif = abs(v[i]-v[j])
      if dif < min_dif:
          min_dif = dif
          a = v[i]
          b = v[j]

print("menor diferença:", min_dif)
print("elemtos:", a, "e", b)
