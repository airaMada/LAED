#5
def verificar_delimitadores(expressao):
    pilha = Pilha()
     pares = {')': '(', ']': '[', '}': '{'}
            
    for char in expressao:
       if char in "([{":
            pilha.push(char)
        elif char in ")]}":
           if pilha.esta_vazia() or pilha.pop() != pares[char]:
                return False
    return pilha.esta_vazia()