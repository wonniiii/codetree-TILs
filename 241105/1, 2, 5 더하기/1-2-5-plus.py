import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = [1,2,5]
dp = [0]* (n+1)
dp[0] = 1

for i in range(1,n+1):
    for j in range(len(arr)):
        if i >= arr[j]:
            dp[i] = dp[i] + dp[i-arr[j]] % 10007

ans = dp[n]
print(ans)