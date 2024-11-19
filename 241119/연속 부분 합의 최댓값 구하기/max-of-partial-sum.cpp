#include <iostream>
using namespace std;
#include <climits>

const int MAX_N = 100001;  
int n;
int arr[MAX_N];
int dp[MAX_N];

void Initialize() {
    for(int i = 1; i <= n; i++) {
        dp[i] = INT_MIN;
    }
    dp[1] = arr[1];
}

int main() {
    cin >> n;
    for(int i = 0; i <= n; i++) {  
        cin >> arr[i];
    }

    Initialize();  
    for(int i = 2; i <= n; i++) {
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
    }

    int ans = INT_MIN;
    for(int i = 1; i <= n; i++) {
        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}