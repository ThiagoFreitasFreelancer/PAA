def knapsack_with_dependencies(weights, values, capacity, dependencies):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # Sem incluir o item i
            if weights[i-1] <= w:
                if i-1 == 0 or any(dp[j+1][w-weights[i-1]] > 0 for j in dependencies.get(i-1, [])):
                    dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    def get_items(i, w):
        if i == 0 or w == 0:
            return []
        if dp[i][w] != dp[i-1][w]:
            return get_items(i-1, w-weights[i-1]) + [i-1]
        return get_items(i-1, w)
    
    items_included = get_items(n, capacity)
    
    return dp, dp[n][capacity], items_included

# Exemplo de uso
weights = [1, 3, 2, 4]  # Pesos dos itens
values = [8, 7, 5, 9]   # Valores dos itens
capacity = 5            # Capacidade da mochila
dependencies = {0: [], 1: [0], 2: [0], 3: [2]}  # Grafo de dependências

dp_table, max_value, items = knapsack_with_dependencies(weights, values, capacity, dependencies)

print("Valor máximo:", max_value)
print("Itens incluídos:", items)
print("Tabela de valores:")

# Exibir a tabela completa
header = "id p v | " + " ".join(f"{i}" for i in range(capacity + 1))
print(header)
print("-" * len(header))

for i in range(len(weights) + 1):
    row = f"{i} {weights[i-1] if i > 0 else 0} {values[i-1] if i > 0 else 0} | " + " ".join(f"{dp_table[i][j]}" for j in range(capacity + 1))
    print(row)
