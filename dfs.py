graph = {'A': set(['B', 'C']),
         'B': set(['A','D','E']),
         'C': set(['A','F']),
         'D': set(['B']),
         'E': set(['B','F']),
         'F': set(['C','E'])}

def dfs(graph, vertex, visited=[]):
    if vertex not in visited:
        visited.append(vertex)
        for node in graph[vertex].difference(visited):
            dfs(graph, node, visited)
    return visited

print(dfs(graph, 'A'))
