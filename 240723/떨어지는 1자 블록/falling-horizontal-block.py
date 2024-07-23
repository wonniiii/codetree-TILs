n, m, k = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 초기 위치 설정
x = 0
y = k - 1
stop = False

while not stop:
    for i in range(m):
        next_x = x + 1
        next_y = y + i
        if not in_range(next_x, next_y) or arr[next_x][next_y] == 1:
            stop = True
            break
    if not stop:
        x += 1

# 블록 배치
for i in range(m):
    arr[x][y + i] = 1

# 결과 출력
for row in arr:
    print(' '.join(map(str, row)))