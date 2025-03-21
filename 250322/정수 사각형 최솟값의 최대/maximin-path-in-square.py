n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)]for _ in range(n)]

def init():
    dp[0][0] = grid[0][0]
    for i in range(1,n):
        dp[i][0] = min(grid[i][0], dp[i-1][0])
    for j in range(1,n):
        dp[0][j] = min(grid[0][j],dp[0][j-1])

init()


for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])