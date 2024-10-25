n,m = map(int, input().split(" "))

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1

    dxs, dys = [1,0], [0,1]

    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)

dfs(0,0)
print(visited[n-1][m-1])