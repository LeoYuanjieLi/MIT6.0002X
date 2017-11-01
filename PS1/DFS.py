def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []
    while stack:
        (vertex, path) = stack.pop()
        for nextVertex in [item for item in graph[vertex] if item not in path]:
            if nextVertex == goal:
                result.append(path + [nextVertex])
            else:
                stack.append((nextVertex, path + [nextVertex]))

    return result


