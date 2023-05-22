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
    
    int n, m;
    
    cin >> n >> m;
    
    vector<int> v;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    for(int i = 0; i < m; i++){
        int a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    sort(v.begin(), v.end());
    
    for(int i = 0; i < n + m; i++){
        cout << v[i] << " ";
    }
    
}
