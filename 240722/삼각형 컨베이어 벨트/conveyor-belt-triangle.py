n,t = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
temp = [0,0,0]

for i in range(t):
    temp[0] = a1[n-1]
    temp[1] = a2[n-1]
    temp[2] = a3[n-1]

    for i in range(n-1, 0, -1):
        a1[i] = a1[i-1]
        a2[i] = a2[i-1]
        a3[i] = a3[i-1]

    a1[0] = temp[2]
    a2[0] = temp[0]
    a3[0] = temp[1]

    temp = [0,0,0]
print(*a1, sep = " ")
print(*a2, sep = " ")
print(*a3, sep = " ")