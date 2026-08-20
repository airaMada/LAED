def mais_frequente(lista):
    contagem = {}
    atual = lista.cabeca
    while atual:
        contagem[atual.valor] = contagem.get(atual.valor, 0) + 1
        atual = atual.proximo
    return max(contagem, key=contagem.get) if contagem else None