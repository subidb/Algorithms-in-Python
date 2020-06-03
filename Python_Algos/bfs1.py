
def bfs(graph, node):
    visitedlist, queue = [], []
    visitedlist.append(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visitedlist:
                visitedlist.append(neighbour)
                queue.append(neighbour)



graph1 = {
    'O': ["M", "P"],
    'P': ["M", "O", "Q", "R"],
    'M': ["P", "N"],
    'N': ["M"],
    'R': ["Q", "P"],
    'Q': ["R", "P"]
}

bfs(graph1, 'R')
