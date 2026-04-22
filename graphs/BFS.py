def bfs(v_count, adjacent, start):
    visited = [False] * v_count
    queue = [None] * v_count
    front, rear  = 0, -1
    
    rear += 1
    queue[rear] = start
    visited[start] = True
    
    while front <= rear:
        current = queue[front]
        front += 1
        
        print(current, end = " ")
        for u in adjacent[current]:
            if not visited[u]:
                rear += 1
                queue[rear] = u
                visited[u] = True
                
v_count = int(input())
e_count = int(input())

adjacent = [[] for _ in range(v_count)]

for _ in range(e_count):
    u, v = list(map(int, input().split()))
    adjacent[u].append(v)
    
start = int(input())
bfs(v_count, adjacent, start)