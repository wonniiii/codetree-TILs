import sys

INT_MAX = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))

sum_min = INT_MAX

for i in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += abs((j + 1) - (i + 1)) * arr[j] 
    if sum_min > sum_diff:
        sum_min = sum_diff

print(sum_min)