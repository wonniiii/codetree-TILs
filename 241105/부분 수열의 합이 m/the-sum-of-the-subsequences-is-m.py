import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
arr = [0]+list(map(int, input().split()))
dp = [0] + [INT_MAX] * m

for i in range(1,n+1):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            if dp[j-arr[i]] == INT_MAX:
                continue
            dp[j] = min(dp[j], dp[j-arr[i]]+1)
ans = dp[m]
if ans == INT_MAX:
    ans = -1
print(ans)