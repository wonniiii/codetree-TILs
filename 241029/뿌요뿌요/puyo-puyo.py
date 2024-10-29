N = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False] * N
    for _ in range(N)
]
zone_num = 0
max_count = -1

def is_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y, current_num):
    if not is_range(x,y):
        return False
    if visited[x][y] or arr[x][y] != current_num:
        return False
    return True

def dfs(x,y, current_num):
    dxs,dys = [1,-1,0,0],[0,0,1,-1]
    visited[x][y] = True
    count = 1

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x+dx, y+dy
        
        if can_go(next_x, next_y, current_num):
            count += dfs(next_x, next_y, current_num)
    return count

def get_zone_num():
    global zone_num
    global max_count

    for i in range(N):
        for j in range(N):
            if not visited[i][j] :
                current_num = arr[i][j]
                count = dfs(i,j,current_num)
                
                if count >= 4:
                    zone_num += 1

                if max_count < count:
                    max_count = count

get_zone_num()

print(zone_num, max_count)