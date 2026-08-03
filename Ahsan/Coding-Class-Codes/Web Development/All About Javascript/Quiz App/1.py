from collections import deque
graph = {
    'A':['B','C','D'],
    'B':['A','C'],
    'C':['A','B'],
    'D':['A']
}

def bfs():
    q = deque()
    q.append('A')
    visited = ['A']
    while len(q) != 0:
        n = q.popleft()
        for v in graph[n]:
            if v not in visited:
                q.append(v)
                visited.append(v)
    print(visited)
bfs()