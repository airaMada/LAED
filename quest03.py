#3.Agora considere duas listas ordenadas de tamanho Apresente um algoritmo que
#encontra a mediana do conjunto formado pelos elementos de e ,em tempo (log2 n).

def mediana(A, B):
    n = len(A)

    if n == 1:
        return (A[0] + B[0]) / 2

    if n == 2:
        return (max(A[0], B[0]) + min(A[1], B[1])) / 2

    m1 = A[n // 2]
    m2 = B[n // 2]

    if m1 == m2:
        return m

    if m1 < m2:
        return mediana(A[n // 2:], B[:n // 2])

    return mediana(A[:n // 2], B[n // 2:])