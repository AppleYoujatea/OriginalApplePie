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
int n,m,k;
int l,r,t;
int h;




int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    
    cin >> n;
    
    vector<int>v;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    
    sort(v.begin(), v.end(), greater<int>());
    
    ll sum = 0;
    ll Max = 0;
    
    for(int i=0;i<n;i++){
        sum = v[i] * (i + 1);
        // 버티는 중량 * (k개의 로프) 가 최대일 때를 구함
        
        if(sum > Max)
            Max = sum;
    }
    
    cout << Max;
    
    
   
    return 0;
    
}
