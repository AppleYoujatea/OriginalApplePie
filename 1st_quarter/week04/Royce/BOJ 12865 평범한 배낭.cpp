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


int w[101];
int v[101];
int dp[101][100001];


int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> k;
    
    // dp[i][j]에서 i는 물건의 개수, j는 무게를 뜻한다.
    // 물건 개수, 무게에 맞는 최대 값을 찾는다.
    
    for(int i=1;i<=n;i++){
        cin >> w[i] >> v[i];
    }
    
    for(int i=1;i<=n;i++){
        for(int j=1;j<=k;j++){
            if(j - w[i] >= 0){
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i]);
            }
            else{
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    
    cout << dp[n][k];
    
    
    
    return 0;
    
}
