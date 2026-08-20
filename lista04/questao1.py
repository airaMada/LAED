class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

def maior_no_fim(lista):
    if not lista.cabeca or not lista.cabeca.proximo: return
    
    anterior_maior = None
    maior = lista.cabeca
    atual = lista.cabeca
    
    while atual.proximo:
        if atual.proximo.valor > maior.valor:
            anterior_maior = atual
            maior = atual.proximo
        atual = atual.proximo
    ultimo = atual
    
    if maior == ultimo: return 
    
    if maior == lista.cabeca:
        lista.cabeca = maior.proximo
    else:
        anterior_maior.proximo = maior.proximo
    
    ultimo.proximo = maior
    maior.proximo = None

lista = ListaEncadeada()

valores = [5, 2, 8, 3, 1]
print(f"Inserindo: {valores}")
for v in valores:
    lista.inserir(v)

print("\nLista original:")
lista.exibir()