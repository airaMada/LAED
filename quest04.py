from random import randint
import random

def criar_vetor(tam, lim_i, lim_s):
  vetor = [0]* tam

  for i in range(tam):
    vetor[i] = random.randint(lim_i, lim_s)

  return vetor

#4. Elemento isolado
v = criar_vetor(8, 0, 9)
print(v)

encontrou = False

for i in range(len(v)):
  tem_mais = False
  tem_menos = False
  for j in range(len(v)):
    if v[j] == v[i]-1:
      tem_menos = True

    if v[j] == v[i] + 1:
      tem_mais = True

  if tem_menos == False and tem_mais == False:
    print("Elemento isolado:", v[i])
    encontrou = True
    break

if encontrou == False:
 print("Não existe elemento isolado")
