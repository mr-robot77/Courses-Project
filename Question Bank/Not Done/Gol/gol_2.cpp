#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    
    vector<int> b(n+1);
    for (int i = 1; i <= n; i++) {
        cin >> b[i];
    }
    
    vector<vector<int>> dp(n+1, vector<int>(q+1, 0));
    
    for (int i = 1; i <= n; i++) {
        dp[i][0] = -1e6;
    }
    
    for (int j = 1; j <= q; j++) {
        dp[0][j] = -1e6;
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= q; j++) {
            dp[i][j] = max(dp[i-1][j-1] + b[i], dp[i][j-1]);
        }
    }
    
    for (int j = 1; j <= q; j++) {
        cout << dp[n][j] << endl;
    }
    
    return 0;
}
