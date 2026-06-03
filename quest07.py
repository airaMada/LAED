from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#7. Repetidos próximos

v = criar_vetor(10, 0, 9)
print("vetor:", v)

k = random.randint(0, 9)
print("k:", k)

encontrou = False

for i in range(len(v)):
  for j in range(i + 1, len(v)):
    if v[i] == v[j] and (j - i) < k:
      print("existe")
      print(f"Elemento repetido:", v[i])
      print(f"Distância:", j - i)
      encontrou = True
      break

  if encontrou:
    break
if encontrou == False:
  print("Não existe")