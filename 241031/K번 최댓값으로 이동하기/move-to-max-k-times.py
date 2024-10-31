import collections

NOT_EXISTS = (-1, -1)

n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 현재 위치
r, c = tuple(map(int, input().split()))
curr_cell = (r - 1, c - 1)

bfs_q = collections.deque()
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and \
           grid[x][y] < target_num


# visited 배열을 초기화 해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

            
def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    bfs_q.append(curr_cell)
    
    target_num = grid[curr_x][curr_y]
    
    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            
            if can_go(new_x, new_y, target_num):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True
            
def need_move(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    best_x, best_y = best_pos
    new_x ,new_y = new_pos

    return (grid[new_x][new_y], -new_x, -new_y) > \
           (grid[best_x][best_y], -best_x, -best_y)
def move():
    global curr_cell

    initialize_visited()

    bfs()

    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i,j) == curr_cell:
                continue
            new_pos = (i,j)
            if need_move(best_pos, new_pos):
                best_pos = new_pos

    if best_pos == NOT_EXISTS:
        return False
    else:
        curr_cell = best_pos
        return True

for _ in range(k):
    is_move = move()

    if not is_move:
        break


final_x, final_y = curr_cell
print(final_x + 1, final_y + 1)