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
    
    ll sum = 0;
    ll num1 = 0;
    ll num2 = 0;
    for(int i=0;i<n;i++){
        int a;
        cin >> a;
        num1 += a;
        num2 += a*a;
    }
    
    
    cout << (num1 * num1 - num2 >> 1);
    
    // -2 3 -6
    // -5
    // (a+b+c)(a+b+c)
    // 전체에서 a^2 + b^2 + c^2 를 빼주면 된다.
    
    
    return 0;
    
}
