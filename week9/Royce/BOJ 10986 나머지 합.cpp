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


int arr[1000001];
int tmp[1001];


int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> m;
    
    
    for(int i=1;i<=n;i++){
        cin >> arr[i];
        
        arr[i] = arr[i] + arr[i-1];
        // 전의 것을 더해서 넣어준다.
        arr[i] %= m;
        // modulo 연산을 위해 사용한 것
        tmp[arr[i]]++;
        // arr의 값을 tmp에 넣어준다.
    }
    
    ll num = tmp[0];
    for(int i=0;i<m;i++){
        ll ans = tmp[i];
        num += ans * (ans - 1) / 2;
        // (n-1) 까지의 합
    }
    
    cout << num;
    
    // 합[j] - 합[i] % m == 0 이 되는 i,j의 쌍을 구하는 것
    // modulo 연산을 해준 arr 값을 이용하여 이 값을 tmp에 넣어 개수를 세준다.
    
    // 각각 개수 별로 거기까지의 합이 모두 성립하게 되므로, 1 ~ (n-1)의 합을 더해준다.
    
    return 0;
    
}
