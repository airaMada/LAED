#4.Verificar se existem dois elementos iguais na matriz M

v = criar_vetor(10, 0, 10)
print(v)

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

encontrou = False

for i in range(len(m)):
  for j in range(len(m)):
    if m[i][j] in v:
      print("Existe elementos repetidos:", m[i][j])
      encontrou = True
      break
    v.append(m[i][j])

  if encontrou:
    break
if not encontrou:
  print("Não existem elementos repetidos")
