class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

def intercalar(l1, l2):

 # Complexidade: O(n + m) onde n e m são os tamanhos das listas