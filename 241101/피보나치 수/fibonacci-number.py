n = int(input())

UNUSED = -1
memo = [UNUSED for _ in range(n+1)]

def fib(n):
    if memo[n] != UNUSED:
        return memo[n]
    if n==1 or n==2:
        return 1
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]

print(fib(n))