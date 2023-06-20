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

int main(){
    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
    
    unsigned long long n, m;
    vector<unsigned long long> v;
    
    cin >> n >> m;
    
    for(int i = 0; i < n; i++){
        unsigned long long a;
        
        cin >> a;
        
        v.push_back(a);
    }
    
    sort(v.begin(), v.end());
    
    unsigned long long right = m * v[0];
    unsigned long long left = 1;
    unsigned long long mid = (left + right) / 2;
    
    unsigned long long ans = 0, sum = 0;
    
    while (right >= left) {
        sum = 0;
        mid = (left + right) / 2;
        
        for(int i = 0; i < n; i++){
            sum += (mid / v[i]);
        }
        
        if(sum >= m){
            if(ans > mid || ans == 0){
                ans = mid;
            }
            right = mid - 1;
        }
        else{
            left = mid + 1;
        }
    }
    
    cout << ans;
    
}
