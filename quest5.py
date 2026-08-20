class No:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

def construir_vetor_esparso(V):
    lista = ListaDupla()
    for i in range(len(V)):
        if V[i] != 0:
            novo = No((V[i], i))

V1 = [0, 5, 0, 0, 8, 0, 3, 0, 0, 0, 7]
print(f"Vetor original: {V1}")

print("\nConstruindo lista esparsa...")
lista1 = construir_vetor_esparso(V1)

print("\nLista duplamente encadeada (apenas não-zero):")
lista1.exibir()