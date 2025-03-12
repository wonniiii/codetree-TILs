n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
count = 1
result = 0

for i in range(n):
    for j in range(1,n):
        if grid[i][j-1] == grid[i][j]:
            count += 1
        if count == m:
            result += 1
            break

    count = 1

count = 1

for i in range(n):
    for j in range(1,n):
        if grid[j-1][i] == grid[j][i]:
            count += 1
        if count == m:
            result += 1
            break

    count = 1

print(result)