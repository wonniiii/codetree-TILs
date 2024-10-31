from collections import deque

n,m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

step = [
    [0] * m
    for _ in range(n)
]

q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == 1

def push(x,y,s):
    visited[x][y] = True
    q.append((x,y))
    step[x][y] = s

def bfs():
    dxs, dys = [1,-1,0,0], [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy
            if can_go(next_x, next_y):
                push(next_x, next_y, step[x][y]+1)

push(0,0,0)
bfs()
if step[n-1][m-1] == 0:
    print(-1)
else:
    print(step[n-1][m-1])