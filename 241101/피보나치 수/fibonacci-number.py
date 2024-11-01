n = int(input())

# n이 0인 경우 예외처리
if n == 0:
    print(0)
else:
    dp = [0] * (n + 1)

    # n이 1일 경우 초기화 및 결과 출력
    dp[1] = 1
    if n > 1:
        dp[2] = 1

    # n이 3 이상일 때만 for문을 통해 피보나치 수열 계산
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])