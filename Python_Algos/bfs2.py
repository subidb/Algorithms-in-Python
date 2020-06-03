# from collections import defaultdict
import collections

graph1 = {
    'A': ['C', 'B'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(graph, node):

    visited = []
    visited.append(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
bfs(graph1, 'A')
