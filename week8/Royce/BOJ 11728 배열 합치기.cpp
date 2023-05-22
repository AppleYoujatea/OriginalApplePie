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

    
    cin >> n;
    
    vector<ll>v;
    for(int i=0;i<n;i++){
        ll a;
        cin >> a;
        v.push_back(a);
    }
    
    sort(v.begin(), v.end());
    
    // -99 -2 -1 4 98
    ll left = 0;
    ll right = v.size() - 1;
    
    ll a = left;
    ll b = right;
    ll sum = v[left] + v[right];
    while(left < right){
        if(v[left] + v[right] < 0){
            if(abs(sum) > abs(v[left] + v[right])){
                sum = v[left] + v[right];
                a = left;
                b = right;
            }
            left++;
        }
        else if(v[left] + v[right] > 0){
            if(abs(sum) > abs(v[left] + v[right])){
                sum = v[left] + v[right];
                a = left;
                b = right;
            }
            right--;
        }
        else{
            sum = v[left] + v[right];
            a = left;
            b = right;
            break;
        }
        
    }
//
//    for(auto k : v){
//        cout << k << " ";
//    }
//
//    cout << a << " " << b << '\n';
    cout << v[a] << " " << v[b];
    
    
    
    
    
    return 0;
    
}
