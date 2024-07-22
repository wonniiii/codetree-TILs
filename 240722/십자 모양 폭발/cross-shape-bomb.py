n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r,c = map(int, input().split())
r -= 1
c -= 1
temp = []
count = arr[r-1][c-1] - 1
res = [[0 for j in range(n)] for i in range(n)]

for i in range(r-count, r+count+1):
    arr[i][c] = 0
for j in range(c-count, c+count+1):
    arr[r][j] = 0

for col in range(n):
    for row in range(n-1, -1, -1):
        if arr[row][col] != 0:
            temp.append(arr[row][col])
            
    for row in range(n-1, -1, -1):
        if temp:
            arr[row][col] = temp.pop(0)
        else:
            arr[row][col] = 0

# 결과 출력
for row in arr:
    print(' '.join(map(str, row)))