from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#5. k repetições

v = criar_vetor(10, 0, 10)
print(v)

k = random.randint(0, 9)
print("k:",k)

encontrou = False

for i in range(len(v)):
  cont = 0
  for j in range(len(v)):
    if v[i] == v[j]:
      cont = cont + 1

  if cont == k:
    print("O elemento", v[i], "aparece", k, "vezes")
    encontrou = True
    break

if encontrou == False:
 print("Não existe")