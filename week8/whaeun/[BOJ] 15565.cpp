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

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int n, k;
    
    cin >> n >> k;
    
    vector<int> v;
    
    int min = 1000010;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        if(a == 1){
            v.push_back(i);
        }
    }
    
    if(v.size() < k){
        cout << -1;
    }
    else{
        
        int start = v[0], end = v[k-1];

        int min = end - start;
        for(int i = k-1; i < v.size(); i++){
            int x = v[i] - v[i-k+1];
            
            if(min > x){
                min = x;
            }
        }
        
        cout << min + 1;
        
    }
    
    
    
}
