class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

def inverter_lista(lista):
    anterior = None
    atual = lista.cabeca
    while atual:
        proximo_no = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo_no
    lista.cabeca = anterior

lista = ListaEncadeada()
valores = [10, 20, 30, 40, 50]
print(f"Inserindo: {valores}")
for v in valores:
    lista.inserir(v)

print("\nLista original:")
lista.exibir()

print("\nInvertendo lista...")
inverter_lista(lista)

#O(n), percurso linear simples