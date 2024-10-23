class TernaryHeapNode:
    def __init__(self, key):
        self.key = key
        self.children = [None, None, None]  # No máximo 3 filhos

class TernaryHeap:
    def __init__(self):
        self.nodes = []  # Usaremos uma lista para facilitar o acesso

    def insert_node(self, key):
        new_node = TernaryHeapNode(key)
        self.nodes.append(new_node)
        self.heapify_up(len(self.nodes) - 1)

    def heapify_up(self, index):
        parent_index = (index - 1) // 3
        while index > 0 and self.nodes[index].key < self.nodes[parent_index].key:
            self.nodes[index].key, self.nodes[parent_index].key = self.nodes[parent_index].key, self.nodes[index].key
            index = parent_index
            parent_index = (index - 1) // 3

    def extract_min(self):
        if not self.nodes:
            return None
        min_key = self.nodes[0].key
        last_node = self.nodes.pop()
        if self.nodes:
            self.nodes[0].key = last_node.key
            self.heapify_down(0)
        return min_key

    def heapify_down(self, index):
        while index * 3 + 1 < len(self.nodes):
            smallest = index
            for i in range(1, 4):
                child_index = index * 3 + i
                if child_index < len(self.nodes) and self.nodes[child_index].key < self.nodes[smallest].key:
                    smallest = child_index
            if smallest != index:
                self.nodes[index].key, self.nodes[smallest].key = self.nodes[smallest].key, self.nodes[index].key
                index = smallest
            else:
                break

def ternary_heap_sort(arr):
    heap = TernaryHeap()
    for key in arr:
        heap.insert_node(key)

    sorted_arr = []
    while heap.nodes:
        sorted_arr.append(heap.extract_min())
    
    return sorted_arr

# Exemplo de uso
arr = [10, 3, 9, 1, 7, 2, 8, 4, 6, 5]
sorted_arr = ternary_heap_sort(arr)
print("Array ordenado:", sorted_arr)
