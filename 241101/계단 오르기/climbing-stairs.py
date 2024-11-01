n = int(input())

# 예외 처리
if n < 2:
    print(0)
else:
    # DP 배열 초기화
    dp = [0] * 1001
    dp[0] = 1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1

    # 점화식을 사용해 dp 배열 채우기
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[n])