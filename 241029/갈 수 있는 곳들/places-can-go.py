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
order = 1
result = 0

def is_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not is_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def push(x,y):
    global result
    visited[x][y] = True
    q.append((x,y))
    result += 1

def bfs():
    dxs, dys = [1,-1,0,0], [0,0,-1,1]
    count = 0

    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy

            if can_go(next_x, next_y):
                push(next_x, next_y)

for _ in range(k):
    x,y = map(int, input().split())
    push(x-1,y-1)
    bfs()

print(result)