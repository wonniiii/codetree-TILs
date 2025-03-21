n,m = tuple(map(int, input().split()))
graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]
cnt = 0


def dfs(vertex):
    global cnt

    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

for i in range(m):
    v1, v2 = tuple(map(int,input().split()))

    graph[v2].append(v1)
    graph[v1].append(v2)

visited[1] = True
dfs(1)

print(cnt)