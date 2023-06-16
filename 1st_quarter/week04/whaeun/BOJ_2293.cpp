#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int dp[10010];

int main(){
    
    int n, k;
    
    cin >> n >> k;
    
    vector<int> coin;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        coin.push_back(a);
    }
    
    dp[0] = 1;
    
    for(int i = 0; i < n; i++){
        for(int j = coin[i]; j <= k; j++){
            dp[j] += dp[j-coin[i]];
        }
    }
    
    cout << dp[k];
    
    
    
}

