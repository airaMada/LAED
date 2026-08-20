#4

class PilhaComMinimo:
    def __init__(self):
        self.topo = None
                
    def push(self, x):
                        
        min_atual = x
        if self.topo and self.topo.min_abaixo < x:
            min_atual = self.topo.min_abaixo
                                                                
                                                            
        novo_no = No(x, self.topo)
        novo_no.min_abaixo = min_atual
                                                    
                                                    
        self.topo = novo_no
                                                                                                    
    def min(self):
      return self.topo.min_abaixo if self.topo else None

pilha = PilhaComMinimo()

print("Empilhando: 5")
pilha.push(5)
print(f"Mínimo atual: {pilha.min()}")
pilha.exibir_com_min()