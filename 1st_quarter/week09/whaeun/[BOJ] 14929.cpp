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
    
    int n;
    
    cin >> n;
    
    vector<int> v;
    long long prefix_sum = 0;
    
    for(int i = 0; i < n; i++){
        int a;
        cin >> a;
        
        prefix_sum += a;
        v.push_back(a);
    }
    
    long long sum = 0;
    
    for(int i = 0; i < n; i++){
        sum += v[i] * (prefix_sum - v[i]);
        prefix_sum -= v[i];
    }
    
    cout << sum;
    
}
