from collections import deque


graph = {
    'A':['B','F','G'],
    'B':['A','C','G'],
    'C':['B','D','G'],
    'D':['C','E','G'],
    'E':['D','F','G'],
    'F':['A','E','G'],
    'G':['A','B','C','D','E','F']
}

def dfs():
    stack = []
    visited = []
    stack.append('A')
    while len(stack) != 0:
        n = stack.pop()
        if n  not in visited:
            for v in graph[n]:
                stack.append(v)
            visited.append(n)
    return visited

def bfs():
    q = deque()
    visited = []
    q.append('A')
    while len(q) != 0:
        n = q.popleft()
        if n  not in visited:
            for v in graph[n]:
                q.append(v)
            visited.append(n)
    return visited
print(dfs())





