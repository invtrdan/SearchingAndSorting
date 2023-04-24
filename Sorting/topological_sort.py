from collections import *

def topological_sort_bfs(graph):
    # Base Cases
    if not graph: return []

    # Tracking Variables
    q, result, visited, indegree = deque(), [], set(), defaultdict(int)
    for src, edges in graph.items(): 
        if src not in indegree: indegree[src] = 0
        for vertex in edges: indegree[vertex] += 1

    for vertex, degree in indegree.items():
        if not degree: q.append(vertex)
    
    while q:
        node = q.popleft()
        if node in visited: return []
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if not indegree[neighbor]: q.append(neighbor)

    return result



    