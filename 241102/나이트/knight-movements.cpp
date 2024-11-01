#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<bool>> visited;
vector<vector<int>> step;
queue<pair<int,int>> q;

int n;

bool InRange(int x, int y) {
    return 0<=x && x<n && 0<=y && y<n;
}

bool CanGo(int x, int y) {
    if(!InRange(x,y)) {
        return false;
    }
    if(visited[x][y]) {
        return false;
    }
    return true;
}

void Push(int x, int y, int num) {
    visited[x][y] = true;
    q.push(make_pair(x,y));
    step[x][y] = num;
}

void BFS() {
    int dx[8] = {1,2,2,1,-1,-2,-2,-1};
    int dy[8] = {-2,-1,1,2,-2,-1,1,2};

    while(!q.empty()) {
        pair<int,int> curr = q.front();
        int curr_x, curr_y;
        tie(curr_x, curr_y) = curr;
        q.pop();

        for(int i=0; i<8; i++) {
            int new_x = curr_x + dx[i];
            int new_y = curr_y + dy[i];

            if(CanGo(new_x, new_y)) {
                Push(new_x, new_y, step[curr_x][curr_y]+1);
            }
        }
    } 
}

int main() {
    cin >> n;

    visited.resize(n,vector<bool>(n,false));
    step.resize(n,vector<int>(n,-1));

    int arr[4];
    for(int i = 0; i<4; i++) {
        cin >> arr[i];
    }

    // 1부터 시작하는 좌표를 0부터 시작하도록 변환
    Push(arr[0]-1, arr[1]-1, 0);
    BFS(); // BFS 함수 호출 추가

    
    cout << step[arr[2]-1][arr[3]-1];
    
    return 0;
}