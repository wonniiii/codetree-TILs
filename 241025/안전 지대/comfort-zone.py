N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def dfs(i, j, k, visited):
    visited[i][j] = True
    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and grid[ni][nj] > k:
            dfs(ni, nj, k, visited)

min_h = min(min(row) for row in grid)
max_h = max(max(row) for row in grid)
max_safe_areas = 0
best_k = min_h

for k in range(min_h, max_h + 1):
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] > k and not visited[i][j]:
                dfs(i, j, k, visited)
                cnt += 1
    if cnt > max_safe_areas:
        max_safe_areas = cnt
        best_k = k

print(best_k, max_safe_areas)