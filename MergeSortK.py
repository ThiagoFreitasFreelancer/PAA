# Função de intercalação (merge) para k partições usando Insertion Sort
def merge_k(A, i, f, d, k):
    # Lista de partes a serem mescladas
    subarrays = []
    for j in range(k):
        inicio = i + j * d
        fim = i + (j + 1) * d - 1 if j != k - 1 else f
        subarrays.append(A[inicio:fim + 1])

    # Junta todas as partições em uma lista única
    result = []
    for subarray in subarrays:
        result.extend(subarray)

    # Aplicar Insertion Sort para ordenar a lista intercalada
    for j in range(1, len(result)):
        key = result[j]
        l = j - 1
        while l >= 0 and result[l] > key:
            result[l + 1] = result[l]
            l -= 1
        result[l + 1] = key

    # Copiar o resultado de volta para o array original A
    A[i:f + 1] = result

# Função para o Merge Sort de um subarray
def merge_sort(A, i, f):
    if i < f:
        mid = (i + f) // 2
        merge_sort(A, i, mid)  # Ordena a primeira metade
        merge_sort(A, mid + 1, f)  # Ordena a segunda metade
        merge(A, i, mid, f)  # Mescla as duas metades

# Função para mesclar duas partes no Merge Sort
def merge(A, i, mid, f):
    left = A[i:mid + 1]
    right = A[mid + 1:f + 1]
    l = r = 0
    k = i

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            A[k] = left[l]
            l += 1
        else:
            A[k] = right[r]
            r += 1
        k += 1

    # Copia os elementos restantes da esquerda, se houver
    while l < len(left):
        A[k] = left[l]
        l += 1
        k += 1

    # Copia os elementos restantes da direita, se houver
    while r < len(right):
        A[k] = right[r]
        r += 1
        k += 1

# Função mergesort_k para ordenar k partições
def mergesort_k(A, i, f, k):
    # Se a diferença entre os índices for menor que k-1, não é necessário dividir mais
    if f - i > k - 1:
        d = (f - i + 1) // k  # Delta, tamanho das partições

        # Aplicar mergesort (com merge sort) para cada uma das k partições
        for j in range(k):
            inicio = i + j * d
            fim = i + (j + 1) * d - 1 if j != k - 1 else f
            merge_sort(A, inicio, fim)  # Aqui, aplicamos o merge sort nas partições

        # Intercalar as k partes usando Insertion Sort
        merge_k(A, i, f, d, k)
    else:
        # Se a partição é pequena o suficiente, usar merge sort
        merge_sort(A, i, f)

# Exemplo de uso
if __name__ == "__main__":
    A = [38, 27, 43, 3, 2, 82, 10]
    k = 2  # Número de partições
    print("Array original:", A)
    mergesort_k(A, 0, len(A) - 1, k)
    print("Array ordenado:", A)
