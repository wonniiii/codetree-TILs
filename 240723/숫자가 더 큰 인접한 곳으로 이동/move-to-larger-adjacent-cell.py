n, r, c = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
r -= 1
c -= 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def simulation(curr_r, curr_c):
    # 상하좌우 이동 방향
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = []
    visited.append(arr[curr_r][curr_c])

    while True:
        max_count = arr[curr_r][curr_c]
        next_r, next_c = curr_r, curr_c

        for dx, dy in zip(dxs, dys):
            nr, nc = curr_r + dx, curr_c + dy
            if in_range(nr, nc) and arr[nr][nc] > max_count:
                max_count = arr[nr][nc]
                next_r, next_c = nr, nc
                break

        if next_r == curr_r and next_c == curr_c:
            break

        visited.append(arr[next_r][next_c])
        curr_r, curr_c = next_r, next_c

    print(' '.join(map(str, visited)))

simulation(r, c)