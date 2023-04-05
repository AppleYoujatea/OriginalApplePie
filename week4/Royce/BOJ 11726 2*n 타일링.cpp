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

    
    int dp[1001];
    
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    dp[4] = 5;
    
    cin >> n;
    
    if(n >= 4){
        for(int i=1;i<=n-2;i++){
            dp[i+2] = (dp[i+1] + dp[i]) % 10007;
        }
    }
    cout << dp[n] % 10007;
    
    
    return 0;
    
}
