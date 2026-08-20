#a1)
def busca_por_indice(lista, k):
    atual = lista.cabeca
    while atual:
        valor, pos = atual.valor  # Assume tupla (valor, posição)
        if pos == k: return valor
        if pos > k: break  # Otimização: passou da posição k
        atual = atual.proximo
    return 0

#a2)
def busca_por_valor(lista, x):
    atual = lista.cabeca
    while atual:
        valor, pos = atual.valor
        if valor == x: return pos
        atual = atual.proximo
    return -1

#a3)
#O(n) para busca e ajuste da lista.