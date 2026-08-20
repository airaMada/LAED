class No:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

def particao(lista, k):
    q = lista.cabeca
    r = lista.cauda
    while q != r and q.anterior != r:
        while q and q.valor <= k: q = q.proximo
        while r and r.valor > k: r = r.anterior
        if q and r and q != r and q.anterior != r:
            q.valor, r.valor = r.valor, q.valor