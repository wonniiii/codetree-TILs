n,t = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
temp = [0,0]

for i in range(t):
    temp[0] = a1[n-1]
    temp[1] = a2[n-1]

    for j in range(n-1, 0, -1):
        a1[j] = a1[j-1]
        a2[j] = a2[j-1]
    
    a1[0] = temp[1]
    a2[0] = temp[0]
    temp = [0,0]
    
print(*a1, sep = " ") 
print(*a2, sep = " ")