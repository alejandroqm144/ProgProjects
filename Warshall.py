

def transitive_closure(graph):
    n = len(graph)
    closure = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            closure[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure

graph = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

transitive_closure_graph = transitive_closure(graph)
print("Matriz de cierre transitivo:")
for row in transitive_closure_graph:
    print(row)