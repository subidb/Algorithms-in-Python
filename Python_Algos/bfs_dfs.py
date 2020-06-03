
graph1 = {
    'A': ['C', 'B'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'A'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E', 'C']
}


def bfs(graph, node):
    q = []
    visited_list = []

    q.append(node)
    visited_list.append(node)

    while q:
        vertex = q.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited_list:
                visited_list.append(neighbour)
                q.append(neighbour)


def dfs(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        print(node, end=" ")
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


bfs(graph1, 'B')
print()
dfs(graph1, 'B')
