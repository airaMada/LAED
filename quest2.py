class No:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

def atualizar(lista, x, y):
    atual = lista.cabeca
    while atual and atual.valor != x:
        atual = atual.proximo
    if not atual: return 
    
    if atual.anterior: atual.anterior.proximo = atual.proximo
    else: lista.cabeca = atual.proximo
    if atual.proximo: atual.proximo.anterior = atual.anterior
    else: lista.cauda = atual.anterior

    novo = No(y)
    p = lista.cabeca
    while p and p.valor < y:
        p = p.proximo