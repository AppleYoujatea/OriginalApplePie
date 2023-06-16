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

int arr[16];

void dfs(int cnt){
    if(cnt == n){
        answer++;
        return;
    }
    
    for(int i = 0; i < n; i++){
        arr[cnt] = i;
        
        bool check = true;
        
        for(int j = 0; j < cnt; j++){
            // 같은 열, 대각선상에 위치
            if(arr[cnt] == arr[j] || cnt - j == abs(arr[cnt] - arr[j])){
                check = false;
            }
        }
        
        if(check){
            dfs(cnt+1);
        }
        
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> n;
    
    dfs(0);
    
    cout << answer;
}
