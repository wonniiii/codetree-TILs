from collections import deque

n,h,m = map(int, input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

step = [
    [0] * n
    for _ in range(n)
]

res = [
    [101] * n
    for _ in range(n)
]
q = deque()
human_pos = []
space_pos = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            human_pos.append((i,j))
        elif grid[i][j] == 3:
            space_pos.append((i,j))

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def initalArr():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] != 1

def push(x,y,s):
    visited[x][y] = True
    step[x][y] = s
    q.append((x,y))

def bfs():
    dxs, dys = [1,-1,0,0],[0,0,-1,1]

    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy
            if can_go(next_x, next_y):
                push(next_x, next_y, step[x][y]+1)

for human in human_pos:
    human_x, human_y = human
    initalArr()
    push(human_x,human_y,0)
    bfs()
    for space in space_pos:
        space_x, space_y = space    
        if res[human_x][human_y] > step[space_x][space_y]:
            res[human_x][human_y] = step[space_x][space_y]
    
    if step[space_x][space_y] == 0:
        res[human_x][human_y] = -1
           
for i in range(n):
    for j in range(n):
        if res[i][j] == 101:
            res[i][j] = 0
        print(res[i][j], end=' ')
    print()