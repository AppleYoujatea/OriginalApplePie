#include <iostream>  // stdio.h 와 같은 것
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <cstring>
#include <cmath>
#include <functional>
#include <map>
#include <unordered_map>
#include <set>
#include <sstream>

// control i
#define MAX 987654321
#define mod1 1000000000
#define mod 1000000007
#define pii pair<int, int>
using ll = long long;
using namespace std;
int n,m,k;
int l,r,t;
int h;



int arr[210][210];
int dp[210][210];

int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> m;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            cin >> arr[i][j];
            if(i == 1 && j == 1){
                dp[i][j] = arr[i][j];
            }
            else if(i == 1 && j != 1){
                dp[i][j] = arr[i][j] + dp[i][j-1];
            }
            else if(i != 1 && j == 1){
                dp[i][j] = arr[i][j] + dp[i-1][j];
            }
            else{
                dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];
            }
        }
    }
    
    int ans = -MAX;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            for(int k=i;k<=n;k++){
                for(int l=j;l<=m;l++){
                    int num = dp[k][l] - dp[k][j-1] - dp[i-1][l] + dp[i-1][j-1];
                    ans = max(ans, num);
                }
            }
        }
    }
    // i ~ j 안에서 합을 구해야 하므로 4중 포문이 필요하다
    
    cout << ans;
    
    
    return 0;
    
}
