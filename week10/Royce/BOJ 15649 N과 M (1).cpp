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


int arr[11];
bool check[11];

void DFS(int num){
    if(num == m){
        for(int i=0;i<m;i++)
            cout << arr[i] << " ";
        cout << '\n';
        return;
    }
    // m개가 되었을 때 출력해주고 리턴한다.
    
    for(int i=1;i<=n;i++){
        if(!check[i]){
            check[i] = true;
            arr[num] = i;
            DFS(num+1);
            check[i] = false;
        }
        // 아직 지나지 않았을 경우에 true로 표시해주고,
        // arr[num] 에 그러한 i를 넣어주고
        // DFS를 num+1으로 해서 들어간다.
    }
}



int main(){
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    
    cin >> n >> m;
    
    DFS(0);
    
    
    
    
    
    
    return 0;
    
}
