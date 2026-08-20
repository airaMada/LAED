#3

class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class Pilha:
    def __init__(self):
        self.topo = None
                                    
    def push(self, x):
        self.topo = No(x, self.topo)
                                                    
    def pop(self):
        if not self.topo: return None
            valor = self.topo.valor
            self.topo = self.topo.proximo
        return valor
                                                                                            
    def esta_vazia(self):
        return self.topo is None

def inverter_fila(fila):
    pilha = Pilha()
            
    while not fila.esta_vazia():
        pilha.push(fila.dequeue())
                            
    while not pilha.esta_vazia():
        fila.enqueue(pilha.pop())

fila = Fila()
valores = [1, 2, 3, 4, 5]
print(f"Inserindo na fila: {valores}")
for v in valores:
    fila.enqueue(v)

print("\nFila original:")
fila.exibir()

print("\nInvertendo fila usando pilha")
inverter_fila(fila)

print("\nFila invertida:")
fila.exibir()