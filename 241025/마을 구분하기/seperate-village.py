n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    # 범위 내에 있고, 방문하지 않았으며, 사람이 있을 경우
    return is_in_range(x, y) and not visited[x][y] and grid[x][y] == 1

def dfs(x, y):
    # DFS로 한 마을에 속하는 사람의 수를 카운트
    visited[x][y] = 1
    count = 1  # 현재 노드를 포함한 사람 수

    # 상, 하, 좌, 우 방향
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            count += dfs(new_x, new_y)  # 재귀 호출로 마을 크기 누적
    
    return count

villages = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:  # 사람이고 아직 방문하지 않았다면
            village_size = dfs(i, j)  # 해당 마을 크기를 계산
            villages.append(village_size)

# 마을 수 출력
print(len(villages))
# 마을 내 사람 수를 오름차순으로 정렬 후 출력
for village in sorted(villages):
    print(village)