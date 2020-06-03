graph1 = {
    'A': ["D", "C"],
    'B': ["D"],
    'C': ["A"],
    'D': ["B", "A"]
}


def bfs(graph, node, visitedlist=None):
    visitedlist = [node]
    q = [node]

    while q:
        vertex = q.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visitedlist:
                visitedlist.append(neighbour)
                q.append(neighbour)


def dfs(graph, node, visitedlist):
    print(node, end=" ")
    visitedlist.append(node)
    for neigbour in graph[node]:
        if neigbour not in visitedlist:
            dfs(graph, neigbour, visitedlist)


graph1 = {
    'A': ['C', 'B'],
    'B': ['A', 'D', 'E'],
    'C': ['F', 'A'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E', 'C']
}

bfs(graph1, 'B')
print()
dfs(graph1, 'B', [])


