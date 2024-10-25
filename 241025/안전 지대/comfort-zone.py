N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def is_range(y, x):
    return 0 <= y < N and 0 <= x < M

def can_go(y, x, k):
    if not is_range(y, x):
        return False
    return not visited[y][x] and grid[y][x] > k

def dfs(y, x, k):
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[y][x] = True
    
    for dy, dx in zip(dys, dxs):
        next_y, next_x = y + dy, x + dx
        if can_go(next_y, next_x, k):
            dfs(next_y, next_x, k)

max_num = max(map(max, grid))
max_safe_areas = 0
best_k = 1

for k in range(1, max_num + 1):
    visited = [[False] * M for _ in range(N)]
    safe_area_count = 0
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                safe_area_count += 1
    
    if safe_area_count > max_safe_areas:
        max_safe_areas = safe_area_count
        best_k = k

print(best_k, max_safe_areas)