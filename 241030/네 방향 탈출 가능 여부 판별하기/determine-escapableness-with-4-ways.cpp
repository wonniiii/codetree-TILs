#include <iostream>
#include <vector>
#include <queue>   // queue를 사용하기 위해 필요
using namespace std;

// 전역 변수로 선언
vector<vector<int>> arr;
vector<vector<bool>> visited;
queue<pair<int, int>> q;
int N, M; 
int res;

bool InRange(int x, int y) {
    return 0 <= x && x < N && 0 <= y && y < M;  // 5 대신 N, M 사용
}

bool CanGo(int x, int y) {
    if(!InRange(x,y))
        return false;
    if(visited[x][y] || arr[x][y] == 0)
        return false;
    return true;
}

void Push(int x, int y) {
    visited[x][y] = true;
    q.push(make_pair(x,y));
}

void BFS() {
    int dx[4] = {1,-1,0,0};
    int dy[4] = {0,0,-1,1};

    while(!q.empty()) {
        pair<int, int> curr_pos = q.front();
        q.pop();  // 세미콜론 추가

        int x = curr_pos.first;
        int y = curr_pos.second;

        for(int i=0; i<4; i++) {
            int new_x = x+dx[i];
            int new_y = y+dy[i];

            if(CanGo(new_x, new_y))
                Push(new_x, new_y); 
        }
    }
}

int main() {
    cin >> N >> M;  // 전역 변수에 저장
    
    // 벡터 크기 초기화
    arr = vector<vector<int>>(N, vector<int>(M));
    visited = vector<vector<bool>>(N, vector<bool>(M, false));

    // 입력 받기
    for(int i=0; i<N; i++) {
        for(int j=0; j<M; j++) {
            cin >> arr[i][j];  // 세미콜론 추가
        }
    }

    Push(0,0);
    BFS();

    if (visited[N-1][M-1] == 1) {
        cout << 1;
    }else {
        cout << 0;
    }

    return 0;  // return 문 추가
}