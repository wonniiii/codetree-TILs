n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(1,n):
    for j in range(0,i):
        if j + arr[j] >= i:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))