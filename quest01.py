#1.Imagine que nós aplicamos o procedimento Partição() sobre a lista L

def partition(L):
    pivot = L[0]
    i = 1

    for j in range(1, len(L)):
        if L[j] <= pivot:
            L[i], L[j] = L[j], L[i]
            i += 1

    L[0], L[i-1] = L[i-1], L[0]
    return i - 1


def bubble_sort(L, ini, fim):
    for i in range(ini, fim + 1):
        for j in range(ini, fim):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


def algoritmo(L):
    p = partition(L)
    bubble_sort(L, 0, p - 1)
    bubble_sort(L, p + 1, len(L) - 1)
    return L