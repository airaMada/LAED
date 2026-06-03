#5.Verificar a matriz M contém duas linhas exatamente iguais

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

for i in range(len(m)):
  for j in range(len(m)):
    iguais = True
    for k in range(len(m)):
      if m[i][j] != m[j][i]:
        iguais = False
        break

  if iguais == True:
    print("Existe linhas iguais")
    break

if not iguais:
  print("Não existem linhas iguais")