k,n = tuple(map(int, input().split()))
answer = []

def print_answer():
    for elem in answer:
        print(elem, end= " ")
    print()

def find_duplicated_permutations(cnt):
    if cnt == n:
        print_answer()
        return

    for i in range(1, k + 1):
        if cnt >= 2 and i == answer[-1] and i == answer[-2]:
            continue
        else:
            answer.append(i)
            find_duplicated_permutations(cnt+1)
            answer.pop()

find_duplicated_permutations(0)