// Side Case
// 1. 0 0 0 
// 2. 0 0
// 3. -1 1 0
// 4. -2 0 2 -1
// 5. 0 1 2 3 - 0과 자기 자신이 합쳐져 숫자가 형성되는 경우
// 6. 0 0 -1 2

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
    map<int, int> mp;
    
    int zero_cnt = 0;
    bool check_zero = false;
    
    for(int i = 0; i < n; i++){
        int a;
        
        cin >> a;
        
        if(a == 0){
            zero_cnt++;
        }
        
        v.push_back(a);
    }
    
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            mp[v[i] + v[j]]++;
            
            if(v[i] + v[j] == 0 && v[i] != 0 && v[j] != 0){
                check_zero = true;
            }
        }
    }
    
    int cnt = 0;
    
    for(int i = 0; i < n; i++){
        if((zero_cnt && mp[v[i]] > zero_cnt && v[i] != 0) || (!zero_cnt && mp[v[i]]) || (v[i] == 0 && (check_zero || zero_cnt >= 3))){
            cnt++;
        }
    }
    
    cout << cnt;
    
}
