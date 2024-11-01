#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> grid;
vector<vector<int>> step;
int n;

int main() {
    cin >> n;

    grid.resize(n,vector<int>(n));
    step.resize(n,vector<int>(n));

    for(int i =0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> grid[i][j];
        }
    }

    step[0][0] = grid[0][0];

    for(int i=1; i<n; i++) {
        step[i][0] = step[i-1][0] + grid[i][0];
    }

    for(int i=1; i<n; i++) {
        step[0][i] = step[0][i-1] + grid[0][i];
    }

    for(int i=1; i<n; i++) {
        for(int j=1; j<n; j++) {
            step[i][j] = max(step[i-1][j], step[i][j-1]) + grid[i][j];
        }
    }

   cout << step[n-1][n-1];

    return 0;
}