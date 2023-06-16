#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<iomanip>

using namespace std;

int mapp[1030][1030];
int dp[1030][1030];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n, m;
    
    cin >> n >> m;
    
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            cin >> mapp[i][j];
            
            if(i == 0 && j == 0){
                dp[i][j] = mapp[i][j];
            }
            else if(j == 0){
                dp[i][j] = dp[i-1][j] + mapp[i][j];
            }
            else{
                dp[i][j] = dp[i][j-1] + dp[i-1][j] + mapp[i][j] - dp[i-1][j-1];
            }
        }
    }
    
    for(int i = 0; i < m; i++){
        int x1, y1, x2, y2;
        
        cin >> x1 >> y1 >> x2 >> y2;
        
        cout << dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1-1][y1-1] << "\n";
    }
    
    
    
}
