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


// I, V, X, L
// 1, 5, 10, 50

int arr[27][27];
bool check[27][27];
int ans = 0;


int DFS(int a, int b){
    int ans = 0;
    
    if(b > m){
        a++;
        b = 1;
    }
    // b가 m보다 클 경우에 a를 증가시켜주고, b를 1로 만들어서 다시 찾는다.
    // 즉 다음 행으로 넘어가는 것
    
    if(a > n)
        return 0;
    // 다음으로 넘어간 행이 n을 넘으면 0을 리턴하는 것 끝났으므로..
    
    if(!check[a-1][b] || !check[a][b-1] || !check[a-1][b-1]){
        
        // 하나라도 false면 넴모가 아니므로 들어간다.
        
        check[a][b] = true;
        ans += (DFS(a, b+1) + 1);
        check[a][b] = false;
        
        // true로 하고, ans에 DFS의 값을 b+1을 해주고 +1 해준 다음에 ans에 더한다.
        // 그리고 a,b를 다시 false로 한다.
    }
    
    ans += DFS(a, b+1);
    
    return ans;
    
}



int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    
    cin >> n >> m;
    
    int num = DFS(1,1);
    
    cout << num + 1;
    
    
    
    return 0;
    
}


