#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<cmath>
#include<iomanip>

using namespace std;

int dp[100010];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n;
    
    cin >> n;
    
    vector<int> v;
    
    int cnt = 0;
    
    for(int i = 0; i < n; i++){
        int a;
        cin >> a;
        
        v.push_back(a);
        
        if(i >= 1){
            if(v[i] < v[i-1]){
                cnt++;
                dp[i-1] = cnt;
            }
            else{
                dp[i-1] = cnt;
            }
        }
    }
    
    dp[n-1] = cnt;
//
//    cout << "\n";
//
//    for(int i = 0; i < n; i++){
//        cout << dp[i] << " ";
//    }
//
//    cout << "\n";
    
    int m;
    cin >> m;
    
    for(int i = 0; i < m; i++){
        int a, b;
        
        cin >> a >> b;
        
        cout << dp[b-2] - dp[a-2] << "\n";
    }
    
    
    
    
}
