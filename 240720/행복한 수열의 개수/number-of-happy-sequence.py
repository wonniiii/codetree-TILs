n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
a = []

def cal(array, count):
    a = [array[0]]
    if len(array) == 1:
        return True
    flag = 1
    for i in range(1, len(array)):
        if array[i] == a[-1]:
            flag += 1
        else:
            a.append(array[i])
        if flag == count:
            flag = 1
            return True
            break
    return False

res = 0
for i in range(n):
    if cal(arr[i], m):
        res += 1
for j in range(n):
    if cal(list(zip(*arr))[j], m):
        res += 1
print(res)