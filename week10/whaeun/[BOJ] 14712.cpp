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

int n, m, answer = 0;
int mapp[33][33];

void dfs(int cnt){
    if(cnt == n * m){
        answer++;
        return;
    }
    
    int x = cnt % m + 1;
    int y = cnt / m + 1;
    
    dfs(cnt + 1);
    
    bool check = true;
    
    if(mapp[y-1][x] && mapp[y][x-1] && mapp[y-1][x-1]){
        check = false;
    }
    
    if(check){
        mapp[y][x] = 1;
        dfs(cnt + 1);
        mapp[y][x] = 0;
    }
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n >> m;
    
    dfs(0);
    
    cout << answer;
}
