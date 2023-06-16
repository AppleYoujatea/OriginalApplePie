#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dp[1010];

int main(){
    
    int n;
    
    cin >> n;
    
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    
    for(int i = 3; i <= n; i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 10007;
    }
    
    cout << dp[n];
}
