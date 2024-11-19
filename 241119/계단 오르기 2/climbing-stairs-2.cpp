#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
   int n;
   cin >> n;
   
   vector<int> coins(n + 1);
   vector<vector<int>> dp(n + 1, vector<int>(4, INT_MIN));
   
   for(int i = 1; i <= n; i++) {
       cin >> coins[i];
   }
   
   dp[0][0] = 0;
   
   for(int i = 1; i <= n; i++) {
       for(int j = 0; j <= 3; j++) {
           if(j < 3 && dp[i-1][j] != INT_MIN) {
               dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + coins[i]);
           }
           
           if(i >= 2 && dp[i-2][j] != INT_MIN) {
               dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i]);
           }
       }
   }
   
   int ans = INT_MIN;
   for(int j = 0; j <= 3; j++) {
       ans = max(ans, dp[n][j]);
   }
   
   cout << ans;
   return 0;
}