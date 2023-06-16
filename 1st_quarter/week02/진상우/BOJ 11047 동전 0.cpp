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
#define mod 1000000000
#define pii pair<int, int>
using ll = long long;
using namespace std;
ll n,m,k;
int l,r,t;
int h;




int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    
    cin >> n >> k;
    
    vector<ll>v;
    for(int i=0;i<n;i++){
        ll a;
        cin >> a;
        v.push_back(a);
    }
    
    sort(v.begin(), v.end(), greater<ll>());
    int ans = 0;
    
    for(int i=0;i<n;i++){
        if(k - v[i] >= 0){
            ans += (k / v[i]);
            k %= v[i];
            
            if(k <= 0)
                break;
        }
    }
    
    
    cout << ans;
    
    
   
    return 0;
    
}
