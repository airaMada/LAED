class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

def separar_pares_impares(lista):
    pares = ListaEncadeada()
    impares = ListaEncadeada()

#O(n), visitando cada nó exatamente uma vezlock