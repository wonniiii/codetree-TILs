from collections import deque

n,m = map(int, input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

order = 1
q = deque()

def is_range(x,y):
    return 0<=x<m and 0<=y<n

def push(x,y):
    global order
    grid[x][y] = order
    order += 1
    visited[x][y]= True
    q.append((x,y))

def can_go(x,y):
    if not is_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True
  
def bfs():
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy

            if can_go(next_x, next_y):
                push((next_x, next_y))
    
push((0,0))
bfs()
if visited[m-1][n-1] == 1:
    print(1)
else:
    print(0)