import sys
INT_MAX = sys.maxsize

n,m = map(int, input().split())
coin = list(map(int,input().split()))
coin.append(0)
dp = [0] * (m+1)

for i in range(m+1):
    dp[i] = INT_MAX

dp[0] = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if i>=coin[j]:
            if dp[i-coin[j]] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i-coin[j]]+1)
ans = dp[m]
if ans == INT_MAX:
    ans = -1
print(ans)