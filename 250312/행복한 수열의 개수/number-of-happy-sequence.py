n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 가로 검사
for i in range(n):
    count = 1
    happy = False  
    for j in range(1, n):
        if grid[i][j-1] == grid[i][j]:
            count += 1
        else:
            count = 1
        if count >= m:
            result += 1
            happy = True
            break  

    if not happy and count >= m:
        result += 1

# 세로 검사
for i in range(n):
    count = 1
    happy = False
    for j in range(1, n):
        if grid[j-1][i] == grid[j][i]:
            count += 1
        else:
            count = 1
        if count >= m:
            result += 1
            happy = True
            break
    if not happy and count >= m:
        result += 1

print(result)
