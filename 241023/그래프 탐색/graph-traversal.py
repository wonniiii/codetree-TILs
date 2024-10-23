N,M = map(int,input().split(" "))
array = [[0]* (N+1) for i in range(0,N+1)]

visited = [False] * (N+1)

for i in range(0,M):
    col,row = map(int,input().split(" "))
    array[col][row] = 1
    array[row][col] = 1

def dfs(vertex):
    visited[vertex] = True  # 현재 정점을 방문 처리
    count = 0  # 방문한 정점 수를 기록
    for curr_v in range(1, N+1):
        if array[vertex][curr_v] == 1 and not visited[curr_v]:
            count += 1  # 새로운 정점 방문 시 카운트 증가
            count += dfs(curr_v)  # 연결된 정점도 계속 탐색
    return count

print(dfs(1))