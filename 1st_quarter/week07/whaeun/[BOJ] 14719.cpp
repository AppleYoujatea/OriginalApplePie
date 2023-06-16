#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>

using namespace std;

vector<vector<int>> rain;
vector<int> v;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, m;
    
    cin >> n >> m;
    
    for(int i = 0; i <= n; i++){
        rain.push_back(v);
    }
    
    for(int i = 1; i <= m; i++){
        int a;
        
        cin >> a;
        
        for(int j = 0; j < a; j++){
            rain[j].push_back(i);
        }
    }
    
    int ans = 0;
    
    for(int i = 0; i < n; i++){
        if(rain[i].size() >= 2){
            for(int j = rain[i].size() - 1; j > 0; j--){
                ans += rain[i][j] - rain[i][j-1] - 1;
            }
        }
    }
    
    cout << ans;
    
}
