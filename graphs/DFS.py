def dfs(start, adjacent, visited):
    print(start, end = " ")
    
    visited[start] = True
    for u in adjacent[start]:
        if not visited[u]:
            dfs(u, adjacent, visited)
            
vertices = int(input())
edges = int(input())

adjacent = [[] for _ in range(vertices)]
visited = [False] * vertices

for _ in range(edges):
    u, v = list(map(int, input().split()))
    adjacent[u].append(v)
    # adjacent[v].append(u) if non-directed
    
start = int(input())
dfs(start, adjacent, visited)