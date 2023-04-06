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


ll w[101];
ll v[101];
ll dp[10001];
ll arr[101];


int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> k;
    
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    dp[0] = 1;
    for(ll i=0;i<n;i++){
        for(ll j=arr[i];j<=k;j++){
            dp[j] += dp[j - arr[i]];
        }
    }
    
    cout << dp[k];
    
    
    return 0;
    
}
