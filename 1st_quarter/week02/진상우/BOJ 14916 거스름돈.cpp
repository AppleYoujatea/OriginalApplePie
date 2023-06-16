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
    
    int ans = 0;
    int div = n % 5;
    
    if(n==1 || n==3)
        ans = -1;
    else if(div % 2 == 0)
        ans = (n / 5) + (div / 2);
    // 5로 나누었을 경우 div(5로 나눈 나머지)가 2로 나누어질 경우에
    // n / 5 의 몫 + div를 2로 나눈 몫을 더해준다.
    else
        ans = ((n / 5) - 1) + ((div + 5) / 2);
    // 나머지가 1,3일 경우에 5원인 동선은 하나 덜 사용한다.
    // 그러므로 뒤의 div에 5를 더해주고 2로 나누어 개수를 센다...
    
    cout << ans;
    
    
   
    return 0;
    
}

