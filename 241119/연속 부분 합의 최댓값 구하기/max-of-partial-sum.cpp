#include <iostream>
using namespace std;
#include <climits>

const int MAX_N = 100001;  
int n;
int arr[MAX_N];
int dp[MAX_N];

void Initialize() {
    for(int i = 0; i < n; i++) {  
        dp[i] = INT_MIN;
    }
    dp[0] = arr[0];  
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) {  
        cin >> arr[i];
    }

    Initialize();  
    for(int i = 1; i < n; i++) {  
        dp[i] = max(dp[i-1] + arr[i], arr[i]);
    }

    int ans = dp[0]; 
    for(int i = 1; i < n; i++) {  
        ans = max(ans, dp[i]);
    }

    cout << ans;

    return 0;
}