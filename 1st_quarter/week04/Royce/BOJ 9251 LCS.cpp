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


  


int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    string st1, st2;
    
    cin >> st1 >> st2;
    
    int dp[1001][1001];
    
    for(int i=1;i<=st1.length();i++){
        for (int j=1;j<=st2.length();j++){
            if(st1[i-1] == st2[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
                // 같은 경우에는 하나 늘려준당.
            }
            else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                // 같지 않을 경우에는 해당하는 부분이 없으므로 그냥 i-1,j i,j-1 중 하나를 고른다.
            }
        }
    }
    
    
    cout << dp[st1.length()][st2.length()];
    
    
    return 0;
    
}
