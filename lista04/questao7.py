def remover_valor(lista, k):
    while lista.cabeca and lista.cabeca.valor == k:
        lista.cabeca = lista.cabeca.proximo

lista = ListaEncadeada()
valores = [2, 5, 2, 3, 2, 4, 2]
print(f"Inserindo: {valores}")
for v in valores:
    lista.inserir(v)

print("\nLista original:")
lista.exibir()

print("\nRemovendo todos os '2'")
remover_valor(lista, 2)