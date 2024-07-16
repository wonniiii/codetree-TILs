import sys

INT_MAX = sys.maxsize
n = int(input())
arr = list(map(int, input().split()))
house = list(range(1, n + 1))

sum_min = 0

for i in range(n):
    sum_diff = 0
    for j in range(n-1):
        sum_diff += (abs(house[j+1] - house[i]) * arr[j+1])
    if INT_MAX > sum_diff :
        sum_min = sum_diff

print(sum_min)