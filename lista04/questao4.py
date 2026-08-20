class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

def duplicar_impares(lista):
    atual = lista.cabeca
    while atual:
        if atual.valor % 2 != 0:
            novo = No(atual.valor)
            novo.proximo = atual.proximo
            atual.proximo = novo
            atual = novo.proximo 
        else:
            atual = atual.proximo

lista = ListaEncadeada()
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista original: {valores}")
for v in valores:
    lista.inserir(v)

print("\nLista original:")
lista.exibir()

print("\nDuplicando números ímpares...")
duplicar_impares(lista)