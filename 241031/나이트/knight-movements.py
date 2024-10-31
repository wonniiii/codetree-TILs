from collections import deque

n = int(input())
nums = list(map(int, input().split()))
start_x,start_y = nums[0]-1, nums[1]-1
end_x, end_y = nums[2]-1, nums[3]-1


visited = [
    [False] * n
    for _ in range(n)
]

step = [
    [0] * n
    for _ in range(n)
]

q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dxs, dys = [-2,-2,-1,-1,1,1,2,2], [-1,1,-2,2,-2,2,-1,1]
    
    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x+dx, y+dy
            if can_go(next_x, next_y):
                push(next_x, next_y, step[x][y]+1)

push(start_x, start_y,0)
bfs()
if step[end_x][end_y] == 0 and visited[x][y] == False:
    print(-1)
else:
    print(step[end_x][end_y])