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

long long mapp[1030][1030];
long long dp[1030][1030];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    
    int n, m;
    
    cin >> n >> m;
    
    long long max_num = -10010;
    int max_x = 0, max_y = 0;
    
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
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
                        
            if(dp[i][j] > max_num){
                max_num = dp[i][j];
            }
        }
    }

    
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= m; j++){
            
            for(int k = i; k <= n; k++){
                for(int l = j; l <= m; l++){
                    long long num = dp[k][l] - dp[k][j - 1] - dp[i - 1][l] + dp[i-1][j-1];
                    
                    if(num > max_num){
                        max_num = num;
                    }
                }
            }
            
            
        }
    }
    
    cout << max_num;
    
    
}
