# n,m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# a = []

# def cal(array, count):
#     a = [array[0]]
#     if len(array) == 1:
#         return True
#     flag = 1
#     for i in range(1, len(array)):
#         if array[i] == a[-1]:
#             flag += 1
#         else:
#             a.append(array[i])
#         if flag == count:
#             return True
#             break
#     return False

# res = 0
# for i in range(n):
#     if cal(arr[i], m):
#         res += 1
# for j in range(n):
#     if cal(list(zip(*arr))[j], m):
#         res += 1
# print(res)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_happy_sequence(array, m):
    count = 1
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

happy_sequence_count = 0

# Check rows
for i in range(n):
    if is_happy_sequence(arr[i], m):
        happy_sequence_count += 1

# Check columns
for j in range(n):
    column = [arr[i][j] for i in range(n)]
    if is_happy_sequence(column, m):
        happy_sequence_count += 1

print(happy_sequence_count)