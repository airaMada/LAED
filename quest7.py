def transformar_para_lista_de_listas(lista_original, k):
    n = 0
    atual = lista_original.cabeca
    while atual:
        n += 1
        atual = atual.proximo
    
    m = n // k
    vetor_ponteiros = []
    atual = lista_original.cabeca
    
    for i in range(k):
        vetor_ponteiros.append(atual)
        for _ in range(m):
            if atual: atual = atual.proximo
    return vetor_ponteiros