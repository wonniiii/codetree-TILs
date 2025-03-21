n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for j in range(1,n):
        dp[0][j] = dp[0][j-1] + grid[0][j]


initialize()


for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[n-1][n-1])

