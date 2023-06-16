

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


int arr[21];
int ans = 0;

void DFS(int num, int Sum){
    
    if(num == n)
        return;
    
    if(Sum + arr[num] == m)
        ans++;
    // 이를 합한 경우가 m이 되면 성립하므로 ans를 늘려준다.
    
    DFS(num+1, Sum);
    // 안넣고 그냥 가는 경우로 해보기
    DFS(num+1, Sum + arr[num]);
    // arr[num]를 더한 그걸로 해보기
    
    return;
    
    
}



int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> m;
    
    
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    
    DFS(0,0);
    
    cout << ans;
    
    
    
    return 0;
    
}


