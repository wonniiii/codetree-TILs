from collections import deque

# 입력 받기
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 초기화
distances = [[-1] * n for _ in range(n)]
q = deque()

# 비를 피할 수 있는 공간을 BFS의 시작점으로 설정
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:  # 비를 피할 수 있는 공간 위치
            q.append((i, j))
            distances[i][j] = 0

# BFS 탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] != 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                q.append((nx, ny))

# 결과 출력
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:  # 사람이 있는 위치
            print(distances[i][j], end=' ')
        else:
            print(0, end=' ')
    print()