# dijkstra_armageddon.py
# Algoritmo de Dijkstra aplicado ao evento Armageddon
# Autor: Marcelo dos Santos Prado

import heapq

# Grafo representando o mapa do Armageddon
# PT: Grafo com os caminhos possíveis
# EN: Graph representing the map paths
# FR: Graphe représentant les chemins de la carte
graph = {
    "Base Norte": {"Encruzilhada A": 2},
    "Base Sul": {"Encruzilhada C": 2},
    "Encruzilhada A": {"Encruzilhada B": 2, "Lago das Sombras": 5},
    "Encruzilhada B": {"Lago das Sombras": 1, "Lago dos Ecos": 4},
    "Encruzilhada C": {"Encruzilhada B": 2},
    "Lago das Sombras": {},
    "Lago dos Ecos": {}
}

def dijkstra(graph, start):
    # PT: Inicializa distâncias e fila de prioridade
    # EN: Initialize distances and priority queue
    # FR: Initialiser les distances et la file de priorité
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    previous = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, previous

def reconstruct_path(previous, start, end):
    # PT: Reconstrói o caminho do início ao destino
    # EN: Reconstruct the shortest path from start to end
    # FR: Reconstruire le chemin le plus court du début à la fin
    path = []
    while end is not None:
        path.insert(0, end)
        end = previous[end]
    return path if path[0] == start else []

# Exemplo de uso: encontrar caminho da Base Norte ao Lago dos Ecos
distances, previous = dijkstra(graph, "Base Norte")
shortest_path = reconstruct_path(previous, "Base Norte", "Lago dos Ecos")

for i, node in enumerate(shortest_path):
    print(f"{i+1}. {node} "
          f"# PT: Ponto do caminho | EN: Path point | FR: Point de passage")

# Distância final
print(f"\n# PT: Distância total: {distances['Lago dos Ecos']}")
print(f"# EN: Total distance: {distances['Lago dos Ecos']}")
print(f"# FR: Distance totale: {distances['Lago dos Ecos']}")
