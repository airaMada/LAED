class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def tem_repetido(lista):
    vistos = set()
    atual = lista.cabeca
    while atual:
        if atual.valor in vistos: return True
        vistos.add(atual.valor)
        atual = atual.proximo
    return False

lista1 = ListaEncadeada()
valores1 = [3, 7, 2, 7, 5, 2]
print(f"Inserindo: {valores1}")
for v in valores1:
    lista1.inserir(v)

print("\nLista:")
lista1.exibir()

resultado = tem_repetido(lista1)
print(f"\nTem repetido? {resultado}")