from collections import deque

# 입력 처리
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = map(int, input().split())

# 방문 처리 배열
visited = [[False] * n for _ in range(n)]

# 방향 이동 설정 (상, 하, 좌, 우)
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

# 범위 내 여부 체크 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 가능 여부 체크 함수
def can_go(x, y, num):
    # 범위 내에 있고, 방문하지 않았으며, 해당 위치의 값이 현재 값보다 작아야 함
    return in_range(x, y) and not visited[x][y] and grid[x][y] < num

# BFS를 통해 이동을 반복하는 함수
def bfs():
    # 시작 위치 큐에 추가 및 방문 처리
    q = deque([(start_x-1, start_y-1)])
    visited[start_x-1][start_y-1] = True
    current_x, current_y = start_x-1, start_y-1

    # k번 이동 반복
    for _ in range(k):
        next_positions = []  # 다음으로 갈 수 있는 위치와 값을 저장할 리스트
        
        # 현재 위치에서 갈 수 있는 위치 찾기
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                next_x, next_y = x + dx, y + dy
                if can_go(next_x, next_y, grid[x][y]):
                    next_positions.append((grid[next_x][next_y], next_x, next_y))
        
        # 다음 위치로 이동할 수 없다면 종료
        if not next_positions:
            break

        # 최댓값을 기준으로 위치 선정 (값 > 행 번호 > 열 번호 순으로 우선순위)
        next_positions.sort(reverse=True, key=lambda pos: (pos[0], -pos[1], -pos[2]))
        max_value, next_x, next_y = next_positions[0]

        # 이동할 위치로 설정
        current_x, current_y = next_x, next_y
        visited[next_x][next_y] = True
        q.append((next_x, next_y))  # 다음 위치를 큐에 추가하여 이동 준비

    # 최종 위치 출력
    print(current_x, current_y)

# BFS 실행
bfs()