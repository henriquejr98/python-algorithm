import heapq

def dijkstra(graph, start):
    # Inicialização
    distancia = {vertice: float('infinity') for vertice in graph}
    distancia[start] = 0
    fila = [(0, start)]

    while fila:
        # Pega o vértice com a menor distância
        atual_dist, vertice_atual = heapq.heappop(fila)

        # Se já encontramos um caminho mais curto para este vértice, ignore-o
        if atual_dist > distancia[vertice_atual]:
            continue

        # Percorre os vizinhos do vértice atual
        for vizinho, peso in graph[vertice_atual].items():
            dist = atual_dist + peso

            # Se encontrarmos um caminho mais curto para o vizinho, atualize a distância
            if dist < distancia[vizinho]:
                distancia[vizinho] = dist
                heapq.heappush(fila, (dist, vizinho))

    return distancia

# Exemplo de uso:
grafo = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'E': 7, 'B': 8},
    'D': {'E': 6, 'F': 3},
    'E': {'F': 1}
}

resultado = dijkstra(grafo, 'A')
print(resultado)
