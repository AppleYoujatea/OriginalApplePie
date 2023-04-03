#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dp[1010];

int main(){
    
    int n;
    
    cin >> n;
    
    vector<int> v;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++){
            if(v[j] < v[i]){
                if(dp[i] < dp[j]){
                    dp[i] = dp[j];
                }
            }
        }
        dp[i]++;
    }
    
    int answer = 0;
    
    for(int i = 0; i < n; i++){
        if(answer < dp[i]){
            answer = dp[i];
        }
    }
    
    cout << answer;
    
}
