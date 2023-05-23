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
    
    long long n, m;
    
    cin >> n >> m;
    
    long long sum = 0;
    
    map<long long, long long> mp;
    
    for(int i = 0; i < n; i++){
        long long a;
        
        cin >> a;
        sum += (a % m);
        mp[sum % m]++;
    }
    
    long long cnt = 0;
    
    for (auto iter : mp) {
        cnt += iter.second * (iter.second - 1) / 2;
    }

    cout << cnt + mp[0];
}
