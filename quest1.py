class No:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

class ListaDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

def elemento_central(lista):
    if not lista.cabeca: return None
    slow = fast = lista.cabeca
    # fast.proximo.proximo garante que em listas pares paremos no item correto
    while fast.proximo and fast.proximo.proximo:
        slow = slow.proximo
        fast = fast.proximo.proximo
    return slow.valor

lista1 = ListaEncadeada()
valores1 = [1, 2, 3, 4, 5]
print(f"Inserindo: {valores1}")
for v in valores1:
    lista1.inserir(v)

print("\nLista:")
lista1.exibir()

central = elemento_central(lista1)
print(f"\nElemento central: {central} (esperado: 3)")