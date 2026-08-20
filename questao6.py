#6
class FilaComPilhas:
    def __init__(self):
       self.p1 = Pilha() 
       self.p2 = Pilha() 
                        
    def enqueue(self, x):
        self.p1.push(x)
                                        
   def dequeue(self):
       if self.p2.esta_vazia():
                                                        
            while not self.p1.esta_vazia():
                self.p2.push(self.p1.pop())
       return self.p2.pop()