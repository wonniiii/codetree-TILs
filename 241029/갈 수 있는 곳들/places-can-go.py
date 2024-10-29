from collections import deque

n,k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

q = deque()

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x, y):
    return in_range(x, y) and not grid[x][y] and \
           not visited[x][y]

def bfs():
    dxs, dys = [1,-1,0,0], [0,0,-1,1]
    count = 0

    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy

            if can_go(next_x, next_y):
                q.append(next_x, next_y)
                visited[next_x][next_y] = True

for _ in range(k):
    x,y = map(int, input().split())
    bfs_q.append((x - 1, y - 1))
    visited[x - 1][y - 1] = True

bfs()

ans = sum([
    1
    for i in range(n)
    for j in range(n)
    if visited[i][j]
])

print(ans)