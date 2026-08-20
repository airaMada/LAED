class No:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

def varredura(lista):
    if not lista.cabeca: return
    atual = lista.cabeca
    while atual.proximo:
        if atual.valor > atual.proximo.valor:
            # Chama função de troca de nós (ponteiros)
            trocar_nos(lista, atual, atual.proximo)
        else:
            atual = atual.proximo

lista1 = ListaEncadeada()
valores1 = [5, 3, 8, 1, 4, 2]
print(f"Inserindo: {valores1}")
for v in valores1:
    lista1.inserir(v)

print("\nLista original:")
lista1.exibir()

print("\nAplicando varredura")
varredura(lista1)