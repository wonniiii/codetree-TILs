n,m = map(int, input().split(" "))

answer = [
    [0 for _ in range(n+1)]
    for _ in range(m+1)
    ]
visited = [
    [0 for _ in range(n+1)]
    for _ in range(m+1)
]
order = 1
grid = [list(map(int, input().split())) for _ in range(m)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global order 

    dxs, dys = [1,0], [0,1]

    if x == n and y == m:
        return 1

    answer[x][y] = order
    order += 1
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)
    return 0

print(dfs(0,0))