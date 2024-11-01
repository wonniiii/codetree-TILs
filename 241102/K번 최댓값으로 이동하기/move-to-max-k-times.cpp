#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

#define NOT_EXISTS make_pair(-1, -1)

int n, k;
vector<vector<int>> grid;
vector<vector<bool>> visited;
queue<pair<int, int>> q;
pair<int, int> curr_cell;

bool InRange(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < n;
}

bool CanGo(int x, int y, int num) {
    if (!InRange(x, y)) 
        return false;
    if (visited[x][y] || grid[x][y] >= num) 
        return false;
    return true;
}

void InitializeVisited() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            visited[i][j] = false;
        }
    }
}

void BFS() {
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    int curr_x, curr_y;
    tie(curr_x, curr_y) = curr_cell;
    visited[curr_x][curr_y] = true;
    q.push(curr_cell);
    int target_num = grid[curr_x][curr_y];

    while (!q.empty()) {
        pair<int, int> curr_pos = q.front();
        tie(curr_x, curr_y) = curr_pos;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int next_x = curr_x + dx[i];
            int next_y = curr_y + dy[i];

            if (CanGo(next_x, next_y, target_num)) {
                visited[next_x][next_y] = true;
                q.push(make_pair(next_x, next_y));
            }
        }
    }
}

bool NeedUpdate(pair<int, int> best_pos, pair<int, int> new_pos) {
    if (best_pos == NOT_EXISTS)
        return true;

    int best_x, best_y;
    tie(best_x, best_y) = best_pos;

    int new_x, new_y;
    tie(new_x, new_y) = new_pos;

    return make_tuple(grid[new_x][new_y], -new_x, -new_y) > make_tuple(grid[best_x][best_y], -best_x, -best_y);
}

bool Move() {
    InitializeVisited();
    BFS();

    pair<int, int> best_pos = NOT_EXISTS;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j] || make_pair(i, j) == curr_cell) {
                continue;
            }
            pair<int, int> new_pos = make_pair(i, j);
            if (NeedUpdate(best_pos, new_pos))
                best_pos = new_pos;
        }
    }
    if (best_pos == NOT_EXISTS) {
        return false;
    } else {
        curr_cell = best_pos;
        return true;
    }
}

int main() {
    cin >> n >> k;

    grid.resize(n, vector<int>(n));
    visited.resize(n, vector<bool>(n, false));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) 
            cin >> grid[i][j];

    int r, c;
    cin >> r >> c;
    curr_cell = make_pair(r - 1, c - 1);

    while (k--) {
        bool is_moved = Move();
        
        if (!is_moved)
            break;
    }
    
    int final_x, final_y;
    tie(final_x, final_y) = curr_cell;
    cout << final_x + 1 << " " << final_y + 1;
}