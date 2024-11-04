n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0]*n
    for _ in range(n)
]

dp[0][0] = grid[0][0]
res = grid[0][0]

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + grid[i][0]
    
for j in range(1,n):
    dp[0][j] = dp[0][j-1] + grid[0][j]

for i in range(1,n):
    for j in range(1,n):
        flag = 0
        if dp[i-1][0] > dp[0][j-1]:
            flag = grid[i-1][0]
        else:
            flag = grid[0][j-1]
        dp[i][j] = max(dp[i-1][0], dp[0][j-1]) + grid[i][j]
        if res > flag:
            res = flag

if res > grid[n-1][n-1]:
    res = grid[n-1][n-1]    
print(res)