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


vector<ll>v;
ll Max = -1;

int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    
    cin >> k >> n;
    
    
    
    for(int i=0;i<k;i++){
        int a;
        cin >> a;
        v.push_back(a);
        
        if(a > Max)
            Max = a;
    }
    
    ll left = 1;
    ll right = Max;
    ll mid = 0;
    ll ans = 0;
    
    while(left <= right){
        mid = (left + right) / 2;
        
        ll num = 0;
        
        for(int i=0;i<k;i++){
            num += v[i] / mid;
        }
        
        // 더한 합이 n보다 클 경우에 더 줄일 수도 있으니까, 큰 쪽 부분(오른쪽 부분)을 탐색한다.
        if(num >= n){
            left = mid + 1;
            ans = max(ans, mid);
        }
        else{
            right = mid - 1;
        }
        // 더 작을 경우 작은 쪽 부분(왼쪽 부분)을 탐색한다.
        
    }
    
    cout << ans;
    
    
    
    
    
    

    
    return 0;
    
}



