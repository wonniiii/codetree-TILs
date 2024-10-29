from collections import deque

n, k = map(int, input().split())

# 격자 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 방문 배열 초기화
visited = [
    [False] * n
    for _ in range(n)
]

# BFS를 위한 큐
q = deque()
result = 0  # 방문 가능한 칸의 수

# 격자 범위 체크
def is_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 가능 여부 체크
def can_go(x, y):
    return is_range(x, y) and not visited[x][y] and grid[x][y] == 0

# BFS 함수
def bfs(start_x, start_y):
    q.append((start_x, start_y))
    visited[start_x][start_y] = True  # 시작점 방문 처리
    count = 1  # 시작점을 포함하여 방문한 칸 수

    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]  # 상하좌우 이동

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy

            if can_go(next_x, next_y):
                visited[next_x][next_y] = True  # 방문 처리
                q.append((next_x, next_y))
                count += 1  # 방문한 칸 수 증가

    return count

# 각 시작점 처리
for _ in range(k):
    x, y = map(int, input().split())
    # 0-based index로 변환
    start_x, start_y = x - 1, y - 1
    # BFS를 수행하여 각 시작점에서 도달할 수 있는 칸 수를 더함
    result += bfs(start_x, start_y)

print(result)