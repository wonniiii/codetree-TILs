N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def is_range(y, x):
    return 0 <= y < N and 0 <= x < M

def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def can_go(y, x, k):
    if not is_range(y, x):
        return False
    return not visited[y][x] and grid[y][x] > k

def dfs(y, x, k):
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for dy, dx in zip(dys, dxs):
        next_y, next_x = y + dy, x + dx
        if can_go(next_y, next_x, k):
            visited[y][x] = True
            dfs(next_y, next_x, k)

def get_zone_num(k):
    global zone_num

    zone_num = 0
    initialize_visited()

    for i in range(n):
        for j in range(m):
            if can_go(i,j,k):
                visited[i][j] = True
                zone_num += 1
                
                dfs(i,j,k)

max_zone_num = -1
answer_k = 0
max_height = 100

for k in range(1, max_height + 1):
    get_zone_num(k)

    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)