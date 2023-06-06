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

int n, answer = 0;

// 20 * 50 = 1000
int arr[4] = {1, 5, 10, 50};
bool visited[1010] = {0, };

void dfs(int cnt, int num, int total){
    if(cnt == n){
        if(visited[total] == false){
            visited[total] = true;
            answer++;
        }
        
        return;
    }
    
    for(int i = num; i < 4; i++){
        dfs(cnt + 1, i, total + arr[i]);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    dfs(0, 0, 0);
    
    cout << answer;
}
