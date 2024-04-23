

def floyd_warshall(graph):
    distance = graph.copy()

    for k in graph:
        for i in graph:
            for j in graph:
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

graph = {
    'A': {'A': 0, 'B': 3, 'C': 6},
    'B': {'A': float('inf'), 'B': 0, 'C': -2},
    'C': {'A': float('inf'), 'B': float('inf'), 'C': 0}
}
shortest_distances = floyd_warshall(graph)
print("Matriz de distancias más cortas:")
for row in shortest_distances:
    print(row)
