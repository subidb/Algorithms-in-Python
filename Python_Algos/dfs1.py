def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


graph1 = {
    'O': ["M", "P"],
    'P': ["M", "O", "Q", "R"],
    'M': ["P", "N"],
    'N': ["M"],
    'R': ["Q", "P"],
    'Q': ["R", "P"]
}

graph2 = {
    1: [5, 3],
    5: [1, 6],
    6: [],
    3: [6, 7]
}

print(graph2)
for node in graph2:
    print(node, ":", graph2[node])
    # print(node)

print(graph1['R'])
# visitedlist = []
# dfs(visitedlist, graph1, 'O')

# print()
# v1 = list()
# print(v1)