def radix_sort_passo(lista_numeros, digito_pos):
    baldes = [Fila() for _ in range(10)]
            
    for num in lista_numeros:
        digito = (num // (10**digito_pos)) % 10
        baldes[digito].enqueue(num)
                                    
                                    
    nova_lista = []
    for b in baldes:
       while not b.esta_vazia():
           nova_lista.append(b.dequeue())
    return nova_lista