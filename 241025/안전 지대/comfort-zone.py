N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 방향 이동 (상, 하, 좌, 우)
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# 범위 체크 함수
def is_range(x, y):
    return 0 <= x < N and 0 <= y < M

# 높이가 k 이하인 곳은 물에 잠기므로, 물에 잠기지 않은 영역을 탐색하는 dfs 함수
def dfs(x, y, k):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cur_x, cur_y = stack.pop()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = cur_x + dx, cur_y + dy
            if is_range(next_x, next_y) and not visited[next_x][next_y]:
                # 높이가 k 초과인 경우만 안전 영역이므로 탐색 가능
                if grid[next_x][next_y] > k:
                    visited[next_x][next_y] = True
                    stack.append((next_x, next_y))

# 결과 변수
max_safe_areas = 0  # 최대 안전 영역 수
best_k = 0  # 최대 영역 수를 만든 K값

# 1부터 최대 높이까지 K값을 돌며 안전 영역 수를 계산
for k in range(1, max(map(max, grid)) + 1):
    visited = [[False] * M for _ in range(N)]  # 매 K마다 방문 배열 초기화
    safe_area_count = 0  # 안전 영역 개수

    # 모든 좌표를 돌며 높이가 k 초과인 곳에서 DFS 탐색
    for i in range(N):
        for j in range(M):
            if grid[i][j] > k and not visited[i][j]:
                dfs(i, j, k)  # 새로운 안전 영역 발견
                safe_area_count += 1  # 안전 영역 개수 증가

    # 안전 영역 개수 최대값 갱신 및 그때의 K값 저장
    if safe_area_count > max_safe_areas:
        max_safe_areas = safe_area_count
        best_k = k

# 출력: 가장 안전 영역이 많은 K와 그 때의 안전 영역 수
print(best_k, max_safe_areas)