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
ll n,m,k;
int l,r,t;
int h;





int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll s;
    cin >> s;
    
    n = 1;
    
    while(n*(n+1) / 2 <= s){
        n++;
    }
    // n까지의 합을 더했을 때, s보다 작을 경우 n을 계속 늘린다.
    // 최대값이므로 1부터 해서 주르륵 계산하는 것이 좋다.
    
    cout << n-1;
    
    
    

    
    return 0;
    
}



