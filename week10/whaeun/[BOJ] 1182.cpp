#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<iomanip>

#define MAX 1000000007

using namespace std;

int n, s, answer = 0;

vector<int> v;

void dfs(int cnt, int total){
    if(cnt != n){
        if(total + v[cnt] == s){
            answer++;
        }
        
        
        dfs(cnt+1, total);
        dfs(cnt+1, total + v[cnt]);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n >> s;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    dfs(0, 0);
    
    cout << answer;
}
