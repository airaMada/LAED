#2. O k-ésimo maior elemento
L = [7, 2, 9, 4, 1]
k = 2
n = len(L)

for i in range(n):
    for j in range(n - 1):
        if L[j] < L[j + 1]:
            aux = L[j]
            L[j] = L[j + 1]
            L[j + 1] = aux

print(L[k - 1])