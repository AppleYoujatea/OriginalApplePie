#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[110][100010];

int main(){
    int n, k;
    
    cin >> n >> k;
    
    vector<pair<int, int>> knapsack;
    
    knapsack.push_back({0,0});
    
    for(int i = 0; i < n; i++){
        int w, v;
        
        cin >> w >> v;
        
        knapsack.push_back({w, v});
    }
    
    for(int i = 1;  i <= n; i++){
        for(int j = 1;  j <= k; j++){
            if(j >= knapsack[i].first){
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-knapsack[i].first] + knapsack[i].second);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    
    cout << dp[n][k];
}
