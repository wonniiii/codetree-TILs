n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
s1,e1 = map(int, input().split())
s2,e2 = map(int, input().split())
temp = []

for j in range(n):
    if not(j in range(s1-1,e1)):
        temp.append(arr[j])
arr = temp
temp = []
n = len(arr)

for h in range(n):
    if not(h in range(s2-1,e2)):
        temp.append(arr[h])

print(len(temp))
print(*temp, sep = "\n")