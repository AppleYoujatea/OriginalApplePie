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

int roma[5] = {1, 5, 10, 50};
bool check[1001];
int ans = 0;

void DFS(int num, int idx, int Sum){
    if(num == n){
        if(check[Sum] == false){
            check[Sum] = true;
            ans++;
        }
        return;
    }
    // num이 n일 때, 끝났으로 Sum에 대해서 false인 경우 true로 바꾸고, ans를 늘린다.
    // 이 부분을 넘으면 return해준다.
    
    for(int i=idx;i<4;i++){
        DFS(num+1, i, Sum + roma[i]);
    }
    // idx는 지금 위치를 의미하고, 하나씩 증가시킨다.
    // roma[i]를 증가시켜준다.
    
    
}





int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    
    cin >> n;
    
    
    DFS(0,0,0);
    
    cout << ans;
    
    
    return 0;
    
}

